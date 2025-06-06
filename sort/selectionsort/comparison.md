
# Selection Sort: Comparison of Implementations

## Comparison of Selection Sort Without Inbuilt Methods vs. With Inbuilt Methods

The following table compares the two implementations of Selection Sort in Python: one using a traditional approach without inbuilt methods and another using Python’s inbuilt `min()` and `index()` methods.


<table border="1" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <thead>
    <tr>
      <th style="padding: 10px; text-align: left;">Aspect</th>
      <th style="padding: 10px; text-align: left;">Without Inbuilt Methods</th>
      <th style="padding: 10px; text-align: left;">With Inbuilt Methods</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px;"><strong>Code</strong></td>
      <td style="padding: 10px;">
        <pre style="margin: 0; padding: 10px; border-radius: 5px;">
def selection_sort(lst):
    for pass_no in range(len(lst)):
        min_idx = pass_no
        for j in range(pass_no + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[pass_no], lst[min_idx] = lst[min_idx], lst[pass_no]
    return lst
        </pre>
      </td>
      <td style="padding: 10px;">
        <pre style="margin: 0; padding: 10px; border-radius: 5px;">
<code>
def selection_sort(lst):
    for pass_no in range(len(lst)):
        min_item = min(lst[pass_no:])
        idx = lst.index(min_item, pass_no)
        lst[pass_no], lst[idx] = lst[idx], lst[pass_no]
    return lst
</code>
        </pre>
      </td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Code Structure</strong></td>
      <td style="padding: 10px;">Uses nested loops to manually find the minimum element and its index in the unsorted portion.</td>
      <td style="padding: 10px;">Uses <code>min()</code> to find the minimum and <code>index()</code> to locate its position in the unsorted portion.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Readability</strong></td>
      <td style="padding: 10px;">More verbose due to explicit comparison logic in the inner loop.</td>
      <td style="padding: 10px;">More concise and readable due to Python’s inbuilt <code>min()</code> and <code>index()</code> methods.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Efficiency (Comparisons)</strong></td>
      <td style="padding: 10px;"> <u><i>Single pass</i></u> per iteration to find the minimum and its index, minimizing comparisons.</td>
      <td style="padding: 10px;"><u><i>Two passes</u></i> per iteration (<code>min()</code> and <code>index()</code>), doubling the comparisons.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Time Complexity</strong></td>
      <td style="padding: 10px;">O(n²) for best, average, and worst cases (single scan per pass).</td>
      <td style="padding: 10px;">O(n²) for best, average, and worst cases (two scans per pass).</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Space Complexity</strong></td>
      <td style="padding: 10px;">O(1), in-place with minimal extra variables (<code>min_idx</code>).</td>
      <td style="padding: 10px;">O(1), in-place with minimal extra variables (<code>min_item</code>, <code>idx</code>).</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Handling Duplicates</strong></td>
      <td style="padding: 10px;">Correctly handles duplicates by tracking the index of the first minimum element.</td>
      <td style="padding: 10px;">Correctly handles duplicates using <code>index()</code> with a start index to avoid earlier duplicates.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Code Length</strong></td>
      <td style="padding: 10px;">Longer due to explicit loop for finding the minimum index.</td>
      <td style="padding: 10px;">Shorter due to leveraging inbuilt methods.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Use Case</strong></td>
      <td style="padding: 10px;">Preferred for performance in large lists or when minimizing comparisons is critical.</td>
      <td style="padding: 10px;">Preferred for quick implementation, readability, or small lists where clarity is prioritized.</td>
    </tr>
  </tbody>
</table>





## Line-by-Line Code Comparison

Below is a line-by-line comparison of the two Selection Sort implementations to highlight how each line contributes to the algorithm.

| **Line** | **Without Inbuilt Methods**                                                                 | **With Inbuilt Methods**                                                                 | **Comparison**                                                                 |
|----------|---------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **1**    | `def selection_sort(lst):`                                                                  | `def selection_sort(lst):`                                                               | Identical function definition, taking a list as input.                          |
| **2**    | `    for pass_no in range(len(lst)):`                                                       | `    for pass_no in range(len(lst)):`                                                    | Identical outer loop, iterating over each position to build the sorted portion. |
| **3**    | `        min_idx = pass_no`                                                                 | `        min_item = min(lst[pass_no:])`                                                  | Without inbuilt: Initializes `min_idx` to track the minimum’s index. With inbuilt: Uses `min()` to find the smallest value in the unsorted portion. |
| **4**    | `        for j in range(pass_no + 1, len(lst)):`                                            | `        idx = lst.index(min_item, pass_no)`                                              | Without inbuilt: Inner loop to manually compare elements and update `min_idx`. With inbuilt: Uses `index()` to find the position of `min_item` starting from `pass_no`. |
| **5**    | `            if lst[j] < lst[min_idx]:`                                                     |                                                                                          | Without inbuilt: Compares elements to find the smallest, updating `min_idx`. With inbuilt: No equivalent line, as `index()` handles this. |
| **6**    | `                min_idx = j`                                                               |                                                                                          | Without inbuilt: Updates `min_idx` if a smaller element is found. With inbuilt: No equivalent, as `index()` returns the position directly. |
| **7**    | `        lst[pass_no], lst[min_idx] = lst[min_idx], lst[pass_no]`                           | `        lst[pass_no], lst[idx] = lst[idx], lst[pass_no]`                                | Identical swap operation, placing the minimum element at the start of the unsorted portion. |
| **8**    | `    return lst`                                                                            | `    return lst`                                                                         | Identical return statement, providing the sorted list.                          |


<br>

## Time Complexity Comparison

<table border="1" style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
  <thead>
    <tr>
      <th style="padding: 10px; text-align: left;">Aspect</th>
      <th style="padding: 10px; text-align: left;">Traditional (Inner Loop)</th>
      <th style="padding: 10px; text-align: left;">Inbuilt Methods (min() and index())</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 10px;"><strong>Inner Loop Behavior</strong></td>
      <td style="padding: 10px;">For each pass <code>pass_no</code>, the inner loop iterates from <code>pass_no + 1</code> to <code>len(lst) - 1</code>, comparing each element <code>lst[j]</code> with the current minimum <code>lst[min_idx]</code>.</td>
      <td style="padding: 10px;">Two operations per pass: <code>min(lst[pass_no:])</code> iterates over the unsorted portion (<code>n - pass_no</code> elements) to find the smallest value. <code>lst.index(min_item, pass_no)</code> iterates from <code>pass_no</code> to find the first occurrence of <code>min_item</code>.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Comparisons per Pass</strong></td>
      <td style="padding: 10px;">For pass <code>pass_no</code>, performs <code>n - pass_no - 1</code> comparisons.</td>
      <td style="padding: 10px;">Approximately <code>2(n - pass_no)</code> comparisons: <code>n - pass_no - 1</code> for <code>min()</code> and up to <code>n - pass_no</code> for <code>index()</code>.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Comparisons per Pass (Detailed)</strong></td>
      <td style="padding: 10px;">
        <ul style="margin: 0; padding-left: 20px;">
          <li>First pass: <code>n - 1</code> comparisons</li>
          <li>Second pass: <code>n - 2</code> comparisons</li>
          <li>...</li>
          <li>Last pass: 0 comparisons</li>
        </ul>
      </td>
      <td style="padding: 10px;">
        <ul style="margin: 0; padding-left: 20px;">
          <li>First pass: ~<code>2(n - 1)</code> comparisons</li>
          <li>Second pass: ~<code>2(n - 2)</code> comparisons</li>
          <li>...</li>
          <li>Last pass: ~<code>2(1)</code> comparisons</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Total Comparisons</strong></td>
      <td style="padding: 10px;"><code>(n-1) + (n-2) + ... + 1 = n(n-1)/2 ≈ n²/2</code></td>
      <td style="padding: 10px;"><code>2 * [(n-1) + (n-2) + ... + 1] = 2 * n(n-1)/2 ≈ n²</code></td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Number of Scans</strong></td>
      <td style="padding: 10px;">Single scan: The inner loop finds both the minimum value and its index in one pass through the unsorted portion.</td>
      <td style="padding: 10px;">Two scans: Each pass involves two separate iterations over the unsorted portion: one for <code>min()</code> and one for <code>index()</code>.</td>
    </tr>
    <tr>
      <td style="padding: 10px;"><strong>Constant Factor</strong></td>
      <td style="padding: 10px;">Lower constant factor (~<code>n²/2</code> comparisons).</td>
      <td style="padding: 10px;">Higher constant factor (~<code>n²</code> comparisons) due to additional iterations from two scans.</td>
    </tr>
  </tbody>
</table>



## Key Observations
- **Functionality**: Both implementations correctly perform Selection Sort, maintaining the in-place sorting and O(n²) time complexity.
- **Approach**: The inbuilt method version sacrifices some efficiency (due to dual scans) for brevity and readability, while the traditional version optimizes comparisons at the cost of more verbose code.
- **Duplicates**: Both handle duplicates correctly, with the inbuilt version using the `index()` start parameter to ensure the correct minimum is selected.
