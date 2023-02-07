var trap = function(height) {
    let length = height.length;
    let leftWall = new Array(length);
    let rightWall = new Array(length);
    leftWall[0] = 0;
    rightWall[length-1] = 0;
    for(let i=1;i<length;i++){
        leftWall[i] = Math.max(leftWall[i-1],height[i-1]);
    }
    for(let j=length-2;j>=0;j--){
        rightWall[j] = Math.max(rightWall[j+1],height[j+1]);
    }
    console.log(leftWall,rightWall)
    
    let area = 0;
    for(let k=0;k<length;k++){
        area += Math.max(0,Math.min(leftWall[k],rightWall[k])-height[k])
    }
    return area;
};