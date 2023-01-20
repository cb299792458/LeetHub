/**
 * @param {string[]} transactions
 * @return {string[]}
 */
var invalidTransactions = function(transactions) {

    transactions.sort((a,b)=>{ // Sort by time
        return a.split(',')[1] - b.split(',')[1]
    });
    
    let res = new Set;
    for(let i=0;i<transactions.length;i++){ // check each transaction
        const [n,t,a,c] = transactions[i].split(',');
        if(a>1000){ // check for amount
            res.add(i);
        }
        
        let j = i + 1;
        while(transactions[j]){ // check for diff country
            const [n2,t2,a2,c2] = transactions[j].split(',');
            if( n===n2 && c!==c2 && t2-t <= 60){
                res.add(i);
                res.add(j);
            }
            j++;
        }
    }
    
    // Use set of indices to avoid repeat
    return transactions.filter( (transaction,index) => res.has(index) )

};