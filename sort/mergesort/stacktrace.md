# Stack Trace of Merge Sort

The `merge_sort` function recursively divides the array, and the `merge` function combines sorted subarrays. Since the code uses slicing, new lists are created, but we’ll focus on the stack frames for function calls and their local variables. The stack memory includes frames for `merge_sort` and `merge`, with local variables like `arr`, `mid`, `left`, `right`, `result`, `i`, and `j`.

---

### Step-by-Step Stack Trace for merge_sort([4, 2, 1, 3])

Below is the table tracking the stack memory for sorting the array `[4, 2, 1, 3]`. Each time step corresponds to a significant action (function call, return, or merge). The stack frames are listed from top (most recent) to bottom (initial call).

<table border="1" cellpadding="4" cellspacing="0">
  <tr>
    <th>Time Step</th>
    <th>Stack Frames (Top to Bottom)</th>
    <th>Action</th>
  </tr>
  <tr>
    <td>T0</td>
    <td>merge_sort([4, 2, 1, 3])</td>
    <td>Initial call</td>
  </tr>
  <tr>
    <td>T1</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])
    </td>
    <td>Call merge_sort([4, 2])</td>
  </tr>
  <tr>
    <td>T2</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])<br>
      merge_sort([4])
    </td>
    <td>Call merge_sort([4])</td>
  </tr>
  <tr>
    <td>T3</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])
    </td>
    <td>Return [4], unwind</td>
  </tr>
  <tr>
    <td>T4</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])<br>
      merge_sort([2])
    </td>
    <td>Call merge_sort([2])</td>
  </tr>
  <tr>
    <td>T5</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])
    </td>
    <td>Return [2], unwind</td>
  </tr>
  <tr>
    <td>T6</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([4, 2])<br>
      merge([4], [2])
    </td>
    <td>Call merge([4], [2])</td>
  </tr>
  <tr>
    <td>T7</td>
    <td>
      merge_sort([4, 2, 1, 3])
    </td>
    <td>Return [2, 4], unwind</td>
  </tr>
  <tr>
    <td>T8</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])
    </td>
    <td>Call merge_sort([1, 3])</td>
  </tr>
  <tr>
    <td>T9</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])<br>
      merge_sort([1])
    </td>
    <td>Call merge_sort([1])</td>
  </tr>
  <tr>
    <td>T10</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])
    </td>
    <td>Return [1], unwind</td>
  </tr>
  <tr>
    <td>T11</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])<br>
      merge_sort([3])
    </td>
    <td>Call merge_sort([3])</td>
  </tr>
  <tr>
    <td>T12</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])
    </td>
    <td>Return [3], unwind</td>
  </tr>
  <tr>
    <td>T13</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge_sort([1, 3])<br>
      merge([1], [3])
    </td>
    <td>Call merge([1], [3])</td>
  </tr>
  <tr>
    <td>T14</td>
    <td>
      merge_sort([4, 2, 1, 3])
    </td>
    <td>Return [1, 3], unwind</td>
  </tr>
  <tr>
    <td>T15</td>
    <td>
      merge_sort([4, 2, 1, 3])<br>
      merge([2, 4], [1, 3])
    </td>
    <td>Call merge([2, 4], [1, 3])</td>
  </tr>
  <tr>
    <td>T16</td>
    <td>
      Return [1, 2, 3, 4]
    </td>
    <td>Final result</td>
  </tr>
</table>

---

### Explanation of the Table

#### Key Points
- **Stack Frames**: Each frame represents a call to `merge_sort` or `merge`, with local variables (`arr`, `mid`, `left`, `right` for `merge_sort`; `left`, `right`, `result`, `i`, `j` for `merge`). The frames are listed top-to-bottom, with the most recent call at the top.
- **Actions**:
  - **Call**: A new recursive call to `merge_sort` or a call to `merge`, adding a frame to the stack.
  - **Return**: The function returns, popping its frame. For `merge_sort`, it returns the sorted subarray; for `merge`, it returns the merged result.
  - **Unwind**: Returning from a function reduces the stack depth.
- **Stack Depth**: 
    - <text style="color:lightblue">The maximum stack depth is 3 frames (e.g., T2: `merge_sort([4, 2, 1, 3])` → `merge_sort([4, 2])` → `merge_sort([4])`), corresponding to the recursion depth of **_log n = log 4 = 2_** plus the initial call.</text>
- **Memory Usage**:
  - Each `merge_sort` frame stores a reference to the input list `arr` and temporary lists `left` and `right` (due to slicing).
  - Each `merge` frame stores references to `left`, `right`, and a new `result` list, plus indices `i` and `j`.
  - Slicing creates new lists, increasing memory usage compared to the index-based approach from your earlier code.

#### Detailed Walkthrough
- **T0–T1**: Start with `merge_sort([4, 2, 1, 3])`, split into `left = [4, 2]` and `right = [1, 3]`, and call `merge_sort([4, 2])`.
- **T2–T5**: Process `merge_sort([4, 2])`, splitting into `[4]` and `[2]`. Each single-element array returns immediately (base case). The stack peaks at T2.
- **T6**: Call `merge([4], [2])`, which creates `[2, 4]`.
- **T7**: Return `[2, 4]` to `merge_sort([4, 2])`, which unwinds to the initial call.
- **T8–T12**: Process `merge_sort([1, 3])`, splitting into `[1]` and `[3]`, each returning immediately.
- **T13**: Call `merge([1], [3])`, creating `[1, 3]`.
- **T14**: Return `[1, 3]` to the initial call.
- **T15**: Call `merge([2, 4], [1, 3])`, producing the final sorted array `[1, 2, 3, 4]`.
- **T16**: Return the final result, stack is empty.


---

### Notes
- The table assumes Python’s standard recursion behavior, where each function call creates a new stack frame. In practice, the temporary lists (`left`, `right`, `result`) dominate memory usage in this slicing-based implementation.

- Compared to the index-based Merge Sort from your earlier request, this version uses more memory due to slicing but has a similar stack depth (`O(log n)`).

 - If you’d like a table for the index-based version or a different input array, let me know!