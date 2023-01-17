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
var goodNodes = function(root,largest = -Infinity) {

    // dfs
    let goodNode = 0;
    
    if(!root){return 0}
    if(root.val >= largest){
        goodNode = 1;
        largest = root.val;
    }
    
    return goodNode + goodNodes(root.left, largest) + goodNodes(root.right,largest);
};

