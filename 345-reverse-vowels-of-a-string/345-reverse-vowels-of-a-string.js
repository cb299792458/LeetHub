/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {
    let vowels = new Set('aeiouAEIOU'.split(''));

    let left=0,right=s.length-1;
    let arr = s.split('');
    while(left<right){
        if(!vowels.has(arr[left])){
            left++;
            continue;
        }
        if(!vowels.has(arr[right])){
            right--;
            continue;
        }
        [arr[left],arr[right]] = [arr[right],arr[left]];
        right--;
        left++;
    }
    return arr.join('');
};