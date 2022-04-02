'''' Given five positive integers, find the minimum and maximum values that can be calculated by
summing exactly four of the five integers. The print the respective minimum and maximum value
as single line of two space-separated long integers
'''

def mini_max(arr):
    total = []

    # sum1 = total.append(arr[1] + arr[2] + arr[3] + arr[4])
    # sum1 = total.append(arr[0] + arr[2] + arr[3] + arr[4])
    # sum1 = total.append(arr[0] + arr[1] + arr[3] + arr[4])
    # sum1 = total.append(arr[0] + arr[1] + arr[2] + arr[4])
    # sum1 = total.append(arr[0] + arr[1] + arr[2] + arr[3])

    for i in range(len(arr)):
        total.append(sum(arr) - arr[i])
       
    print(min(total), max(total))

arr1 = [1, 3, 5, 7, 9]
mini_max(arr=arr1)