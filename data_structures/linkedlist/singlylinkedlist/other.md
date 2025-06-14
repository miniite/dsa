# Detailed Explanation of Singly Linked List Traversal and Length Methods in Python

## Introduction
Traversal and length calculation are fundamental operations in a singly linked list, enabling visualization of the list’s contents and determination of its size. The provided Python implementation includes two methods for these purposes: `display` for traversing and printing the list, and `get_length` for counting the number of nodes. This document provides a comprehensive explanation of each method, detailing their purpose, logic, step-by-step execution, time complexity, edge cases, and practical examples. The explanation assumes familiarity with the linked list structure, where each node contains data and a reference to the next node, managed via a `head` pointer.

## 1. Traversal (`display`)

### Purpose
The `display` method traverses the singly linked list and prints the data of each node in sequence, followed by `None` to indicate the end of the list. This method is primarily used for debugging and visualization, allowing developers to inspect the list’s contents.

### Code
```python
def display(self):
    if self.head is None:
        print("List is empty")
        return
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```

### Logic
- Check if the list is empty (`head` is `None`). If so, print "List is empty" and exit.
- Start at the `head` and traverse each node, printing its `data` followed by an arrow (` -> `) to represent the link.
- When the end is reached (`current` is `None`), print "None" to mark the list’s termination.

### Step-by-Step Process
1. **Check Empty List**: If `self.head` is `None`, print "List is empty" and exit.
2. **Initialize**: Set `current` to `self.head`.
3. **Traverse and Print**: While `current` is not `None`:
   - Print `current.data` followed by " -> ".
   - Move to the next node (`current = current.next`).
4. **Terminate Output**: Print "None" to indicate the end of the list.

### Time Complexity
- **O(n)**: The method traverses all `n` nodes in the list to print their data. Printing and pointer updates are O(1) per node.

### Edge Cases
- **Empty List**: Prints "List is empty" and exits without traversal.
- **Single-Node List**: Prints the single node’s data followed by " -> None".
- **Multi-Node List**: Prints all nodes’ data in sequence, ending with "None".

### Example
**Initial List**: `0 -> 1 -> 1.5 -> 2 -> None` (head points to node with data 0)
- Call: `display()`
- **Step 1**: Check `head` is not `None`.
- **Step 2**: Initialize `current` to `head` (node with 0).
- **Step 3**: Traverse and print:
   - Print `0 -> `, move to node with 1.
   - Print `1 -> `, move to node with 1.5.
   - Print `1.5 -> `, move to node with 2.
   - Print `2 -> `, move to `None`.
- **Step 4**: Print "None".
- **Output**: `0 -> 1 -> 1.5 -> 2 -> None`

### Illustration
```
List: head -> [0|next] -> [1|next] -> [1.5|next] -> [2|None]
Display:
- Print: 0 -> 1 -> 1.5 -> 2 -> None
```

## 2. Get Length (`get_length`)

### Purpose
The `get_length` method counts the number of nodes in the singly linked list and returns this count as an integer. This method is useful for determining the list’s size, which can inform other operations or validate indices.

### Code
```python
def get_length(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count
```

### Logic
- Initialize a counter (`count`) to 0.
- Start at the `head` and traverse each node, incrementing `count` for each node encountered.
- When the end is reached (`current` is `None`), return the `count`.

### Step-by-Step Process
1. **Initialize**: Set `count` to 0 and `current` to `self.head`.
2. **Traverse and Count**: While `current` is not `None`:
   - Increment `count` by 1.
   - Move to the next node (`current = current.next`).
3. **Return Count**: Return the final value of `count`.

### Time Complexity
- **O(n)**: The method traverses all `n` nodes in the list to count them. Incrementing the counter and updating the pointer are O(1) per node.

### Edge Cases
- **Empty List**: `head` is `None`, so `count` remains 0, and 0 is returned.
- **Single-Node List**: Traverses one node, returning 1.
- **Multi-Node List**: Counts all nodes, returning the total number.

### Example
**Initial List**: `0 -> 1 -> 1.5 -> 2 -> None` (head points to node with data 0)
- Call: `get_length()`
- **Step 1**: Initialize `count = 0`, `current = head` (node with 0).
- **Step 2**: Traverse and count:
   - `count = 1`, move to node with 1.
   - `count = 2`, move to node with 1.5.
   - `count = 3`, move to node with 2.
   - `count = 4`, move to `None`.
- **Step 3**: Return `count = 4`.
- **Result**: 4

### Illustration
```
List: head -> [0|next] -> [1|next] -> [1.5|next] -> [2|None]
Get Length:
- Count node 0: count = 1
- Count node 1: count = 2
- Count node 1.5: count = 3
- Count node 2: count = 4
- Return: 4
```

## Error Handling
Both methods include robust error handling:
- **Empty List**: `display` prints "List is empty" and exits; `get_length` returns 0.
- **Null References**: Traversal in both methods safely checks `current` to avoid dereferencing `None`.

## Practical Considerations
- **Efficiency**: Both methods are O(n) due to traversal, making them suitable for small to medium lists but less efficient for very large lists compared to array-based structures with O(1) length access.
- **Use Cases**: `display` is ideal for debugging, logging, or visualizing the list’s state (e.g., showing a playlist’s contents). `get_length` is useful for validating indices, determining list capacity, or informing operations like insertions (e.g., checking if a position is valid).
- **Pythonic Style**: Methods use snake_case per PEP 8, ensuring readability and consistency.
- **Output Format**: `display` uses a clear, arrow-separated format to represent links, while `get_length` returns a simple integer, making both outputs intuitive.

## Conclusion
The `display` and `get_length` methods provide essential functionality for inspecting and measuring a singly linked list in Python. The `display` method facilitates visualization by printing the list’s contents, while `get_length` quantifies the list’s size, both with linear time complexity and robust error handling. By understanding their logic and implementation, developers can effectively utilize these operations in scenarios requiring list inspection or size determination, such as debugging data structures or validating operations. The provided code adheres to Python’s style guidelines and serves as a reliable foundation for further exploration of linked list operations.

