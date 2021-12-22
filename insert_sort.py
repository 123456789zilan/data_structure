'''
for j = 2 to A.lengh
    key = A[j]
    //insertA[j] into a sorted sequence A[1...j-1]
    i = j -1 
    
    while i > 0 and A[i] > key
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = key
'''

def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[i] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr

# Testing 
if __name__ == '__main__' :
    a= [10,10,6,7,9]
    print(insert_sort(a))