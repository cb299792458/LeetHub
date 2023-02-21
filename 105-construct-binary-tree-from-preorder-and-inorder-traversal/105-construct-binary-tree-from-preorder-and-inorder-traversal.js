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
    
    let headVal = preorder[0];
    let index = inorder.indexOf(headVal);
    
//     let leftInorder = inorder.slice(0,index);
//     let rightInorder = inorder.slice(index+1);
    
//     let leftPreorder = preorder.slice(0,index);
//     let rightPreorder = preorder.slice(index);
    
    return new TreeNode(headVal,
                    buildTree(preorder.slice(1,index+1),inorder.slice(0,index)),
                    buildTree(preorder.slice(index+1),inorder.slice(index+1))
                );
    
};