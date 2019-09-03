/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode sum = new ListNode(0); 
        ListNode dummysum = sum;
        ListNode d1 = l1;
        ListNode d2 = l2;
        int carry = 0;
        while(d1 != null || d2 != null){
            int x = (d1 != null) ? d1.val : 0;
            int y = (d2 != null) ? d2.val : 0;
            sum.next = new ListNode((x + y + carry) % 10);
            carry = (x + y + carry) / 10;
            if(d1 != null) d1 = d1.next; 
            if(d2 != null) d2 = d2.next;
            sum = sum.next;
        }
        if(carry > 0){
            sum.next = new ListNode(carry);
        }
        return dummysum.next;
    }
}
