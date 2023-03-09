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
    // if(this.dict.has(searchWord)) return false;
    
    let rightLength = false;
    for(let dictWord of this.dict){
        if(dictWord.length === searchWord.length) rightLength = true;
    }
    if(!rightLength) return false;
    
    for(let index = 0; index<searchWord.length; index++){
        let char = searchWord[index];
        for(let letter of letters){ // for every letter
            if(char===letter) continue;
            
            let newWord = searchWord.slice(0,index) + letter + searchWord.slice(index+1);
            if(this.dict.has(newWord)) return true;
        }
    }
    
    return false;
};

/*
searchWords: scar
dict has scar
s->letter
acar, bcar, ccar, scar NOT CHANGED


*/
function compare(str1,str2){
    
}