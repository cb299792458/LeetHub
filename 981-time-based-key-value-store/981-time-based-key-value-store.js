
var TimeMap = function() {
    this.store = {};
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
    if(!this.store[key]) this.store[key] = [];
    this.store[key].push({timestamp,value});
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
    // if(!this.store[key]) return ""
    return bsearch(this.store[key],timestamp);
};

function bsearch(store,timestamp){
    if(!store) return ''
    if(store.length===1){
        return store[0].timestamp <= timestamp ? store[0].value : '';
    }
    const midIndex = Math.floor(store.length/2);
    if(store[midIndex].timestamp > timestamp) return bsearch(store.slice(0,midIndex),timestamp);
    return bsearch(store.slice(midIndex),timestamp);
    
}

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */