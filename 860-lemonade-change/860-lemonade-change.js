/**
 * @param {number[]} bills
 * @return {boolean}
 */
var lemonadeChange = function(bills) {
    let fives = 0;
    let tens = 0;
    
    for(let bill of bills){
        if(bill===5) fives++;
        if(bill===10){
            if(!fives) return false;
            fives --;
            tens ++;
        }
        if(bill===20){
            if(tens){
                tens--;
            
                if(!fives) return false;
                fives --;
            } else {
                if(fives<3) return false;
                fives += -3;
            }
        }
        
    }
    return true;
};