/**
 * @param {string} s
 * @return {boolean}
 */
var checkRecord = function(s) {
    let absences = 0;
    let lates = 0;
    for(let day of s){
        if(day==='L'){
            lates++;
            if(lates===3) return false;
        } else {
            lates = 0;
            if(day==='A') absences++;
        }
    }
    return absences<2
};