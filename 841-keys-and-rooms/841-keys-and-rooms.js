/**
 * @param {number[][]} rooms
 * @return {boolean}
 */
var canVisitAllRooms = function(rooms) {
    let visitedRooms = new Set;
    
    
    const explore = (roomId) => {
        if(!visitedRooms.has(roomId)){
            visitedRooms.add(roomId);
            rooms[roomId].forEach((keyId)=>{
                explore(keyId);
            });
        }
    };
    
    explore(0);
    
    return visitedRooms.size === rooms.length;
};