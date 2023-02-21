/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if(!preorder.length) return null;
    
    let headVal = preorder.shift();
    let leftInorder = inorder.slice(0,inorder.indexOf(headVal));
    let rightInorder = inorder.slice(inorder.indexOf(headVal)+1);
    
    let leftPreorder = preorder.filter(x=>leftInorder.includes(x));
    let rightPreorder = preorder.filter(x=>rightInorder.includes(x));
    
    let head = new TreeNode(headVal, buildTree(leftPreorder,leftInorder), buildTree(rightPreorder,rightInorder));
    
    
    return head;
};