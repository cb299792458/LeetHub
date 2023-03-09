
var BSTIterator = function(root) {
    this.root = root;
    this.pointer = 0;
    this.nums = [-Infinity];
    let nums = this.nums;
    function traverse(node){
        if(!node) return;
        traverse(node.left);
        nums.push(node.val);
        traverse(node.right);
    }
    
    traverse(root);
    // console.log(nums);
    
};


BSTIterator.prototype.next = function() {
    this.pointer++;
    return this.nums[this.pointer];
};

BSTIterator.prototype.hasNext = function() {
    return this.pointer < this.nums.length-1;
};

