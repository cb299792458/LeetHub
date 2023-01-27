
var MinStack = function() {
    this.stack = [{val: null, min: Infinity}];
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    let prevMin = this.stack[0].min;
    this.stack.unshift({val: val, min: Math.min(val,prevMin)})
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.shift()
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[0].val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack[0].min;
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */