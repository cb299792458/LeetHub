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
 * @return {number[][]}
 */
var levelOrder = function(root) {
    const firstLevel = [root];
    const res = [];
    
    traverseLevel(firstLevel,res);

    return res;
};

function traverseLevel(level,res){
    if(!level.length) return
    let thisLevel = [];
    let nextLevel = [];
    for(let node of level){
        if(!node) continue;
        thisLevel.push(node.val);
        nextLevel.push(node.left);
        nextLevel.push(node.right);
    }
    
    if(thisLevel.length) res.push(thisLevel);
    traverseLevel(nextLevel,res);
}