
class RandomizedSet{
    constructor(){
        this.set = new Set
    }
    
    /** 
     * @param {number} val
     * @return {boolean}
     */
    insert = function(val) {
        let res = !this.set.has(val);
        this.set.add(val);
        return res;
    }

    /** 
     * @param {number} val
     * @return {boolean}
     */
    remove = function(val) {
        let res = this.set.has(val);
        this.set.delete(val);
        return res;
    }

    /**
     * @return {number}
     */
    getRandom = function() {
        const entries = [...this.set]
        return entries[Math.floor(entries.length*Math.random())]
    }

}
/** 
 * Your RandomizedSet object will be instantiated and called as such:
 * var obj = new RandomizedSet()
 * var param_1 = obj.insert(val)
 * var param_2 = obj.remove(val)
 * var param_3 = obj.getRandom()
 */