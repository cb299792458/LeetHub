var kthSmallest = function(root, k) {
    let count = 0;
    let result = null

    var traverse = function(root) {
        if (!root || result) return;

        traverse(root.left);
        count++;
        if (count === k) {
            result = root.val;
            return;
        }
        traverse(root.right);
    }

    traverse(root);
    return result;
};