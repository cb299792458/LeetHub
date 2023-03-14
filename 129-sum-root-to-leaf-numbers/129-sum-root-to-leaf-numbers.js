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
 * @return {number}
 */
var sumNumbers = function(root) {
    function traverse(node, curr = 0){
        // console.log(curr);
        if(!node) return curr;
        curr = (10*curr) + node.val;
        
        if(!node.right) return traverse(node.left,curr);
        if(!node.left) return traverse(node.right,curr);
        return traverse(node.left,curr) + traverse(node.right,curr);
    }
    
    return traverse(root);
};