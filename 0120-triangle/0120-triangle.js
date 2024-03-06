const minimumTotal = (triangle) => {
    for (let i=1; i<triangle.length; i++) {
        const lastRow = triangle[i-1];
        const thisRow = triangle[i];
        for (let j=0; j<thisRow.length; j++) {
            if (j===0) {
                triangle[i][j] += lastRow[j];
            } else if (j===thisRow.length-1) {
                triangle[i][j] += lastRow[j-1];
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