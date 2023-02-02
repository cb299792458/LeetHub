
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
    let store = this.store[key];
    if(!store) return '';

    let left = 0, right = store.length-1;
    if(timestamp<store[left].timestamp) return "";
    if(timestamp>store[right].timestamp) return store[right].value;
    
    while(left<right){
        let mid = Math.floor((left+right)/2);
        if(store[mid].timestamp===timestamp) return store[mid].value;
        if(store[mid].timestamp<timestamp){
            left = mid+1;
        }
        if(store[mid].timestamp>timestamp){
            right = mid-1;
        }
        
    }
    if(store[left].timestamp===timestamp) return store[left].value;
    return store[left-1].value;
    
}

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */