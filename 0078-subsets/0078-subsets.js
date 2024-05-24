/**
 * @param {number[]} nums
 * @return {number[][]}
 
 always return empty array
 always return each element at least once
 
 [] -> [[]]
 [0] -> [[], [0]]
 [0,1] -> [[], [0], [1], [0,1]]
 
 take first number [1,2,3] 1
 iterate through array [2,3]
 push a unique array with every number [[1,2],[1,3]]
 [2,3]
 [1,2,3]
 [1],[2],[3]
 
 create an array of empty arrays of length 2**nums.length
 iterate through nums:
    count = 2**i
    skip count subarrays, add nums[i] to count subarrays
 []  []  []  []  []  []  []  [] 
 
 [     ]
 [1    ]
 [  2  ]
 [1,2  ]
 [    3]
 [1,  3]
 [  2,3]
 [1,2,3]
 */
var subsets = function(nums) {
    let result = new Array(2**nums.length).fill().map(() => new Array())

    for (let i=0;i<nums.length;i++) {
        let count = 2**i
        let currentNum = nums[i]
        let push = false
        let currentCount = 0
        for (let j=0;j<result.length;j++) {
            if (push) {
                result[j].push(currentNum)
            }
            
            currentCount++;
            if (currentCount === count) {
                currentCount = 0
                push = !push
            }
        }
    }
    return result
};