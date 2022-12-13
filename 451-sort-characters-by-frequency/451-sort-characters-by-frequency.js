/**
 * @param {string} s
 * @return {string}
 */
var frequencySort = function(s) {
    
    let buckets = new Array(62).fill(0);
    
    let chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcedfghijklmnopqrstuvwyxz1234567890'.split('')
    for(let input of s){
        buckets[chars.indexOf(input)]++
    }
    
    // console.log(buckets);
    // buckets is an array
    // the index is where in chars the char is found
    // the element is the count of times that char appears in s
    
    let output = '';
    let charAmount = {};
    for(let i=0; i<buckets.length; i++){
        let char = chars[i];
        let amount = buckets[i];
        
        if(amount === 0){continue}
        
        charAmount[char] = [char,amount];
        
    }
    let toSort = Object.values(charAmount);
    
    let sorted = toSort.sort((a,b)=>{
        if(a[1] > b [1]){
            return -1;
        }
        return 1;
    });
    
    for(let element of sorted){
        let [char,amount] = element;
        for(let i=0;i<amount;i++){
            output += char;
        }
    }
    

    return output;
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    // let counts = {};
    // s.split('').forEach((char)=>{
    //     counts[char] = counts[char] ? counts[char] + 1 : 1;
    // });
    // let countArr = Object.entries(counts).sort((a,b)=>{return b[1] - a[1]})
    // let ans = '';
    // countArr.forEach((arr)=>{
    //    for(let i = 0; i < arr[1]; i++){
    //        ans += arr[0];
    //    } 
    // });
    // return ans;
};