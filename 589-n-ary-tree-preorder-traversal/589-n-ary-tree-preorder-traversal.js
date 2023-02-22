/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[]}
 */
var preorder = function(root) {
    let res = [];
    if(!root) return res;
    
    res = res.concat(root.val);
    for(let child of root.children) res = res.concat(preorder(child));

    return res;
};