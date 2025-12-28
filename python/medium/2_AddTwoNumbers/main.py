# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        l3 = ListNode ()
        head = l3
        resto = 0
        while ( l1 != None or l2 != None or resto > 0 ):
            value = resto

            if l1 != None:
                value += l1.val
                l1 = l1.next

            if l2 != None:
                value += l2.val
                l2 = l2.next

            l3.next = ListNode ( value % 10 )
                
            resto = value // 10

            l3 = l3.next

        return head.next
    
    def addTwoNumbers2 ( self, l1, l2):

        head = None
        tail = None
        resto = 0

        while l1 != None or l2 != None or resto > 0:
            value = resto

            if l1 != None:
                value += l1.val
                l1 = l1.next

            if l2 != None:
                value += l2.val
                l2 = l2.next

            newNode = ListNode ( value % 10)

            resto = value // 10

            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
        
        return head
                

            
             


def makeList ( nums ):
    curr = ListNode ()
    head = curr
    for n in nums:
        curr.next = ListNode ( n )
        curr = curr.next
    return head.next

def toList ( node ):
    out = []
    while node != None:
        out.append (node.val)
        node = node.next
    return out


l1 = makeList ( [2, 4, 3])

l2 = makeList ( [5, 6, 4])

S = Solution ()

resultado = S.addTwoNumbers2 ( l1, l2)

mostrar = toList( resultado)

print ( mostrar)



