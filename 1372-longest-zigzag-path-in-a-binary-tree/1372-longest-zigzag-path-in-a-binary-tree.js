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
var longestZigZag = function(root) {
    res = 0;
    function helper(node,left,length){
        if(!node) return;
        res=Math.max(res,length);
        
        if(left){
            helper(node.left,false,length+1)
            helper(node.right,true,1)
        } else {
            helper(node.left,false,1)
            helper(node.right,true,length+1)
        }

    }
    
    helper(root,true,0);
    helper(root,false,0);
    return res;
    
};