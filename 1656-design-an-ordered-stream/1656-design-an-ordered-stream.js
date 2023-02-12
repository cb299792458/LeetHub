/**
 * @param {number} n
 */
var OrderedStream = function(n) {
    this.current = 1;
    this.eles = {};
};

/** 
 * @param {number} idKey 
 * @param {string} value
 * @return {string[]}
 */
OrderedStream.prototype.insert = function(idKey, value) {
    this.eles[idKey] = value;
    let res = [];
    while(this.eles[this.current]){
        res.push(this.eles[this.current]);
        this.current++;
    }
    return res;
};

/** 
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(idKey,value)
 */