/**
 * @param {string[][]} accounts
 * @return {string[][]}
 */
var accountsMerge = function(accounts) {
    const owners = {};
    const emails = [];
    
    for(let i in accounts){
        emails[i] = []
        for(let j=1;j<accounts[i].length;j++){
            let email = accounts[i][j];
            if(!owners[email]) owners[email] = [];
            owners[email].push(i);
            emails[i].push(email);
        }
    }
    
    let seen = new Set;
    let mergedAccounts = [];
    
    for(let i in accounts){
        if(seen.has(i)) continue;
        
        // let userEmails = new Set;
        // let stack = [i];
        // while(stack.length){
        //     let current = stack.pop();
        //     if(seen.has(current)) continue;
        //     seen.add(current);
        //     for(let email of emails[current]){
        //         userEmails.add(email);
        //         stack = stack.concat(owners[email]);
        //     }
        // }
        
        let name = accounts[i].shift();
        let userEmails = new Set(accounts[i]);
        userEmails.forEach((email)=>{
            for(let owner of owners[email]){
                seen.add(owner)
                for(let email2 of emails[owner]){
                    userEmails.add(email2);
                }
            }
        });
        
        
        let emailArray = Array.from(userEmails);
        emailArray.sort((a,b)=>{
            if(a<b) return -1;
            return 1;
        });
        
        mergedAccounts.push([name,...emailArray]);
    }
    return mergedAccounts;
};