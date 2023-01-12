/**
 * @param {string} homepage
 */
var BrowserHistory = function(homepage) {
    this.history = [homepage]
    this.currentPage = 0
};
/** 
 * @param {string} url
 * @return {void}
 */
BrowserHistory.prototype.visit = function(url) {
    this.history = this.history.slice(0, this.currentPage+1)
    this.history.push(url)
    this.currentPage ++
};
/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.back = function(steps) {
    if(this.currentPage >= steps){
        this.currentPage -= steps
    }else {
        this.currentPage = 0
    }
    return this.history[this.currentPage]
    
};
/** 
 * @param {number} steps
 * @return {string}
 */
BrowserHistory.prototype.forward = function(steps) {
    if(this.history.length > steps + this.currentPage){
        this.currentPage += steps
    }else {
        this.currentPage = this.history.length -1
    }
    return this.history[this.currentPage]
};