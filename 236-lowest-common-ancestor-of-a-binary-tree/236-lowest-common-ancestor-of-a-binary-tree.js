/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(node, p, q) {
    // if(badMemo.has(node)) return false;
    
    const descendant = (node,child)=>{
        if(!node) return false;
        if(node.val===child.val) return true;
        return descendant(node.left,child) || descendant(node.right,child);
    }
    let current = node;
    
    while(true){
        if(descendant(current.left,p)&&descendant(current.left,q)){
            current = current.left;
        } else if(descendant(current.right,p)&&descendant(current.right,q)){
            current = current.right;
        } else break
    }
    
    return current;
    
};