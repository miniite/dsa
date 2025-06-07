Examples for Selection Sort

## Example 1: Sorting a Small List with No Duplicates
**Input List**: `[64, 34, 25, 12]` (n = 4)


<table>
<tr>
<th> 
        
### Traditional (Inner Loop) Implementation
</th>
<th>

### Inbuilt Methods Implementation
</th>
</tr>
<tr>
<td>
        
- **Pass 1 (pass_no = 0)**:
  - Unsorted portion: `[64, 34, 25, 12]`
  - Initialize `min_idx = 0` (points to `64`)
  - Inner loop (`j = 1 to 3`):
    - `j = 1`:
      - Compare `lst[1] = 34` with `lst[min_idx] = 64`. `34 < 64`
      - Update `min_idx = 1`. (1 comparison)
    - `j = 2`:
      - Compare `lst[2] = 25` with `lst[min_idx] = 34`. `25 < 34`
      - Update `min_idx = 2`. (1 comparison)
    - `j = 3`:
      - Compare `lst[3] = 12` with `lst[min_idx] = 25`. `12 < 25`
      - Update `min_idx = 3`. (1 comparison)
  - Total comparisons: 3
  - Swap: `lst[0] = 64` with `lst[3] = 12`. List: `[12, 34, 25, 64]`

</td>
<td>


- **Pass 1 (pass_no = 0)**:
  - Unsorted portion: `[64, 34, 25, 12]`
  - `min_item = min([64, 34, 25, 12])`:
    - Compare `64` vs. `34`: `34` is smaller. (1 comparison)
    - Compare `34` vs. `25`: `25` is smaller. (1 comparison)
    - Compare `25` vs. `12`: `12` is smaller. (1 comparison)
    - Result: `min_item = 12`. Comparisons: 3
  - `idx = lst.index(12, 0)`:
    - Check `lst[0] = 64`: Not 12
    - Check `lst[1] = 34`: Not 12
    - Check `lst[2] = 25`: Not 12
    - Check `lst[3] = 12`: Found
    - Result: `idx = 3`. Comparisons: ~3 (comparing each element to `12`)
  - Total comparisons: ~3 (min) + ~3 (index) = ~6
  - Swap: `lst[0] = 64` with `lst[3] = 12`. List: `[12, 34, 25, 64]`



</td>
</tr>

<tr>
<td>

- **Pass 2 (pass_no = 1)**:
  - Unsorted portion: `[34, 25, 64]`
  - Initialize `min_idx = 1` (points to `34`)
  - Inner loop (`j = 2 to 3`):
    - `j = 2`:
      - Compare `lst[2] = 25` with `lst[min_idx] = 34`. `25 < 34`
      - Update `min_idx = 2`. (1 comparison)
    - `j = 3`:
      - Compare `lst[3] = 64` with `lst[min_idx] = 25`. `64 > 25`
      - No update. (1 comparison)
  - Total comparisons: 2
  - Swap: `lst[1] = 34` with `lst[2] = 25`. List: `[12, 25, 34, 64]`
</td>
<td>

- **Pass 2 (pass_no = 1)**:
  - Unsorted portion: `[34, 25, 64]`
  - `min_item = min([34, 25, 64])`:
    - Compare `34` vs. `25`: `25` is smaller. (1 comparison)
    - Compare `25` vs. `64`: `25` is smaller. (1 comparison)
    - Result: `min_item = 25`. Comparisons: 2
  - `idx = lst.index(25, 1)`:
    - Check `lst[1] = 34`: Not 25
    - Check `lst[2] = 25`: Found
    - Result: `idx = 2`. Comparisons: ~1 (one non-match comparison)
  - Total comparisons: ~2 (min) + ~1 (index) = ~3
  - Swap: `lst[1] = 34` with `lst[2] = 25`. List: `[12, 25, 34, 64]`
</td>
</tr>

<tr>
<td>

