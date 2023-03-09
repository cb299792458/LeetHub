const str = 'abcdefghijklmnopqrstuvwxyz';
const letters = str.split('');

var MagicDictionary = function() {
    this.dict = new Set;
};

MagicDictionary.prototype.buildDict = function(dictionary) {
    // this.dict = dictionary;
    for(let word of dictionary) this.dict.add(word);
};

MagicDictionary.prototype.search = function(searchWord) {
    for(let word of [...this.dict]){
        if(compare(word,searchWord)===1) return true;
    }
    
    return false;
};

function compare(str1,str2){
    if(str1.length !== str2.length) return false;
    
    let differences = 0;
    for(let i=0;i<str1.length;i++){
        if(str1[i]!==str2[i]) differences++;
    }
    return differences;
}







