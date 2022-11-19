/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let string = s.toLowerCase().split('').filter((c)=>{
        return 'qwertyuiopasdfghjklzxcvbnm1234567890'.includes(c);
    }).join('');
    // console.log(string);
    let ans = true;
    for(let i=0;i<=string.length/2;i++){
        if(string[i] !== string[string.length-i-1]){
            ans = false;
        }
    }
    return ans;
};