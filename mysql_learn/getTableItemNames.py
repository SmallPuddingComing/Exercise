#coding:utf8

import MySQLdb
from MySQLdb.cursors import DictCursor

try:
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
    cur = conn.cursor(DictCursor) #查询结果返回一个字典
    conn.select_db('test')
    cur.execute('select name from player')
    result = cur.fetchall()
    # conn.commit()
    cur.close()
    conn.close()
    print result
except MySQLdb.Error, msg:
    print "MySQLdb Erro %d: %s" % (msg.args[0],str(msg.args[1]))

#get rollnames from tablename in mysql
def getTableItemNames(tablename):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
    cursor = conn.cursor(DictCursor) #查询结果返回一个字典
    conn.select_db('test')
    cursor.execute("describe %s" % tablename)#得到表的列的属性和名字
    dbnameList = cursor.fetchall()
    cursor.close()
    conn.close()

    dbnameList = [data['Field'] for data in dbnameList]
    return dbnameList

#删除数据条有主键约束
def clearPlayerData():
    sqlList = ["DELETE FROM PLAYER WHERE id=%d"%(2),
               "DELETE FROM POLL WHERE id=%d"%(0)]
    if executeSqlList('test',sqlList):
        print "clear over"

#批量操作sql语句
def executeSqlList(tablename, sqlList):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
    cursor = conn.cursor(DictCursor) #查询结果返回一个字典
    conn.select_db('test')
    for sql in sqlList:
        if isinstance(sql, tuple):
            cursor.execute(*sql)
        else:
            cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return True

#生成字符串查询语句
def formatCondition(props):
    args = []
    itemsList = []
    for key, val in props.iteritems():
        args.append(val)
        itemsList.append("%s = %s AND" % (key, "%s"))
    sqlList = ''.join(itemsList)
    return sqlList[:-4], args

#每一条增加的数据插入到参数Props中，这个props是生成查询语句条件的
def forEachPlusInsertProps(tableName, props):
    assert(isinstance(props, dict))
    pvaluestr = "%s," * len(props)
    pvaluestr = pvaluestr[:-1]
    pkeystr = str(tuple(props.keys())).replace('\'', '`')
    args = []
    for val in props.itervalues():
        args.append(val)
    sqlStr = "INSERT INTO `%s` %s values (%s)" % (tableName, pkeystr, pvaluestr)
    return sqlStr, args

#批量insert保存数据库
def saveDBList(tabkeName, dataList):
    sqlList = []
    for data in dataList:
        sql = forEachPlusInsertProps(tabkeName, data) #这里得到的是个元组（sqlStr, args）
        sqlList.append(sql)
    return executeSqlList(tabkeName, sqlList)

#单个事务的启动，进行数据的查询
def readDataFromDB(tableName, props=None, batch=None, items=None):
    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
    cursor = conn.cursor(DictCursor)
    conn.select_db('test')

    if batch: #多条行的搜索
        pkName = batch['pkName']
        count = batch['count']
        if props: #有条件
            prers, args = formatCondition(props)
            sql = "select %s from %s where %s" % (pkName, tableName, prers)
        else:
            args = None
            sql = "select %s from %s" % (pkName, tableName)

        cursor.execute(sql, args)
        result = cursor.fetchall()
        pkList = [data[pkName] for data in result]
        result = getRecordList(tableName, pkName, pklist=pkList,items=items,count=count) #多条行数据进行字段的筛选
    else:
        if items: #多条列的搜索
            items = ','.join(["%s"] * len(items)) % tuple(items)
        else:
            items = "*"

        if props: #有条件
            prers, args = formatCondition(props)
            sql = "select %s from %s where %s" % (items, tableName,prers)
        else:
            args = None
            sql = "select %s from %s " % (items, tableName)

        cursor.execute(sql, args)
        result = cursor.fetchall()

    cursor.close()
    conn.close()
    return result

#单个事务的开启，进行多行数据的列字段的筛选, 给定一个数量
def getRecordList(tableName, pkname, pklist, items=None, count=0):
    if items:
        items = ','.join(['`%s`'] * len(items)) % tuple(items)
    else:
        items = '*'

    conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', port=3306)
    cursor = conn.cursor(DictCursor)
    conn.select_db('test')

    #查询pklist中所有行的截取列字段
    def readRecordList(pklist):
        pkListStr = ",".join(["%s"] * len(pklist))
        sql = "select %s from %s where %s in (%s)" % (items, tableName, pkname, pkListStr)
        cursor.execute(sql, pklist)
        return cursor.fetchall()

    if count:
        pos = 0
        result = []
        while pos < len(pklist):
            newPos = pos + count
            result.extend(readRecordList(pklist[pos:newPos]))
            pos = newPos
    else:
        result = readRecordList(pklist)


    return result

if __name__ == '__main__':
    result = getTableItemNames('user')
    print "have a table rollname", result

    clearPlayerData()

    #多条数据插入数据库
    # dataList = [{'id':'114151','name':'qq'},{'id':'114152', 'name':'ww'}, {'id':'114153', 'name':'ee'}]
    # print "inset into many data is ", saveDBList('player', dataList)

    #查询多条数据
    props = {'level':20}
    # batch = {'pkName':['11', '114151', '114152', '114153', '115', '118'], 'count':3}
    batch = {'pkName':'name', 'count':3}
    items = ['id', 'name']
    print "get many date from player no items", readDataFromDB('player', props=props, batch=batch, items=None)

    #查询多条数据的指定列字段
    items = ['sex']
    print "get many data from palyer have items[sex]", readDataFromDB('player', props=props, batch=batch, items=items)

    #查询单条数据的指定字段
    items = ['name', 'sex']
    print "get one data from player have item[name, sex]", readDataFromDB('player', props=props, batch=None, items=items)

    #实践证明，patch里面存放的是pkName是主键，count是数量每次读取的行数
    #items里面放的就是需要截取的字段名