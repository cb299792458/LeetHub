/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let left = 0;
    let right = height.length - 1;
    let area = 0;
    
    while(left < right){
        area = Math.max(area,(right-left)*Math.min(height[left],height[right]));
        if(height[left] > height[right]){
            right--;
        } else {
            left++;
        }
    }
    
    return area;
};