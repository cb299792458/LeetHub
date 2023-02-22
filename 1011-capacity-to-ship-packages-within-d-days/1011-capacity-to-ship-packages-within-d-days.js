// /**
//  * @param {number[]} weights
//  * @param {number} days
//  * @return {number}
//  */
// var shipWithinDays = function(weights, days) {
//     function checkWeight(w){
//         let capacity = w;
//         let ships = 1;
//         for(let weight of weights){
//             if(capacity >= weight){
//                 capacity -= weight;
//                 if(capacity===0){
//                     ships++;
//                     capacity = w;
//                 }
//             } else {
//                 if(weight>w) return false;
//                 ships++;
//                 capacity = w - weight;
//             }
//         }
//         return ships <= days;
//     }
//     let left = Math.max(...weights);
//     let right = weights.reduce((num,sum) => num+sum );
//     let res;
//     while(left<=right){
//         let mid = Math.floor((left+right)/2);
//         console.log(left,right,mid)
//         if(checkWeight(mid)){
//             res = mid;
//             right = mid-1;
//         } else {
//             left = mid+1;
//         }
//     }
//     return res;
// };

var shipWithinDays = function(weights, days) {
    
    let sum = 0;
    let max = 0;


    for(let w of weights){
        max = Math.max(w, max);
        sum += w
    }


    let low = max;
    let high = sum;
    let result;
    while(low <= high){
        let mid = Math.floor((low + high)/2);
       if(calculate(mid)){
           result = mid;
           high = mid - 1;
       } else{
           low = mid + 1;
       }
    }

return result

    function calculate(mid){
        let sum = 0;
        let day = 1;
        
        for(let i=0; i<weights.length; i++){
            if(sum+weights[i] <= mid){
                sum += weights[i]
            } else{
                sum = weights[i];
                day++
            }
        }
        if(day <= days) return true; 
        else return false;
    }

};