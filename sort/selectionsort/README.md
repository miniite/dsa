
# Understanding Selection Sort in Python

## Introduction
Selection Sort is a simple comparison-based sorting algorithm. It works by repeatedly finding the minimum element from the unsorted portion of the array and placing it at the beginning. This process continues until the entire array is sorted. While not the most efficient for large datasets, its simplicity makes it a great learning tool for understanding sorting algorithms.

## How Selection Sort Works
1. **Initialization**: Start with the entire array as the unsorted portion.
2. **Find Minimum**: Iterate through the unsorted portion to find the smallest element.
3. **Swap**: Swap the smallest element with the first element of the unsorted portion.
4. **Reduce Unsorted Portion**: Move the boundary of the sorted portion one element forward.
5. **Repeat**: Repeat steps 2–4 until the entire array is sorted.

The algorithm divides the array into two parts: a sorted subarray and an unsorted subarray. With each iteration, the sorted subarray grows, and the unsorted subarray shrinks.

## Python Implementation
Below is a Python implementation of the Selection Sort algorithm:

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

```python
# Example usage
if __name__ == "__main__":
    # Test array
    array = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", array)
    sorted_array = selection_sort(array)
    print("Sorted array:", sorted_array)
```

### Explanation of the Code
- **Function Definition**: `selection_sort(arr)` takes an array as input.
- **Outer Loop**: Iterates through each element of the array (`i` from 0 to `n-1`).
- **Inner Loop**: Finds the index of the minimum element in the unsorted portion (`j` from `i+1` to `n-1`).
- **Swap**: Swaps the minimum element with the first element of the unsorted portion.
- **Return**: Returns the sorted array.
- **Example Output**:
  ```
  Original array: [64, 34, 25, 12, 22, 11, 90]
  Sorted array: [11, 12, 22, 25, 34, 64, 90]
  ```

## Time and Space Complexity
- **Time Complexity**:
  - Best Case: O(n²) – when the array is already sorted.
  - Average Case: O(n²) – due to the nested loops.
  - Worst Case: O(n²) – when the array is sorted in reverse order.
- **Space Complexity**: O(1) – Selection Sort is an in-place sorting algorithm, requiring no extra space beyond a few variables.

## Advantages
- Simple to understand and implement.
- In-place sorting (no additional memory required).
- Performs well for small datasets or arrays with a small number of elements.

## Disadvantages
- Inefficient for large datasets due to O(n²) time complexity.
- Not adaptive; it doesn’t take advantage of existing order in the array.
- Outperformed by more advanced algorithms like Quick Sort or Merge Sort for larger arrays.

## When to Use Selection Sort
- When the dataset is small (e.g., fewer than 50 elements).
- When memory usage is a concern, as it requires no extra space.
- For educational purposes to understand sorting concepts.

## Conclusion
Selection Sort is a straightforward algorithm that’s easy to implement but not suitable for large datasets due to its quadratic time complexity. In Python, its implementation is concise and readable, making it a great starting point for beginners learning sorting algorithms. For larger or more complex sorting tasks, consider using built-in functions like `sorted()` or more efficient algorithms like Quick Sort or Merge Sort.
