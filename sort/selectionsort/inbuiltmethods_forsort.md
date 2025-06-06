
# Selection Sort in Python Using Inbuilt Methods

## Introduction
Selection Sort is a simple, in-place sorting algorithm that works by repeatedly finding the minimum element in the unsorted portion of an array and swapping it with the first element of that portion. This article focuses on a specific Python implementation of Selection Sort that uses inbuilt methods like `min()` and `index()` to locate the minimum element, highlighting how it adheres to the core principles of the algorithm.

## The Code
Below is the Python implementation of Selection Sort using inbuilt methods:

```python
def selection_sort(lst):
    for pass_no in range(len(lst)):
        min_item = min(lst[pass_no:])
        idx = lst.index(min_item, pass_no)  # Find first occurrence of min_item starting from pass_no
        lst[pass_no], lst[idx] = lst[idx], lst[pass_no]
    return lst
```

## How the Code Follows Selection Sort
Selection Sort operates by dividing the list into a sorted and an unsorted portion, iteratively shrinking the unsorted portion by moving the smallest element to the sorted portion. Let’s break down how this code implements that logic using inbuilt methods:

1. **Outer Loop (Iterating Over Passes)**:
   - The loop `for pass_no in range(len(lst))` iterates through each position in the list, representing the start of the unsorted portion. 
   - Each iteration (`pass_no`) corresponds to one pass of Selection Sort, where the goal is to place the smallest element from the unsorted portion at index `pass_no`.

   - This aligns with Selection Sort’s principle of building the sorted portion one element at a time.

2. **Finding the Minimum Element**:
   - The line `min_item = min(lst[pass_no:])` uses Python’s inbuilt `min()` function to find the smallest element in the slice `lst[pass_no:]`, which represents the unsorted portion of the list (from index `pass_no` to the end).

   - This step directly implements the Selection Sort requirement of identifying the minimum element in the unsorted segment using an inbuilt method.

3. **Locating the Minimum Element’s Index**:
   - The line `idx = lst.index(min_item, pass_no)` uses the inbuilt `index()` method to find the index of the first occurrence of `min_item` in the list, starting the search from `pass_no`. 

   - The `pass_no` parameter ensures that only the unsorted portion is considered, avoiding earlier duplicates in the sorted portion.
   - This is crucial for correctness, as it ensures the algorithm selects the correct minimum element’s position in the unsorted segment, adhering to Selection Sort’s logic of selecting the smallest element’s index.

4. **Swapping Elements**:
   - The swap `lst[pass_no], lst[idx] = lst[idx], lst[pass_no]` exchanges the first element of the unsorted portion (`lst[pass_no]`) with the minimum element found (`lst[idx]`).
   
   - This step follows Selection Sort’s core mechanism of placing the smallest element at the beginning of the unsorted portion, effectively expanding the sorted portion.

5. **Returning the Sorted List**:
   - After all passes are complete, the list is fully sorted, and `return lst` provides the result. The in-place modification ensures no additional space is used, a hallmark of Selection Sort.

## Handling Duplicates
The use of `lst.index(min_item, pass_no)` is particularly effective for handling duplicates. By specifying the start index `pass_no`, the algorithm ensures it selects the first occurrence of the minimum value in the unsorted portion, preventing incorrect swaps with earlier duplicates in the sorted portion. For example:
```python
array = [64, 34, 25, 12, 25, 11, 90]
print(selection_sort(array))  # Output: [11, 12, 25, 25, 34, 64, 90]
```
This correctly places both `25` values in their sorted positions without confusion.

## Time and Space Complexity
- **Time Complexity**: 
    - O(n²) for best, average, and worst cases, as the algorithm always scans the unsorted portion to find the minimum and performs a constant-time swap each pass. 
    - The inbuilt `min()` and `index()` methods each iterate over the unsorted portion, contributing to the quadratic complexity.

- **Space Complexity**: 
    - O(1), as the sorting is in-place, requiring only a few variables (`min_item`, `idx`) regardless of input size. 
    - The slice `lst[pass_no:]` in Python creates a view, not a copy, so no significant extra memory is used.

## Alignment with Selection Sort Principles
This implementation adheres strictly to Selection Sort’s core principles:
- **In-Place Sorting**: The list is modified directly without requiring additional arrays.

- **Minimum Selection**: Each pass identifies the smallest element in the unsorted portion using inbuilt methods.
- **Incremental Sorting**: The sorted portion grows by one element per pass, with the unsorted portion shrinking accordingly.
- **Stability Consideration**: While this implementation is not stable (it may swap equal elements), Selection Sort is not inherently stable, and this code prioritizes simplicity and correctness.

## Advantages and Trade-offs
- **Advantages**:
  - The use of inbuilt `min()` and `index()` methods makes the code concise and readable, leveraging Python’s built-in functionality.

  - It handles duplicates correctly by using the start index in `index()`.
- **Trade-offs**:
  - The `min()` and `index()` calls both iterate over the unsorted portion, effectively doubling the comparisons compared to a traditional implementation that tracks the minimum index in a single loop. However, this doesn’t change the O(n²) Blasius, just the constant factor.

  - For very large lists, this approach may be slightly slower than the traditional method due to the dual iteration.

## Conclusion
This Selection Sort implementation using inbuilt methods is a concise and correct realization of the algorithm’s core idea: repeatedly select the minimum element from the unsorted portion and place it at the beginning. 

By leveraging Python’s `min()` and `index()` methods with a start index, it handles duplicates effectively and maintains the in-place, quadratic-time nature of Selection Sort. While slightly less efficient than the traditional approach due to extra iterations, its clarity makes it an excellent example for learning and understanding the algorithm.
