def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for passno in range(n):
        # Flag to optimize for already sorted arrays
        swapped = False
        # Last passno elements are already in place
        for i in range(0, n - passno - 1):
            # Compare adjacent elements
            if arr[i] > arr[i + 1]:
                # Swap if they are in wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    arr = eval(input("Enter values inside '[]' : "))
    print("\nExample 2 - Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Example 2 - Sorted array:", sorted_arr)
