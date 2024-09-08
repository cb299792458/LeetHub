/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */

const splitListToParts = (head, k) => {
    // Get total length
    let curr = new ListNode(0, head);
    let length = 0;

    while (curr.next) {
        curr = curr.next;
        length += 1;
    }

    // Get lengths of parts
    const nodes = Math.floor(length / k);
    const extra = length % k;
    const lengths = Array.from({ length: k }, (_, i) => nodes + (i < extra ? 1 : 0));

    const parts = [];
    curr = new ListNode(0, head);

    for (let n of lengths) { // For each part
        let temp = curr; // Remember tail of last part
        parts.push(curr.next); // Add head of part to result
        for (let i = 0; i < n; i++) {
            curr = curr.next; // Move to tail of current part
        }
        temp.next = null; // Cut tail of last part
    }
    return parts;
}
