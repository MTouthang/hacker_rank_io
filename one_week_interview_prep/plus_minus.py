'''' Given an array of integer find the ratio of positive,
    negative and zero. Print the decimal value of each fraction on a new line
    with 6 decimal places'''

arr= [-4,3, -9, 0, 4, 1]

def plusMinus(arr):
    pos =0
    neg = 0
    zero = 0
    for i in arr:
        if i>0:
            pos +=1
        if i<0:
            neg +=1
        if i==0:
            zero +=1

    print("pos: {0}, neg: {1}, zero: {2}".format(pos, neg, zero))

    print("Print the decimal value of each fraction on a new linewith 6 decimal places")

    print("pos: ", round((pos / len(arr)),6))
    print("neg: ", round((neg / len(arr)), 6))
    print("zero: ", round((zero / len(arr)), 6))

plusMinus(arr)
