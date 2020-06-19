def main():
    arr = []
    with open('integerarray.txt', 'r') as file:
        for line in file:
            arr.append(int(line))
    
    # arr = [1, 3, 5, 2, 4, 6]
    # arr = [20, 60, 30, 70, 40, 50, 10]
    # arr = [1, 2, 3, 4, 5, 10, 12, 15, 6, 7, 8, 9, 11, 13, 14, 16, 32, 35, 70]

    # print(arr)
    print(mergeSort(arr))
    # print(arr)


def mergeSort(arr):
    if len(arr) == 1:
        return 0
    middle = len(arr) // 2
    L = arr[:middle]
    R = arr[middle:]
    inv_count = 0

    # count the no. of inversion in the left half
    inv_count += mergeSort(L)
    # count the no. of inversion in the right half
    inv_count += mergeSort(R)
    # count the no. of split inversion
    inv_count += merge(arr, L, R)
    return inv_count
    # return arr


def merge(arr, left_half_array, right_half_array):
    i = j = k = 0
    inv_count = 0
    while i < len(left_half_array) and j < len(right_half_array):
        if left_half_array[i] <= right_half_array[j]:
            arr[k] = left_half_array[i]
            i += 1
        else:
            arr[k] = right_half_array[j]
            j += 1
            # counts the number of inversion
            inv_count += len(left_half_array) - i
        k += 1

    #copy the remaining elements to end of array if any
    while i < len(left_half_array):
        arr[k] = left_half_array[i]
        i += 1
        k += 1
    while j < len(right_half_array):
        arr[k] = right_half_array[j]
        j += 1
        k += 1
    
    return inv_count
    # return arr


if __name__ == "__main__":
    main()