# https://binarysearch.com/problems/Add-Linked-Lists

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def solve(self, l0, l1):
        carry = 0
        res = LLNode(-1)
        crawl = res


        while l0 or l1 or carry:
            node = LLNode(carry)

            if l0:
                node.val += l0.val
                l0 = l0.next

            if l1:
                node.val += l1.val
                l1 = l1.next

            if node.val >= 10:
                node.val = node.val % 10
                carry = 1
            else:
                carry = 0
            
            crawl.next = node
            crawl = crawl.next
        
        return res.next
     

class Solution:
    def solve(self, l0, l1):
        cur1, cur2 = l0, l1
        counter = 1
        sm = 0

        while cur1:
            val = cur1.val*counter
            counter*=10
            sm+=val
            cur1 = cur1.next

        counter=1
        while cur2:
            val = cur2.val*counter
            counter*=10
            sm+=val
            cur2 = cur2.next


        result = LLNode(0)
        if sm == 0:
            return result

        cur = result

        while sm > 0:
            rem = sm % 10
            newNode = LLNode(rem)
            cur.next = newNode
            sm//=10
            cur = cur.next

        result = result.next
        return result