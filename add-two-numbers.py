class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __iter__(self):
        curNode = self
        while curNode is not None:
            yield curNode
            curNode = curNode.next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(None)
        ret = head
        while l1 != None or l2 != None:
            x = l1.val if l1 != None and l1.val != None else 0
            y = l2.val if l2 != None and l2.val != None else 0
            sum = x + y + carry
            carry = sum // 10
            ret.next = ListNode(sum % 10)
            ret = ret.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None

        if carry == 1:
            ret.next = ListNode(carry)

        result = []
        for node in head.next:
            result.append(node.val)

        return result

if __name__ == '__main__':
    l1 = ListNode(1,ListNode(2,ListNode(3)))
    l2 = ListNode(4,ListNode(5,ListNode(6)))

    s = Solution()
    print(s.addTwoNumbers(l1,l2))

"""
The pseudocode is as following:

Initialize current node to dummy head of the returning list.
Initialize carry to 00.
Initialize pp and qq to head of l1l1 and l2l2 respectively.
Loop through lists l1l1 and l2l2 until you reach both ends.
Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
Set sum = x + y + carrysum=x+y+carry.
Update carry = sum / 10carry=sum/10.
Create a new node with the digit value of (sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
Advance both pp and qq.
Check if carry = 1carry=1, if so append a new node with digit 11 to the returning list.
Return dummy head's next node.
"""