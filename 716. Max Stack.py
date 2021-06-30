#716. Max Stack
#Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

#Implement the MaxStack class:

#MaxStack() Initializes the stack object.
#void push(int x) Pushes element x onto the stack.
#int pop() Removes the element on top of the stack and returns it.
#int top() Gets the element on the top of the stack without removing it.
#int peekMax() Retrieves the maximum element in the stack without removing it.
#int popMax() Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the top-most one.
 

#Example 1:

#Input
#["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
#[[], [5], [1], [5], [], [], [], [], [], []]
#Output
#[null, null, null, null, 5, 5, 1, 5, 1, 5]

#Explanation
#MaxStack stk = new MaxStack();
#stk.push(5);   // [5] the top of the stack and the maximum number is 5.
#stk.push(1);   // [5, 1] the top of the stack is 1, but the maximum is 5.
#stk.push(5);   // [5, 1, 5] the top of the stack is 5, which is also the maximum, because it is the top most one.
#stk.top();     // return 5, [5, 1, 5] the stack did not change.
#stk.popMax();  // return 5, [5, 1] the stack is changed now, and the top is different from the max.
#stk.top();     // return 1, [5, 1] the stack did not change.
#stk.peekMax(); // return 5, [5, 1] the stack did not change.
#stk.pop();     // return 1, [5] the top of the stack and the max element is now 5.
#stk.top();     // return 5, [5] the stack did not change.
from sortedcontainers import SortedDict

class DoublyLinkedNode:
    def __init__(self, val = None):
        self.val = val
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = DoublyLinkedNode() 
        self.tail = DoublyLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_top = DLL()
        self.sorted_stack = SortedDict() ##  key: val; val: list of DLL nodes
        
    def push(self, x: int) -> None:
        previous = self.stack_top.tail.prev
        previous.next = DoublyLinkedNode(val = - x)
        previous.next.prev = previous
        previous.next.next = self.stack_top.tail
        self.stack_top.tail.prev = previous.next

        
        if -x in self.sorted_stack:
            self.sorted_stack[-x].append(self.stack_top.tail.prev)
        else:
            self.sorted_stack[-x] = [self.stack_top.tail.prev]

    def pop(self) -> int:
        res = self.stack_top.tail.prev.val
        popped_node = self.sorted_stack[res].pop()
        
        if not len(self.sorted_stack[res]):
            self.sorted_stack.pop(res)
        
        previous, next_one = popped_node.prev, popped_node.next
        previous.next = next_one
        next_one.prev = previous
        return - res
        

    def top(self) -> int:
        # print('top', 'sorted_stack', [{-i:len(self.sorted_stack[i])} for i in self.sorted_stack.keys()])
        # print(self.stack_top.val)
        return - self.stack_top.tail.prev.val
        