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

const fill = function(image, r, c, color, prev){
    if(
        r >= 0 &&
        c >= 0 &&
        r < image.length &&
        c < image[0].length &&
        image[r][c] !== color &&
        image[r][c] === prev
    ){
        image[r][c] = color;
        fill(image, r + 1, c, color, prev);
        fill(image, r - 1, c, color, prev);
        fill(image, r, c + 1, color, prev);
        fill(image, r, c - 1, color, prev);
    }
    
}
