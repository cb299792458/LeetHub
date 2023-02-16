/**
 * @param {number} n
 * @param {number[][]} preferences
 * @param {number[][]} pairs
 * @return {number}
 */
var unhappyFriends = function(n, preferences, pairs) {
    
    function makePreferredPartners(){
        let preferredPartners = [];
        
        for(let [a,b] of pairs){
            preferredPartners[a] = ( preferences[a].slice(0,preferences[a].indexOf(b)) )  
            preferredPartners[b] = ( preferences[b].slice(0,preferences[b].indexOf(a)) )  
        }
        return preferredPartners;
    }
    console.log("preferred partners: ", makePreferredPartners())
    let preferredPartners = makePreferredPartners();
    
    let count = 0;
    for(let first=0;first<n;first++){
        if(!preferredPartners[first].length) continue;
        for(let second of preferredPartners[first]){
            if(preferredPartners[second].includes(first)){
                count++;
                break;
            }
        }
    }
    return count;
    
    
    // preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    // pairs = [[0, 1], [2, 3]]
    // 0=Ann, 1=Bob, 2=Cody, 3=Dan
    
    
/* for loop through each person i
        preferences[1] = [3,2,0] 
        Bob likes Dan, then Cody, then Ann
        But Bob is paired with Ann
            check every preference after their pair
            check Dan and Cody
                Dan likes Bob, then Cody, then Ann
                Dan's partner is Cody
                
    
        if any preference after their pair prefers them to their partner, they are unhappy
        Bob and Dan are unhappy because: 
        Bob likes Dan more than he likes Ann and 
        Dan likes Bob more than he likes Cody
        
        Another idea:
        make a graph of "preferred partners"
        graph[a] = [ everyone that person a likes more than their partner]
          0   1   2   3
        [[ ],[3],[ ],[1]]
        
        go through, check if two people have each other in their preferred partners
        
*/
};





