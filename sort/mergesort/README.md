
# Merge Sort in Python

Merge Sort is a popular and efficient sorting algorithm that follows the divide-and-conquer paradigm. It divides the input array into two halves, recursively sorts them, and then merges the sorted halves to produce a fully sorted array. Merge Sort is stable, meaning it preserves the relative order of equal elements, and has a time complexity of O(n log n) in all cases.

This article explains how Merge Sort works and provides a Python implementation with detailed explanations.

## How Merge Sort Works

1. **Divide**: Split the input array into two halves until each subarray contains a single element (or is empty). A single element is considered sorted.
2. **Conquer**: Recursively sort the two halves.
3. **Merge**: Combine the sorted halves into a single sorted array by comparing elements and placing them in the correct order.

The merging process is the core of the algorithm, ensuring that elements from the two sorted subarrays are combined into a single sorted array.

## Python Implementation

Below is a Python implementation of the Merge Sort algorithm.

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)



def merge(left, right):
    result = []
    i = j = 0
    
    # Compare elements from both arrays and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array, if any
    result.extend(left[i:])
    
    # Add remaining elements from right array, if any
    result.extend(right[j:])
    
    return result

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
```

### Explanation of the Code

- **merge_sort(arr)**:
  - **Base Case**: If the array has 1 or 0 elements, it is already sorted, so return it.
  - **Divide**: Compute the midpoint of the array using integer division (`len(arr) // 2`). Split the array into `left` (elements from start to midpoint) and `right` (elements from midpoint to end).
  - **Conquer**: Recursively call `merge_sort` on the `left` and `right` halves to sort them.
  - **Merge**: Call the `merge` function to combine the sorted `left` and `right` arrays.

- **merge(left, right)**:
  - Create an empty `result` list to store the merged array.
  - Use two pointers, `i` and `j`, to track the current position in the `left` and `right` arrays.
  - Compare elements from `left[i]` and `right[j]`. Append the smaller element to `result` and increment the corresponding pointer.
  - After one array is exhausted, append any remaining elements from the other array to `result`.
  - Return the merged `result` array.

- **Example Usage**: The main block demonstrates sorting an example array `[64, 34, 25, 12, 22, 11, 90]`. The output will be:
  ```
  Original array: [64, 34, 25, 12, 22, 11, 90]
  Sorted array: [11, 12, 22, 25, 34, 64, 90]
  ```

## Time and Space Complexity

- **Time Complexity**: O(n log n)
  - The array is divided into two halves log n times (since each division halves the array size).
  - Merging takes O(n) time for each level of recursion, as it processes all elements.
  - Total: O(n) * O(log n) = O(n log n) for best, average, and worst cases.
- **Space Complexity**: O(n)
  - The algorithm requires additional space for the temporary arrays during merging.
  - The recursion stack also uses O(log n) space, but the dominant factor is the O(n) space for the merged arrays.

## Advantages of Merge Sort

- **Stable Sorting**: Maintains the relative order of equal elements.
- **Predictable Performance**: Always O(n log n), regardless of input data.
- **Suitable for Large Datasets**: Efficient for sorting large datasets, especially when data is stored in linked lists or external storage (e.g., disk-based sorting).

## Disadvantages of Merge Sort

- **Space Usage**: Requires O(n) extra space for merging, which can be a drawback for memory-constrained systems.
- **Not In-Place**: Unlike algorithms like Quick Sort, Merge Sort does not sort the array in-place, leading to higher memory usage.
- **Slower for Small Arrays**: For small inputs, the overhead of recursion and merging can make it slower than simpler algorithms like Insertion Sort.

## When to Use Merge Sort

- **Linked Lists**: Merge Sort is highly efficient for sorting linked lists, as it avoids random access and only requires sequential access during merging.
- **External Sorting**: Ideal for sorting data that doesn’t fit in memory (e.g., sorting large files on disk).
- **Stable Sorting Requirement**: Use when maintaining the relative order of equal elements is important.
- **Parallel Processing**: Merge Sort can be parallelized, as the divide step can be processed independently.

<br>

## Language-Agnostic Version of Merge Sort

```python
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    
    L = [0] * n1
    R = [0] * n2
    
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]
    
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("Sorted array:", arr)
```

## Conclusion

Merge Sort is a reliable and efficient sorting algorithm with a consistent O(n log n) time complexity. Its divide-and-conquer approach makes it versatile for various applications, particularly when stability or external sorting is required. While it uses more memory than in-place sorting algorithms, its predictable performance makes it a go-to choice for many scenarios. The Python implementation provided is straightforward and can be easily adapted for different use cases.