- **Pass 3 (pass_no = 2)**:
  - Unsorted portion: `[34, 64]`
  - Initialize `min_idx = 2` (points to `34`)
  - Inner loop (`j = 3 to 3`):
    - `j = 3`:
      - Compare `lst[3] = 64` with `lst[min_idx] = 34`. `64 > 34`
      - No update. (1 comparison)
  - Total comparisons: 1
  - Swap: None (same element). List: `[12, 25, 34, 64]`
</td>
<td>

- **Pass 3 (pass_no = 2)**:
  - Unsorted portion: `[34, 64]`
  - `min_item = min([34, 64])`:
    - Compare `34` vs. `64`: `34` is smaller. (1 comparison)
    - Result: `min_item = 34`. Comparisons: 1
  - `idx = lst.index(34, 2)`:
    - Check `lst[2] = 34`: Found
    - Result: `idx = 2`. Comparisons: ~0 (immediate match)
  - Total comparisons: ~1 (min) + ~0 (index) = ~1
  - Swap: None (same element). List: `[12, 25, 34, 64]`
</td>
</tr>

<tr>
<td>

- **Pass 4 (pass_no = 3)**:
  - Unsorted portion: `[64]`
  - No inner loop (`j = 4 to 3` is empty)
  - Total comparisons: 0
  - Swap: None. List: `[12, 25, 34, 64]`
</td>
<td>

- **Pass 4 (pass_no = 3)**:
  - Unsorted portion: `[64]`
  - `min_item = min([64])`:
    - No comparisons (single element). Comparisons: 0
  - `idx = lst.index(64, 3)`:
    - Check `lst[3] = 64`: Found
    - Result: `idx = 3`. Comparisons: ~0 (immediate match)
  - Total comparisons: ~0 (min) + ~0 (index) = ~0
  - Swap: None. List: `[12, 25, 34, 64]`
</td>
</tr>



<tr>
<td>

#### Total Comparisons
- Pass 1: 3 comparisons
- Pass 2: 2 comparisons
- Pass 3: 1 comparison
- Pass 4: 0 comparisons
- **Total**: `3 + 2 + 1 + 0 = 6` comparisons
- **Formula**: `n(n-1)/2 = 4*3/2 = 6`
</td>
<td>

#### Total Comparisons
- Pass 1: ~6 comparisons
- Pass 2: ~3 comparisons
- Pass 3: ~1 comparison
- Pass 4: ~0 comparisons
- **Total**: `6 + 3 + 1 + 0 = ~10` comparisons
- **Formula**: Approximately `2 * n(n-1)/2 = 2 * 4*3/2 = 12`, slightly less due to early termination in `index()`.
</td>
</tr>
</table>




### Comparison for Example 1
- **Traditional**: 6 comparisons (single scan per pass, `n(n-1)/2 = 6`).
- **Inbuilt**: ~10 comparisons (two scans per pass, ~`2 * n(n-1)/2 = 12`, slightly reduced due to `index()` stopping early).
- **Constant Factor**: Inbuilt method performs roughly 1.67x more comparisons (10/6), reflecting the higher constant factor due to two scans (`min()` and `index()`) vs. one scan.

---

## Example 2: Sorting a List with Duplicates
**Input List**: `[64, 25, 25, 12]` (n = 4)




<table>
<tr>
<th>

### Traditional (Inner Loop) Implementation
</th>
<th>

### Inbuilt Methods Implementation
</th>
</tr>

<tr>
<td>

- **Pass 1 (pass_no = 0)**:
  - Unsorted portion: `[64, 25, 25, 12]`
  - Initialize `min_idx = 0` (points to `64`)
  - Inner loop (`j = 1 to 3`):
    - `j = 1`:
      - Compare `lst[1] = 25` with `lst[min_idx] = 64`. `25 < 64`
      - Update `min_idx = 1`. (1 comparison)
    - `j = 2`:
      - Compare `lst[2] = 25` with `lst[min_idx] = 25`. `25 = 25`
      - No update (keeps first occurrence). (1 comparison)
    - `j = 3`:
      - Compare `lst[3] = 12` with `lst[min_idx] = 25`. `12 < 25`
      - Update `min_idx = 3`. (1 comparison)
  - Total comparisons: 3
  - Swap: `lst[0] = 64` with `lst[3] = 12`. List: `[12, 25, 25, 64]`
</td>
<td>

- **Pass 1 (pass_no = 0)**:
  - Unsorted portion: `[64, 25, 25, 12]`
  - `min_item = min([64, 25, 25, 12])`:
    - Compare `64` vs. `25`: `25` is smaller. (1 comparison)
    - Compare `25` vs. `25`: `25` is equal. (1 comparison)
    - Compare `25` vs. `12`: `12` is smaller. (1 comparison)
    - Result: `min_item = 12`. Comparisons: 3
  - `idx = lst.index(12, 0)`:
    - Check `lst[0] = 64`: Not `12`. (1 comparison)
    - Check `lst[1] = 25`: Not `12`. (1 comparison)
    - Check `lst[2] = 25`: Not `12`. (1 comparison)
    - Check `lst[3] = 12`: Found. (0 comparisons)
    - Result: `idx = 3`. Comparisons: ~3
  - Total comparisons: ~3 (min) + ~3 (index) = ~6
  - Swap: `lst[0] = 64` with `lst[3] = 12`. List: `[12, 25, 25, 64]`
</td>
</tr>

<tr>
<td>

- **Pass 2 (pass_no = 1)**:
  - Unsorted portion: `[25, 25, 64]`
  - Initialize `min_idx = 1` (points to `25`)
  - Inner loop (`j = 2 to 3`):
    - `j = 2`:
      - Compare `lst[2] = 25` with `lst[min_idx] = 25`. `25 = 25`
      - No update (keeps first occurrence). (1 comparison)
    - `j = 3`:
      - Compare `lst[3] = 64` with `lst[min_idx] = 25`. `64 > 25`
      - No update. (1 comparison)
  - Total comparisons: 2
  - Swap: None (same element). List: `[12, 25, 25, 64]`
</td>
<td>

- **Pass 2 (pass_no = 1)**:
  - Unsorted portion: `[25, 25, 64]`
  - `min_item = min([25, 25, 64])`:
    - Compare `25` vs. `25`: `25` is equal. (1 comparison)
    - Compare `25` vs. `64`: `25` is smaller. (1 comparison)
    - Result: `min_item = 25`. Comparisons: 2
  - `idx = lst.index(25, 1)`:
    - Check `lst[1] = 25`: Found. (0 comparisons)
    - Result: `idx = 1`. Comparisons: ~0
  - Total comparisons: ~2 (min) + ~0 (index) = ~2
  - Swap: None (same element). List: `[12, 25, 25, 64]`
</td>
</tr>

<tr>
<td>

- **Pass 3 (pass_no = 2)**:
  - Unsorted portion: `[25, 64]`
  - Initialize `min_idx = 2` (points to `25`)
  - Inner loop (`j = 3 to 3`):
    - `j = 3`:
      - Compare `lst[3] = 64` with `lst[min_idx] = 25`. `64 > 25`
      - No update. (1 comparison)
  - Total comparisons: 1
  - Swap: None (same element). List: `[12, 25, 25, 64]`
</td>
<td>

- **Pass 3 (pass_no = 2)**:
  - Unsorted portion: `[25, 64]`
  - `min_item = min([25, 64])`:
    - Compare `25` vs. `64`: `25` is smaller. (1 comparison)
    - Result: `min_item = 25`. Comparisons: 1
  - `idx = lst.index(25, 2)`:
    - Check `lst[2] = 25`: Found. (0 comparisons)
    - Result: `idx = 2`. Comparisons: ~0
  - Total comparisons: ~1 (min) + ~0 (index) = ~1
  - Swap: None (same element). List: `[12, 25, 25, 64]`
</td>
</tr>

<tr>
<td>

