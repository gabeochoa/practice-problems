#!/usr/bin/python


#O(n^2)
def et_tu(arr, n):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i != j):
                if(arr[i] + arr[j] == n):
                    return True
    return False

def trees(arr, n):
    sorted(arr)
    l = 0
    r = len(arr)-1
    while l<r:
        ts = arr[l] + arr[r]
        if(ts > n):
            r-=1
        elif(ts < n):
            l+=1
        else:
            return True
    return False

def match(arr, n):
    return trees(arr, n) and et_tu(arr, n)

def main():
    assert match([0,0,0,0,0,0], 1) == False
    assert match([0,0,1,0,0,0], 1) == True
    assert match([1,2,3,4,5], 6) == True
    assert match([1,2,3,4,5], 8) == True
    assert match([1,2,3,4,5], 9) == True
    assert match([1,2,3,4,5], 10) == False
    assert match([1,2,3,4,5], 11) == False

    


main()