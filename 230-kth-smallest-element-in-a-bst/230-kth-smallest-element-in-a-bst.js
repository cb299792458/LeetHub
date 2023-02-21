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
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let nums = []
    function traverse(node){
        
        if(nums.length===k) return nums[k-1];
        if(!node) return false;
        if(traverse(node.left)) return traverse(node.left);
        nums.push(node.val);
        if(traverse(node.right)) return traverse(node.right);
        return nums[k-1]
    }

    
    return traverse(root);
    
};