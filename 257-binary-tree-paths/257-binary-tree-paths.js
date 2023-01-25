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
 * @return {string[]}
 */
var binaryTreePaths = function(root) {
    const ans = new Set;
    
    function backtrack(node,path){
        if(!node){
            return;
        }
        
        path.push(node.val);
        
        if(!node.left && !node.right){
            ans.add(path.join('->'));
            return;
        } else {
            backtrack(node.left,[...path]);
            backtrack(node.right,[...path]);
        }
        
    };
    
    backtrack(root,[]);
    return Array.from(ans);
};