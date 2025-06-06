# Best practises in Bubble Sort 

### 1. Why We Use the `swapped` Flag
The `swapped` flag is an optimization in Bubble Sort to detect if the list is already sorted, allowing the algorithm to terminate early and avoid unnecessary passes. Here's a detailed explanation:

- **Purpose**: The `swapped` flag tracks whether any swaps occurred during a pass through the list. If no swaps are made in a pass, it means all adjacent elements are in the correct order, and thus the list is sorted. The algorithm can then exit early without completing the remaining passes.
- **How It Works**:
  - At the start of each pass (`passno`), `swapped` is set to `False`.
  - If a swap occurs in the inner loop (when `arr[i] > arr[i + 1]`), `swapped` is set to `True`.
  - After the inner loop, if `swapped` remains `False`, no elements were out of order, so the list is sorted, and the algorithm breaks out of the outer loop.
- **Benefit**: This optimization improves the best-case time complexity from O(n²) to O(n) when the list is already sorted or becomes sorted early. For example, in Example 2 (`[1, 2, 4, 3, 5, 6]`), the list was sorted after one pass, and the `swapped` flag allowed the algorithm to terminate after the second pass with no swaps.

#### What Happens If `swapped` Is Not Used?
Without the `swapped` flag, the algorithm will always perform all `n` passes, even if the list is sorted early, leading to unnecessary iterations:
- **Impact on Performance**:
  - **Best Case (Already Sorted)**: Without `swapped`, an already sorted list (e.g., `[1, 2, 3, 4, 5, 6]`) would still require `n` passes, each checking all pairs up to `n - passno - 1`. This results in O(n²) time complexity, as the algorithm doesn't recognize that no swaps are needed.
  - **Partially Sorted Lists**: In cases like [Example 2](example.md#example-2-sorting-1-2-4-3-5-6), where only one swap was needed, the algorithm would still perform all `n = 6` passes, wasting time on redundant comparisons.
- **Example 2 Without `swapped`**:
  - The array `[1, 2, 4, 3, 5, 6]` is sorted after Pass 1 (`[1, 2, 3, 4, 5, 6]`).
  - With `swapped`, the algorithm stops after Pass 2 (no swaps, `swapped = False`). Total comparisons: 5 (Pass 1) + 4 (Pass 2) = 9.
  - Without `swapped`, it would perform all 6 passes: 5 + 4 + 3 + 2 + 1 + 0 = 15 comparisons, increasing runtime unnecessarily.
- **Conclusion**: Removing the `swapped` flag eliminates the early termination optimization, making the algorithm less efficient, especially for nearly sorted or fully sorted lists. The worst-case time complexity (O(n²)) remains unchanged, but the best-case performance degrades from O(n) to O(n²).

### 2. Why the Inner Loop Uses `range(0, n - passno - 1)`
The inner loop `for i in range(0, n - passno - 1)` determines how many pairs of adjacent elements are compared in each pass. The expression `n - passno - 1` is used for the following reasons:

- **Purpose**: The inner loop compares adjacent elements `arr[i]` and `arr[i + 1]`. After each pass (`passno`), the largest `passno` elements are correctly sorted at the end of the array, so there's no need to compare those elements in subsequent passes.
- **Breakdown of `n - passno - 1`**:
  - `n`: The length of the array (e.g., 7 for Example 1).
  - `passno`: The number of completed passes, starting from 0. After `passno` passes, the last `passno` elements are sorted.
  - `- 1`: Since the loop compares `arr[i]` with `arr[i + 1]`, the index `i` must stop one position before the end of the unsorted portion to avoid accessing `arr[i + 1]` out of bounds.
- **Why It Works**:
  - In the first pass (`passno = 0`), the loop iterates from `i = 0` to `n - 1 - 1 = n - 1`, comparing all adjacent pairs up to the last pair (`arr[n-2]` and `arr[n-1]`).
  - In the second pass (`passno = 1`), the largest element is already at `arr[n-1]`, so the loop iterates from `i = 0` to `n - 1 - 1 = n - 2`, excluding the last element.
  - After `passno` passes, the last `passno` elements are sorted, so the loop only needs to cover indices `0` to `n - passno - 1`.
- **Example 1 Illustration**:
  - Array: `[64, 34, 25, 12, 22, 11, 90]`, `n = 7`.
  - Pass 1 (`passno = 0`): `range(0, 7 - 0 - 1) = range(0, 6)`. 
  
    - Compares pairs at indices `(0,1), (1,2), (2,3), (3,4), (4,5), (5,6)`. 
    - Largest element (90) ends up at index 6.
  - Pass 2 (`passno = 1`): `range(0, 7 - 1 - 1) = range(0, 5)`. 
    - Compares pairs up to index 4, since index 6 is sorted. 
    - Second largest (64) moves to index 5.
  - This continues, reducing the range by 1 each pass.
- **Why Not Just `n - 1`?**:
  - Using `range(0, n - 1)` for all passes would redundantly compare already sorted elements at the end, wasting computations. For example, after Pass 1, `arr[6]` (90) is sorted, so comparing `arr[5]` and `arr[6]` in Pass 2 is unnecessary.
- **Conclusion**: The `n - passno - 1` range ensures the inner loop only processes the unsorted portion of the array, making the algorithm more efficient by avoiding comparisons of elements already in their final positions.

### Summary
- **Swapped Flag**: Optimizes Bubble Sort by allowing early termination when no swaps occur, improving best-case performance to O(n). Without it, the algorithm always runs all `n` passes, leading to O(n²) even for sorted lists, as seen in Example 2 where it would perform 15 comparisons instead of 9.
- **Inner Loop Range (`n - passno - 1`)**: Limits comparisons to the unsorted portion of the array, excluding the last `passno` elements that are already sorted and accounting for the `i + 1` index to avoid out-of-bounds errors. This ensures efficiency by not rechecking sorted elements.

These mechanisms make the Bubble Sort implementation more efficient, especially for nearly sorted lists like Example 2, while maintaining correctness for unsorted lists like Example 1.