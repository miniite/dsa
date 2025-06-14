# Detailed Explanation of Singly Linked List Deletion Methods in Python

## Introduction
Deletion operations in a singly linked list remove nodes, adjusting references to maintain the list’s integrity. The provided Python implementation of a singly linked list includes four deletion methods: `delete_at_beginning`, `delete_at_end`, `delete_at_position`, and `delete_first_occurrence`. This document provides a comprehensive explanation of each method, detailing their purpose, logic, step-by-step execution, time complexity, edge cases, and practical examples. The explanation assumes familiarity with the linked list structure, where each node contains data and a reference to the next node, managed via a `head` pointer.

## 1. Delete at Beginning (`delete_at_beginning`)

### Purpose
The `delete_at_beginning` method removes the first node (head) of the singly linked list, updating the head to point to the next node. This operation is efficient as it requires no traversal.

### Code
```python
def delete_at_beginning(self):
    if self.head is None:
        print("List is empty")
        return
    self.head = self.head.next
```

### Logic
- Check if the list is empty (`head` is `None`). If so, report an error.
- Update the `head` to point to the next node, effectively removing the first node.

### Step-by-Step Process
1. **Check Empty List**: If `self.head` is `None`, print an error message and exit.
2. **Update Head**: Set `self.head` to `self.head.next`, bypassing the first node.

### Time Complexity
- **O(1)**: The operation involves constant-time steps (checking emptiness and updating the head), regardless of the list’s size.

### Edge Cases
- **Empty List**: No deletion occurs, and an error is reported.
- **Single-Node List**: The head becomes `None` after deletion, resulting in an empty list.
- **Multi-Node List**: The second node becomes the new head.

### Example
**Initial List**: `0 -> 1 -> 2 -> None` (head points to node with data 0)
- Call: `delete_at_beginning()`
- **Step 1**: Check `head` is not `None`.
- **Step 2**: Set `head` to `head.next` (node with 1).
- **Resulting List**: `1 -> 2 -> None`

### Illustration
```
Before: head -> [0|next] -> [1|next] -> [2|None]
After:  head -> [1|next] -> [2|None]
```

## 2. Delete at End (`delete_at_end`)

### Purpose
The `delete_at_end` method removes the last node of the singly linked list, requiring traversal to the second-to-last node to update its `next` reference to `None`.

### Code
```python
def delete_at_end(self):
    if self.head is None:
        print("List is empty")
        return
    if self.head.next is None:
        self.head = None
        return
    current = self.head
    while current.next.next:
        current = current.next
    current.next = None
```

### Logic
- Check if the list is empty (`head` is `None`). If so, report an error.
- Check if the list has one node (`head.next` is `None`). If so, set `head` to `None`.
- Traverse to the second-to-last node (where `current.next.next` is `None`) and set its `next` to `None`, removing the last node.

### Step-by-Step Process
1. **Check Empty List**: If `self.head` is `None`, print an error and exit.
2. **Check Single Node**: If `self.head.next` is `None`, set `self.head` to `None` and exit.
3. **Traverse to Second-to-Last**: Start at `head` and move until `current.next.next` is `None`.
4. **Remove Last Node**: Set `current.next` to `None`.

### Time Complexity
- **O(n)**: Traversal to the second-to-last node requires visiting up to `n-1` nodes, where `n` is the list’s length. Checks and reference updates are O(1).

### Edge Cases
- **Empty List**: No deletion occurs, and an error is reported.
- **Single-Node List**: The list becomes empty (`head` set to `None`).
- **Multi-Node List**: The last node is removed, and the second-to-last node’s `next` becomes `None`.

### Example
**Initial List**: `0 -> 1 -> 2 -> None` (head points to node with data 0)
- Call: `delete_at_end()`
- **Step 1**: Check `head` is not `None` and `head.next` is not `None`.
- **Step 2**: Traverse: Start at `0`, move to `1` (`1.next.next` is `None`).
- **Step 3**: Set `1.next` to `None`.
- **Resulting List**: `0 -> 1 -> None`

### Illustration
```
Before: head -> [0|next] -> [1|next] -> [2|None]
After:  head -> [0|next] -> [1|None]
```

## 3. Delete at Position (`delete_at_position`)

### Purpose
The `delete_at_position` method removes a node at a specified zero-based index, adjusting references to bypass the deleted node. This generalizes deletion at arbitrary positions.

### Code
```python
def delete_at_position(self, position):
    if self.head is None:
        print("List is empty")
        return
    if position < 0:
        print("Invalid position")
        return
    if position == 0:
        self.delete_at_beginning()
        return
    current = self.head
    for i in range(position - 1):
        if current is None:
            print("Position out of range")
            return
        current = current.next
    if current is None or current.next is None:
        print("Position out of range")
        return
    current.next = current.next.next
```

### Logic
- Check if the list is empty or if `position` is negative. If either, report an error.
- If `position` is 0, delegate to `delete_at_beginning`.
- Traverse to the node at index `position - 1` (the node before the one to delete).
- If traversal reaches `None` or the node at `position` doesn’t exist, report an error.
- Update the `next` reference of the node at `position - 1` to skip the node at `position`.

### Step-by-Step Process
1. **Check Empty List**: If `self.head` is `None`, print error and exit.
2. **Validate Position**: If `position < 0`, print error and exit.
3. **Handle Position 0**: If `position == 0`, call `delete_at_beginning` and exit.
4. **Traverse to Position**: Move `position - 1` steps from `head`. If `current` becomes `None`, the position is invalid.
5. **Check Validity**: If `current` or `current.next` is `None` after traversal, the position is out of range.
6. **Delete Node**: Set `current.next` to `current.next.next`, bypassing the node at `position`.

### Time Complexity
- **O(n)**: Traversal to `position - 1` may require up to `n-1` steps. Checks, delegation to `delete_at_beginning` (O(1)), and reference updates are O(1). For `position = 0`, it’s O(1).

### Edge Cases
- **Empty List**: No deletion occurs, and an error is reported.
- **Negative Position**: Invalid, triggers error message.
- **Position 0**: Handled by `delete_at_beginning`.
- **Position Equals Length**: Invalid, as no node exists at that index.
- **Position Beyond Length**: Invalid, triggers error message.
- **Valid Position in Middle**: Removes the node at the specified index.

### Example
**Initial List**: `0 -> 1 -> 1.5 -> 2 -> None` (head points to node with data 0)
- Call: `delete_at_position(2)`
- **Step 1**: Check `head` is not `None`, `position = 2` is non-negative, and not 0.
- **Step 2**: Traverse to `position - 1 = 1`: Start at `0`, move to `1`.
- **Step 3**: Check `current` (node with 1) and `current.next` (node with 1.5) are not `None`.
- **Step 4**: Set `current.next` to `current.next.next` (node with 2).
- **Resulting List**: `0 -> 1 -> 2 -> None`

### Illustration
```
Before: head -> [0|next] -> [1|next] -> [1.5|next] -> [2|None]
After:  head -> [0|next] -> [1|next] -> [2|None]
```

## 4. Delete First Occurrence (`delete_first_occurrence`)

### Purpose
The `delete_first_occurrence` method removes the first node containing a specified value, adjusting references to bypass it. This is useful for value-based deletion.

### Code
```python
def delete_first_occurrence(self, value):
    if self.head is None:
        print("List is empty")
        return
    if self.head.data == value:
        self.delete_at_beginning()
        return
    current = self.head
    while current.next and current.next.data != value:
        current = current.next
    if current.next is None:
        print("Value not found")
        return
    current.next = current.next.next
```

### Logic
- Check if the list is empty. If so, report an error.
- If the head node’s data matches `value`, delegate to `delete_at_beginning`.
- Traverse the list to find a node whose `next` node contains `value`.
- If no such node is found (`current.next` is `None`), report an error.
- Update `current.next` to skip the node with the matching value.

### Step-by-Step Process
1. **Check Empty List**: If `self.head` is `None`, print error and exit.
2. **Check Head**: If `self.head.data == value`, call `delete_at_beginning` and exit.
3. **Traverse to Match**: Move until `current.next.data == value` or `current.next` is `None`.
4. **Check Existence**: If `current.next` is `None`, the value wasn’t found; print error and exit.
5. **Delete Node**: Set `current.next` to `current.next.next`, bypassing the matching node.

### Time Complexity
- **O(n)**: Traversal to find the value may require visiting up to `n` nodes. Checks, delegation to `delete_at_beginning` (O(1)), and reference updates are O(1).

### Edge Cases
- **Empty List**: No deletion occurs, and an error is reported.
- **Value at Head**: Handled by `delete_at_beginning`.
- **Value Not Found**: Traversal reaches end, and an error is reported.
- **Value in Middle or End**: The first matching node is removed.
- **Multiple Occurrences**: Only the first occurrence is deleted.

### Example
**Initial List**: `0 -> 1 -> 2 -> 2 -> None` (head points to node with data 0)
- Call: `delete_first_occurrence(2)`
- **Step 1**: Check `head` is not `None`, `head.data != 2`.
- **Step 2**: Traverse: Start at `0`, move to `1` (`1.next.data == 2`).
- **Step 3**: Check `current.next` (node with 2) is not `None`.
- **Step 4**: Set `current.next` to `current.next.next` (second node with 2).
- **Resulting List**: `0 -> 1 -> 2 -> None`

### Illustration
```
Before: head -> [0|next] -> [1|next] -> [2|next] -> [2|None]
After:  head -> [0|next] -> [1|next] -> [2|None]
```

## Error Handling
All four methods include robust error handling:
- **Empty List**: Checked in all methods, preventing invalid operations.
- **Invalid Position**: `delete_at_position` validates negative positions and out-of-range indices.
- **Value Not Found**: `delete_first_occurrence` reports when the value is absent.
- **Null References**: Traversal in `delete_at_end`, `delete_at_position`, and `delete_first_occurrence` ensures safe navigation.

## Practical Considerations
- **Efficiency**: `delete_at_beginning` is O(1), ideal for stack-like operations. `delete_at_end`, `delete_at_position`, and `delete_first_occurrence` are O(n) due to traversal, less efficient for large lists.
- **Use Cases**: `delete_at_beginning` suits removing recent items (e.g., undo stack). `delete_at_end` is useful for queue-like structures. `delete_at_position` supports indexed removals (e.g., playlist management). `delete_first_occurrence` is ideal for removing specific entries (e.g., task cancellation).
- **Pythonic Style**: Methods use snake_case per PEP 8, ensuring readability and consistency.

## Conclusion
The `delete_at_beginning`, `delete_at_end`, `delete_at_position`, and `delete_first_occurrence` methods provide comprehensive mechanisms for removing nodes from a singly linked list in Python. Each addresses specific deletion needs with distinct time complexities and edge cases. By understanding their logic and implementation, developers can effectively apply these operations in scenarios requiring dynamic data removal, such as implementing stacks, queues, or event logs. The provided code ensures robustness through error handling and adherence to Python’s style guidelines, serving as a reliable foundation for further development.

