/**
 * @param {string[]} words
 * @param {string} order
 * @return {boolean}
 */
var isAlienSorted = function(words, order) {
    function sorted(first,second){
        for(let i=0;i<first.length;i++){
            console.log(first[i],second[i])
            if(first[i] && !second[i]) return false;
            if(order.indexOf(first[i])>order.indexOf(second[i])) return false;
            if(order.indexOf(first[i])<order.indexOf(second[i])) return true;
        }
        return true;
    }
    
    for(let i=0;i<words.length-1;i++){
        if(!sorted(words[i],words[i+1])) return false;
    }
    return true;
};