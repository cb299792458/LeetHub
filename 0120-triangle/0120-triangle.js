const minimumTotal = (triangle) => {
    for (let i=1; i<triangle.length; i++) {
        const row = triangle[i];
        for (let j=0; j<row.length; j++) {
            if (j===0) {
                triangle[i][j] += triangle[i-1][0];
            } else if (j===row.length-1) {
                triangle[i][j] += triangle[i-1][j-1];
            } else {
                triangle[i][j] += Math.min(
                    triangle[i-1][j],
                    triangle[i-1][j-1]
                )
            }
        }
    }
    return Math.min(...triangle[triangle.length-1])
};