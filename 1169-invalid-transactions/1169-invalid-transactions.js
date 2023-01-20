/**
 * @param {string[]} transactions
 * @return {string[]}
 */
var invalidTransactions = function(transactions) {

    transactions.sort((a,b)=>{
        return a.split(',')[1] - b.split(',')[1]
    });
    
    let res = new Set;
    for(let i=0;i<transactions.length;i++){
        const [n,t,a,c] = transactions[i].split(',');
        if(a>1000){
            res.add(i);
        }
        
        let j = i + 1;
        while(transactions[j]){
            const [n2,t2,a2,c2] = transactions[j].split(',');
            if( n===n2 && c!==c2 && t2-t <= 60){
                res.add(i);
                res.add(j);
            }
            j++;
        }
    }
    
    return transactions.filter((transaction,index) => {
        return res.has(index);
    });
};