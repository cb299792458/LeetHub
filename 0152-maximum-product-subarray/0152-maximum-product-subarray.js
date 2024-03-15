var maxProduct = function(nums) {
    if (nums.length == 0) return -Infinity;
    if (nums.length == 1) return nums[0];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            return Math.max(maxProduct(nums.slice(0, i)), maxProduct(nums.slice(i + 1)), 0);
        }
    }

    let totalProduct = 1;
    for (let num of nums) {
        totalProduct *= num;
    }

    if (totalProduct > 0) return totalProduct;

    //start from left, remove all positive, remove first negative
    let cutLeft = totalProduct;
    let l = 0;
    while (nums[l] > 0) {
        cutLeft /= nums[l];
        l++;
    }
    cutLeft /= nums[l];

    let cutRight = totalProduct;
    let r = nums.length - 1;
    while (nums[r] > 0) {
        cutRight /= nums[r];
        r--;
    }
    cutRight /= nums[r];

    return Math.max(cutLeft, cutRight);
};