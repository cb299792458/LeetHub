/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let area = 0;
    let left = 0;
    let right = 0;

    while(left < height.length){
        
        if(height[left] > height[right] || left === right){
            
            let enclosedHeight = Math.min(height[left],height[right])

            for(let mid=left+1;mid<right;mid++){
                if(height[mid] < enclosedHeight){
                    area += enclosedHeight - height[mid];
                    
                    height[mid] = enclosedHeight; 
                }
                
            }
            right ++;
        } else {
            let enclosedHeight = Math.min(height[left],height[right])

            for(let mid=left+1;mid<right;mid++){
                if(height[mid] < enclosedHeight){
                    area += enclosedHeight - height[mid];                    
                    height[mid] = enclosedHeight; 
                }
            }
            
            left = right;
        }
    }
    
    return area;
};