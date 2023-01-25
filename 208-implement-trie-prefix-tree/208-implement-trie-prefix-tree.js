
var Trie = function() {
    this.words = {};
};

/** 
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let current = this.words;
    for(let char of word){
        if(!current[char]) current[char] = {};
        current = current[char]
    }
    current['word?'] = true;
    
};

/** 
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let current = this.words;
    for(let char of word){
        if(!current[char]) return false;
        current = current[char]
    }
    return !!current['word?']
};

/** 
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let current = this.words;
    for(let char of prefix){
        if(!current[char]) return false;
        current = current[char]
    }
    return !!current
};

/** 
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */