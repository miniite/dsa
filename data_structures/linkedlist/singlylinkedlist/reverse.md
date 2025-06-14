# Reversing a Singly Linked List in Python

## Introduction
Reversing a singly linked list rearranges its nodes so that the last node becomes the first, and each node’s `next` pointer points to the previous node. This article presents four methods to reverse a linked list: two iterative (standard iterative and three-pointer) and two recursive (standard recursive and recursive with helper). Each method is implemented in the `LinkedList` class, with code, logic, complexity analysis, and a comparison, using the existing `LinkedList` and `Node` classes.



## 1. Standard Iterative Method

### Code
```python
def reverse_iterative(self):
    if self.head is None or self.head.next is None:
        return
    prev = None
    current = self.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    self.head = prev
```

### Logic
- If the list is empty or has one node, return.
- Use `prev`, `current`, and `next_node` pointers.
- Traverse the list, reversing each node’s `next` pointer to point to `prev`.
- Update `head` to the last node (`prev`).

### Time Complexity
- **O(n)**: Traverses \( n \) nodes once.

### Space Complexity
- **O(1)**: Uses three pointers.

## 2. Iterative with Three Pointers

### Code
```python
def reverse_three_pointers(self):
    if self.head is None or self.head.next is None:
        return
    prev = None
    current = self.head
    next_node = current.next
    while current:
        current.next = prev
        prev = current
        current = next_node
        if next_node:
            next_node = next_node.next
    self.head = prev
```

### Logic
- Similar to standard iterative, but initializes `next_node` early.
- Explicitly tracks three pointers (`prev`, `current`, `next_node`) in each iteration.
- Reverses links and updates pointers until `current` is `None`.

### Time Complexity
- **O(n)**: Traverses \( n \) nodes.

### Space Complexity
- **O(1)**: Uses three pointers.

## 3. Standard Recursive Method

### Code
```python
def reverse_recursive(self):
    if self.head is None or self.head.next is None:
        return
    def _reverse_recursive(current):
        if current.next is None:
            self.head = current
            return current
        next_node = _reverse_recursive(current.next)
        next_node.next = current
        current.next = None
        return current
    _reverse_recursive(self.head)
```

### Logic
- If the list is empty or has one node, return.
- Recursively traverse to the last node, set it as `head`.
- Reverse links by setting each node’s `next` to the previous node.

### Time Complexity
- **O(n)**: Processes \( n \) nodes recursively.

### Space Complexity
- **O(n)**: Recursive call stack depth is \( n \).

## 4. Recursive with Helper Function

### Code
```python
def reverse_recursive_helper(self):
    if self.head is None or self.head.next is None:
        return
    
    def _reverse_helper(prev, current):
        if current is None:
            self.head = prev
            return
        next_node = current.next
        current.next = prev
        _reverse_helper(current, next_node)
    
    _reverse_helper(None, self.head)
```

### Logic
- If the list is empty or has one node, return.
- Use a helper function with `prev` and `current` parameters.
- Recursively reverse links, updating `head` when `current` is `None`.

### Time Complexity
- **O(n)**: Processes \( n \) nodes.

### Space Complexity
- **O(n)**: Recursive call stack depth is \( n \).

## Edge Cases
- **Empty List**: All methods return immediately.
- **Single Node**: No reversal needed, return as is.
- **Multiple Nodes**: Correctly reverse the list, updating `head`.

## Comparison

| Method                     | Time Complexity | Space Complexity | Advantages                     | Limitations                        |
|----------------------------|-----------------|------------------|--------------------------------|------------------------------------|
| Standard Iterative         | O(n)            | O(1)             | Simple, memory-efficient       | Slightly verbose pointer logic     |
| Three Pointers Iterative   | O(n)            | O(1)             | Explicit pointer management    | Redundant initialization           |
| Standard Recursive         | O(n)            | O(n)             | Elegant, concise recursion     | Stack overflow risk for large lists |
| Recursive with Helper      | O(n)            | O(n)             | Clearer recursive logic        | Stack overflow risk, extra function |

- **Preference**: Standard iterative is preferred for its simplicity, O(1) space complexity, and robustness for large lists.

## Example Usage
```python
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.display()  # Output: 1 -> 2 -> 3 -> None

llist.reverse_iterative()
llist.display()  # Output: 3 -> 2 -> 1 -> None

llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
llist.reverse_recursive()
llist.display()  # Output: 3 -> 2 -> 1 -> None
```

## Conclusion
The four methods efficiently reverse a singly linked list, with the standard iterative method preferred for its O(1) space complexity and simplicity. The three-pointer iterative method is similar but slightly redundant. Recursive methods are elegant but risk stack overflow for large lists due to O(n) space complexity. Each method handles edge cases robustly, making them suitable for various applications.

