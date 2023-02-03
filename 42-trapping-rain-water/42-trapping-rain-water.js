/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let area = 0;
    let left = 0;
    let right = 0;
    // let blockedArea = 0;
    
//     while(left < height.length){
//         console.log(`left is ${left}, and right is ${right}`)
//         // if(height[left]===0){
//         //     left++;
//         //     right++;
//         //     continue;
//         // }
        
//         if(right > height.length-1){ // change to right > right-1
            
//             height[left] = height[left]-1;
//             if(height[left]>0) continue;
            
            
//             left ++;
//             right = left;
//             blockedArea = 0;
//             continue;
//         }
//         // get height of left wall (height[left])
//           // look for right wall at least that height
//           // save the space between left and right to area
        
        
//         if(height[left] > height[right] || left === right){
//             if(height[right] < height[left]){
//                 blockedArea += height[right];
//             }
//             right ++;
//         } else {
//             // the right wall closed off some space
//             // save the space to the area variable
//             let currentArea = height[left] * (right - left - 1)
//             console.log(currentArea, blockedArea)
//             area += currentArea - blockedArea;
//             blockedArea = 0;
//             console.log(`the area is ${area}`)
                   
//             left = right;
//         }
//     }
    
    while(left < height.length){
        // console.log(`left is ${left}, and right is ${right}`)
        
        if(height[left] > height[right] || left === right){
            
            // console.log(height,height[left],height[right],right)
            let enclosedHeight = Math.min(height[left],height[right])

            for(let mid=left+1;mid<right;mid++){
                if(height[mid] < enclosedHeight){
                    // add area enclosed at mid
                    // console.log('enclosedheight is ', enclosedHeight, 'mid is ',mid, 'height mid is  ',height[mid]);
                    area += enclosedHeight - height[mid];
                    // console.log(`the area is ${area}`);
                    
                    height[mid] = enclosedHeight; 
                }
                // remember the enclosed area so you don't count it twice
                
            }
            right ++;
        } else {
            let enclosedHeight = Math.min(height[left],height[right])

            for(let mid=left+1;mid<right;mid++){
                if(height[mid] < enclosedHeight){
                    // add area enclosed at mid
                    area += enclosedHeight - height[mid];
                    // console.log(`the area is ${area}`);
                    
                    height[mid] = enclosedHeight; 
                }
                // remember the enclosed area so you don't count it twice  
            }
            
            
            left = right;
        }
    }
    

    return area;
};