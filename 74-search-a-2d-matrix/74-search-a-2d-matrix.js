/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
//     if(target<matrix[0][0]) return false;
//     let top = 0;
//     let bot = matrix.length-1;
//     while(top !== bot){
//         let mid = Math.floor((top+bot)/2);
//         if(target<matrix[mid][0]){
//             bot = mid+1;
//         } else if(target>matrix[mid].at(-1)){
//             top = mid-1;
//         } else {
//             top = mid;
//             bot = mid;
//         }
//     }
//     console.log(top);
//     const sub = matrix[top];
//     let left = 0;
//     let right = sub.length-1;
//     if(target<sub[left]) return false;
//     while(left < right){
        
//         let mid = Math.floor((left+right)/2);
//         // console.log(left,right,mid)
//         if(sub[mid]===target) return true;
//         if(sub[mid]<target) left = mid+1;
//         if(sub[mid]>target) right = mid-1;
//     }
//     return sub[left]===target;
// };

    let l = 0; let r = matrix.length - 1;

    while (l <= r) {
        const mid = Math.floor((l + r) / 2);
        const first = matrix[mid][0];
        const last = matrix[mid][matrix[mid].length - 1];
        if (target === first || target === last) return true;
        if (target > first && target < last) return binarySearch(matrix[mid], target);
        if (target < first) r = mid - 1;
        else l = mid + 1;
    }
    return false;
};

function binarySearch(nums, target) {
  let l = 0;
  let r = nums.length - 1;

  while (l <= r) {
    const mid = Math.floor((l + r) / 2);
    if (nums[mid] === target) return true;
    if (nums[mid] < target) l = mid + 1;
    else r = mid - 1;
  }

  return false;
}