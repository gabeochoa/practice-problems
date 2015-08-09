#!/usr/bin/python

'''
    We use modulos math to jump to the correct spot,
    this fails when we have a jumping pattern
    that wont reach every cell

    In that case where len(arr)%n==0, 
    we just use a secondary array
'''


def et_tu(arr, n):
    print (arr),
    print " " + str(n),
    print " -> ",
    if(len(arr) <= 1 or n == 0):
        print (arr)
        return arr

    count = 0
    while count < n:
        end = arr[len(arr)-1]
        i = len(arr) - 1
        while i > 0:
            arr[i] = arr[i-1]
            i-=1
        arr[0] = end
        count += 1
    print (arr)
    return arr

def jump(arr, n):
    print (arr),
    print " " + str(n),
    print " -> ",

    if(len(arr) <= 1 or n == 0):
        print (arr)
        return arr

    if len(arr) % n == 0:
        return et_tu(arr,n)
        # lst = [0 for i in range(len(arr))]
        # for i in range(len(arr)):
        #     ind = (i+(n%len(arr)))%len(arr)
        #     lst[ind] = i
        # arr = lst
    else:
        nummv = 0
        i = 0
        next = arr[i]
        save = arr[i]
        while True:
            ind = (i+(n%len(arr)))%len(arr)
            save = arr[ind]
            arr[ind] = next
            next = save
            i = ind
            nummv += 1
            if(nummv == len(arr)):
                break;
    print (arr)
    return arr

def rotate(arr, n):
    return jump(arr, n)

def main():
    assert rotate([], 0) == []
    assert rotate([], 4) == []
    assert rotate([1], 0) == [1]
    assert rotate([1], 5) == [1]
    assert rotate([1,2,3], 1) == [3,1,2]
    assert rotate([1,2,3], 3) == [1,2,3]
    assert rotate([1,2,3,4,5], 3) == [3,4,5,1,2]

    a1 = [1, 2, 3, 4, 5, 6, 1, 2, 3]
    a1s = [1, 2, 3, 1, 2, 3, 4, 5, 6]
    assert rotate(a1, 3) == a1s


main()