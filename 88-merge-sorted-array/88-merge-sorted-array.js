/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    let [i,j] = [0,0];
    
    while(i<m+n){

        if(j>= n || (nums1[i] <= nums2[j] && i < m+j)){
           i++;
        } else {
            let k = nums1.length-1;
            while(k>i){
                nums1[k] = nums1[k-1];
                k--;
            }
            
            nums1[i] = nums2[j];
            j++;
            i++;
        } 
        
        console.log(nums1,nums2,i,j)
    }
};