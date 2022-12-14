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
 * @return {number[]}
 */
var rightSideView = function(root) {
    //dfs
    let stack = [{node: root, level: 1}]
    let answer = new Map
    let level = 1
    let result = []

    while(stack.length){
        let curr = stack.pop()
        if(curr.node){
            if(!answer.has(curr.level)) answer.set(curr.level, curr.node.val)

            if(curr.node.left) stack.push({node: curr.node.left, level: curr.level + 1})
            if(curr.node.right) stack.push({node: curr.node.right, level: curr.level + 1})

        }
    }

    answer.forEach(ode => {
        result.push(ode)
    })

    return result
};