class RandomizedSet {
    constructor(){
        this.set = new Set();
    };
    
    insert(val) {
        let res = !this.set.has(val);
        this.set.add(val);
        return res;
    };

    remove(val) {
        let res = this.set.has(val);
        this.set.delete(val);
        return res;
    };

    getRandom() {
        const entries = [...this.set];
        return entries[Math.floor(entries.length*Math.random())];
    };

};
