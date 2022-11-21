/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} color
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, color) {
    fill(image, sr, sc, color, image[sr][sc])
    return image;
};

const fill = function(image, sr, sc, color, prev){
    if(
        sr >= 0 &&
        sc >= 0 &&
        sr < image.length &&
        sc < image[0].length &&
        image[sr][sc] !== color &&
        image[sr][sc] === prev
    ){
        image[sr][sc] = color;
        fill(image, sr + 1, sc, color, prev);
        fill(image, sr - 1, sc, color, prev);
        fill(image, sr, sc + 1, color, prev);
        fill(image, sr, sc - 1, color, prev);
    }
    
}
