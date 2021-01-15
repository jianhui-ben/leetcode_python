#1634. Add Two Polynomials Represented as Linked Lists
#A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

#Each node has three attributes:

#coefficient: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
#power: an integer representing the exponent. The power of the term 9x4 is 4.
#next: a pointer to the next node in the list, or null if it is the last node of the list.
#For example, the polynomial 5x3 + 4x - 7 is represented by the polynomial linked list illustrated below:


# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        temp=PolyNode()
        start=temp
        while poly1 and poly2:
            if poly1.power> poly2.power:
                start.next= PolyNode(x=poly1.coefficient, y=poly1.power)
                poly1=poly1.next
                start=start.next
            elif poly1.power< poly2.power:
                start.next= PolyNode(x=poly2.coefficient, y=poly2.power)
                poly2=poly2.next
                start=start.next
            else:
                if poly2.coefficient+poly1.coefficient!=0:
                    start.next= PolyNode(x=poly2.coefficient+poly1.coefficient\
                                         , y=poly2.power)
                    start=start.next
                poly1=poly1.next
                poly2=poly2.next
        if poly1:start.next= poly1
        elif poly2: start.next= poly2
        return temp.next