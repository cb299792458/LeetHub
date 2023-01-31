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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if(!p && !q) return true;
    if(!p || !q) return false;
    if(p.val !== q.val) return false;
    if( !isSameTree(p.left, q.left) ) return false;
    if( !isSameTree(p.right, q.right) ) return false;
    return true;
};

var isSubtree = function(root, subRoot) {
    
    if(!root) return !subRoot;
    // if(!root)
    return isSameTree(root, subRoot) || isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)
};

