const letters = 'abcdefghijklmnopqrstuvwxyz';

var MagicDictionary = function() {
    this.dict = new Set;
};

MagicDictionary.prototype.buildDict = function(dictionary) {
    // this.dict = dictionary;
    for(let word of dictionary) this.dict.add(word);
};

MagicDictionary.prototype.search = function(searchWord) {
    for(let index = 0; index<searchWord.length; index++){
        let char = searchWord[index];
        for(let letter of letters.split('')){
            if(char===letter) continue;
            
            let newWord = searchWord.slice(0,index) + letter + searchWord.slice(index+1);
            if(this.dict.has(newWord)) return true;
        }
    }
    
    return false;
};

