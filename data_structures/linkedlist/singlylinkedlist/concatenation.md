
# Concatenating Multiple Singly Linked Lists in Python

## Introduction
Concatenating multiple singly linked lists involves joining them end-to-end into a single linked list, preserving the order of nodes from each input list. This article presents iterative and recursive implementations as `@staticmethod` methods in the `LinkedList` class to concatenate a variable number of linked lists, using the standard `*args` convention for variable-length arguments. Each method includes code, brief logic, a comparison of complexities, and considerations for edge cases, building on the existing `LinkedList` and `Node` classes.

 

## Iterative Concatenation Implementation

### Code
```python
@staticmethod
def concatenate_iterative(*args):
    result = LinkedList()
    if not args:
        return result
    dummy = Node(0)
    current = dummy
    for lst in args:
        if lst.head:
            current.next = lst.head
            while current.next:
                current = current.next
    result.head = dummy.next
    return result
```

### Logic
- Create a new `LinkedList` for the result and a dummy node to simplify linking.
- If no lists are provided (`args` is empty), return an empty list.
- Iterate through each `LinkedList` in `args`, linking its head to the current tail.
- Traverse to the end of each list to update the tail pointer (`current`).
- Set `result.head` to `dummy.next`.

### Time Complexity
- **O(N)**: Traverses all \( N \) nodes across all lists to link them, where \( N \) is the total number of nodes.

### Space Complexity
- **O(1)**: Uses constant extra space (dummy and pointers), excluding the result list.

## Recursive Concatenation Implementation

### Code
```python
@staticmethod
def concatenate_recursive(*args):
    result = LinkedList()
    
    def concat_recursive(lists, index):
        if index >= len(lists):
            return None
        if lists[index].head:
            head = lists[index].head
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = concat_recursive(lists, index + 1)
            return head
        return concat_recursive(lists, index + 1)
    
    result.head = concat_recursive(args, 0)
    return result
```

### Logic
- Create a new `LinkedList` for the result.
- Define a recursive helper function `concat_recursive`:
  - Base case: If `index` exceeds the number of lists, return `None`.
  - If the current list has a head, traverse to its tail and link it to the head of the next list (recursively).
  - If the current list is empty, skip to the next list.
- Set `result.head` to the recursive result.

### Time Complexity
- **O(N)**: Traverses all \( N \) nodes to find tails and link lists, with recursive calls bounded by the number of lists.

### Space Complexity
- **O(L)**: Recursive call stack depth is at most \( L \), where \( L \) is the number of lists in `args`.

## Edge Cases
- **No Lists**: Both methods return an empty `LinkedList` when `*args` is empty.
- **Empty Lists**: Skipped during concatenation, contributing no nodes.
- **Single List**: Returns the list itself (iterative) or its head (recursive).
- **Multiple Lists**: Concatenates non-empty lists in order, preserving node sequence.

## Comparison

| Approach   | Time Complexity | Space Complexity | Advantages                     | Limitations                        |
|------------|-----------------|------------------|--------------------------------|------------------------------------|
| Iterative  | O(N)            | O(1)             | Memory-efficient, simple       | Slightly verbose traversal logic   |
| Recursive  | O(N)            | O(L)             | Elegant, handles variable args | Stack overflow risk for many lists |

- **Preference**: Iterative is preferred for its O(1) space complexity and robustness, especially for large lists or many input lists.

## Example Usage
```python
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(2)

list2 = LinkedList()
list2.insert_at_end(3)
list2.insert_at_end(4)

list3 = LinkedList()
list3.insert_at_end(5)

concatenated = LinkedList.concatenate_iterative(list1, list2, list3)
concatenated.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

concatenated = LinkedList.concatenate_recursive(list1, list2, list3)
concatenated.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None
```

## Conclusion
The `@staticmethod` implementations using `*args` efficiently concatenate multiple linked lists, with the iterative method preferred for its O(1) space complexity and simplicity. The recursive method is elegant but risks stack overflow for many lists due to O(L) space complexity. Both handle edge cases robustly and align with Python’s naming conventions, making them suitable for concatenating multiple linked lists in various applications.

