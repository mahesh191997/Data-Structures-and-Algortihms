"""Function takes list as input and tells wheather the element is in the array or not
Time Complexity: O(log2(n))"""

def BinarySearch(array, val):
    low = 0
    high = len(array) - 1
    mid = (low + high)//2    #'//' means floor division
    found = False
    while(low<=high and not found):
        if(val==array[mid]):
            found = True
        elif(val<array[mid]):
            high = mid - 1
        elif(val>array[mid]):
            low = mid + 1 
        mid = (low + high)//2
    if(found):
        return array.index(val)
    else:
        return -1
BinarySearch([0,2,3,4],4)