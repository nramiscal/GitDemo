'''
Shift Array Values Left

Given an array, move all values forward (to the left) by one index, dropping the first value and leaving a 0 (zero) value at the end of the array.

[1,2,3,4,5]
[2,3,4,5,5]
[2,3,4,5,0]
'''

def shiftArrayValsLeft(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[len(arr)-1] = 0

    return arr

print(shiftArrayValsLeft([1,2,3,4,5]))

'''
Square Array Values
Square each value in a given array, returning that same array with changed values.
'''

def squareArrayVals(arr):
    for i in range(len(arr)):
        arr[i] *= arr[i]

    return arr

# print(squareArrayVals([1,2,3,4,5]))


'''
Return Odds Array 1-255
Create an array with all the odd integers between 1 and 255 (inclusive).
'''

def returnOddsArray1To255():
    # newarr = []
    # for i in range(1,256,2):
    #     newarr.append(i)
    #
    # return newarr

    return list(range(1,256,2))


# print(returnOddsArray1To255())


'''
Print Max, Min, Average Array Values
Given an array, print the max, min and average values for that array.
'''

def printMaxMinAverageArrayVals(arr):

    min = arr[0]
    max = arr[0]
    sum = 0

    # for i in range(len(arr)):
    #     print(arr[i])

    for val in arr:
        if val < min:
            min = val
        elif val > max:
            max = val
        sum += val

    return {
        "max": max,
        "min": min,
        "avg": sum/len(arr)
    }

    # return f"min: {min}, max: {max}, avg: {sum/len(arr)}"

# print(printMaxMinAverageArrayVals([1,2,3,4,5]))

'''
Reverse an Array
'''

def reverseArray(arr):
    i = 0
    while i < len(arr)//2:
        temp = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = arr[i]
        arr[i] = temp
        i += 1

    return arr

    # left = 0
    # right = len(arr)-1
    #
    # while left < right:
    #     temp = arr[left]
    #     arr[left] = arr[right]
    #     arr[right] = temp
    #     left += 1
    #     right -= 1
    #
    # return arr

# print(reverseArray([1,2,3,4,5,6,7]))
