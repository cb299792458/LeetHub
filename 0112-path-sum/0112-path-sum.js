/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 
 breadth first search (QUEUE)
 5 4 8 11 13 4 7 2 1
 
 depth first search (STACK)
 5 4 11 7 2 8 13 4 1

 
 */
var hasPathSum = function(root, targetSum) {
    if (!root) return false;
    const stack = [ [root, 0] ];
    
    while (stack.length > 0) {
        let [currentNode, currentSum] = stack.pop();
        currentSum += currentNode.val;
        
        // base case
        if (!currentNode.left && !currentNode.right) {
            // this is a leaf
            if (currentSum === targetSum) {
                return true
            }
            
        }
        
        // right path
        if (currentNode.right) {
            stack.push([currentNode.right, currentSum]);
        }
        // left path
        if (currentNode.left) {
            stack.push([currentNode.left, currentSum]);
        }
    }
    return false;
};