#coding:utf8
#冒泡算法：原理是前一个和后一个进行比较，一次交换,最多是n-1次循环
def bublle_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return None

    for i in xrange(iter_len-1):
        for j in xrange(iter_len-i-1):
            if sort_list[j] < sort_list[j+1]:
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
    return sort_list

#插入排序:原理是首先保存一个key值，然后根据当前的循环找到比当前key小的值，这个时候就依次循环到key放置到首位
def insertion_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return None

    for i in xrange(iter_len):
        key = sort_list[i]
        j = i-1
        while j>=0 and sort_list[j] > key:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key
    return sort_list

#选择排序:从前往后，拿第一个元素和最小值交换，再拿第二个元素和剩下的最小的交换。。。
def selection_sort(sort_list):
    iter_len = len(sort_list)
    if iter_len < 2:
        return None

    for i in xrange(iter_len-1):
        smaller = sort_list[i]
        localtion = i
        for j in xrange(i, iter_len):
            if smaller > sort_list[j]:
                smaller = sort_list[j]
                localtion = j
        if i != localtion:
            sort_list[i], sort_list[localtion] = sort_list[localtion], sort_list[i]
    return sort_list

#快速排序
def quik_sort(sort_list, low, high):
    i = low
    j = high
    if i > j:
        return sort_list

    key = sort_list[i]
    if i < j:
        while i<j and sort_list[j] >= key:
            j -= 1
        sort_list[i] = sort_list[j]
        while i<j and sort_list[i] <= key:
            i += 1
        sort_list[j] = sort_list[i]
    sort_list[i] = key
    quik_sort(sort_list, low, i-1)
    quik_sort(sort_list, j+1, high)



if __name__ == '__main__':
    mylist = [6,5,4,7,8,2]
    # bub = bublle_sort(mylist)
    # print "冒泡排序 result is", bub

    insert = insertion_sort(mylist)
    print "插入排序 result is", insert

    # select = selection_sort(mylist)
    # print "选择排序 result is ", select

    # quik = quik_sort(mylist, 0, 5)
    # print "快速排序 result is", quik