- **Pass 4 (pass_no = 3)**:
  - Unsorted portion: `[64]`
  - No inner loop (`j = 4 to 3` is empty)
  - Total comparisons: 0
  - Swap: None. List: `[12, 25, 25, 64]`
</td>
<td>

- **Pass 4 (pass_no = 3)**:
  - Unsorted portion: `[64]`
  - `min_item = min([64])`:
    - No comparisons (single element). Comparisons: 0
  - `idx = lst.index(64, 3)`:
    - Check `lst[3] = 64`: Found. (0 comparisons)
    - Result: `idx = 3`. Comparisons: ~0
  - Total comparisons: ~0 (min) + ~0 (index) = ~0
  - Swap: None. List: `[12, 25, 25, 64]`
</td>
</tr>



<tr>
<td>

#### Total Comparisons
- Pass 1: 3 comparisons
- Pass 2: 2 comparisons
- Pass 3: 1 comparison
- Pass 4: 0 comparisons
- **Total**: `3 + 2 + 1 + 0 = 6` comparisons
- **Formula**: `n(n-1)/2 = 4*3/2 = 6`
</td>
<td>

#### Total Comparisons
- Pass 1: ~6 comparisons
- Pass 2: ~2 comparisons
- Pass 3: ~1 comparison
- Pass 4: ~0 comparisons
- **Total**: `6 + 2 + 1 + 0 = ~9` comparisons
- **Formula**: Approximately `2 * n(n-1)/2 = 2 * 4*3/2 = 12`, slightly less due to early termination in `index()` with duplicates.
</td>
</tr>
</table>



### Comparison for Example
- **Traditional**: 6 comparisons (`n(n-1)/2 = 6`).
- **Inbuilt**: ~9 comparisons (~`2 * n(n-1)/2 = 12`, reduced due to duplicates causing `index()` to stop early).
- **Constant Factor**: Inbuilt method performs ~1.5x more comparisons (9/6), slightly less than a non-duplicate case because duplicates allow `index()` to terminate early when finding the first occurrence.




## Key Insights
1. **Constant Factor Difference**:
   - **Traditional**: Performs `n(n-1)/2 ≈ n²/2` comparisons due to a single scan per pass to find both the minimum and its index.
   - **Inbuilt**: Performs up to `2 * n(n-1)/2 ≈ n²` comparisons due to two scans (`min()` and `index()`). In practice, the number is slightly less because `index()` may stop early when it finds the minimum, especially with duplicates.
   - The inbuilt method’s constant factor is roughly double (e.g., 1.67x in Example 1, 1.5x in Example 2) due to the additional scan by `index()`.

2. **Impact of Duplicates**:
   - In Example 2, duplicates (`25, 25`) reduce the comparisons in the inbuilt method because `index()` stops at the first occurrence of the minimum (e.g., at `lst[1] = 25` in Pass 2). This lowers the constant factor slightly compared to the worst-case estimate of `2 * n(n-1)/2`.

3. **Asymptotic Complexity**:
   - Both methods are O(n²) because the constant factor (1 vs. ~2) is ignored in Big-O notation.
   - The inbuilt method’s higher constant factor makes it slower in practice, especially for larger lists, but the difference is less pronounced with duplicates or early terminations.

4. **Practical Performance**:
   - For `n = 4`, the traditional method consistently uses 6 comparisons, while the inbuilt method uses 9–10 comparisons, depending on the data.
   - For larger `n`, the inbuilt method’s doubled comparisons (e.g., ~2n²/2 vs. n²/2) make it noticeably slower, though still within O(n²).

---

## Conclusion
The traditional implementation is more efficient, requiring `n(n-1)/2` comparisons with a single scan per pass. The inbuilt method, using `min()` and `index()`, requires up to `2 * n(n-1)/2` comparisons due to two scans, resulting in a higher constant factor (roughly 1.5x–2x more comparisons). Duplicates can slightly reduce the inbuilt method’s comparisons by allowing `index()` to terminate early, but the constant factor remains higher. Both methods maintain O(n²) time complexity, but the inbuilt method sacrifices performance for code simplicity.