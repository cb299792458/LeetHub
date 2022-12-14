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
//     bfs
//     let queue = [root];
    // let largest = -Infinity;
//     let goodNodes = 0;
    
//     while(queue.length>0){
//         let curr = queue.shift();
//         if(curr.val >= largest){
//             goodNodes++;
//         }
//         largest = Math.max(largest,curr.val);
//         if(curr.left){queue.push(curr.left)}
//         if(curr.right){queue.push(curr.right)}
        
//     }
    
    // return goodNodes;
    
    // dfs
    let goodNode = 0;
    
    if(!root){return 0}
    if(root.val >= largest){
        goodNode = 1;
        largest = Math.max(largest,root.val);
    }
    
    return goodNode + goodNodes(root.left, largest) + goodNodes(root.right,largest);
};

