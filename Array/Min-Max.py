
def find_min_max(arr, n):
    i=0
    if n % 2 == 0:
        if arr[0] > arr[1]:
            max_val=arr[0]
            min_val=arr[1]
        else:
            max_val=arr[1]
            min_val=arr[0]

        i=2
    else:
        min_val=arr[0]
        max_val=arr[0]

        i=1

    while i < n-1:
        if arr[i] > arr[i+1]:
            if arr[i] > max_val:
                max_val=arr[i]

            if arr[i+1] < min_val:
                min_val = arr[i+1]

        else:
            if arr[i] < min_val:
                min_val=arr[i]

            if arr[i+1] > max_val:
                max_val=arr[i+1]

        i+=2

    print("Min Malue= ", min_val)
    print("Max Malue= ", max_val)





# Example
arr = [7, 2, 9, 4, 1, 8]
n = len(arr)

find_min_max(arr, n)

