class Twitter{
    constructor(){
        this.tweets = [];
        this.followers = {};
    }
    
    postTweet(userId, tweetId){
        this.tweets.unshift({userId: userId, tweetId: tweetId});
    }
    
    getNewsFeed(userId){
        let ans = [];
        if(!this.followers[userId]) this.followers[userId] = new Set;

        for(let tweet of this.tweets){
            if(ans.length===10) break;
            if(userId===tweet.userId || this.followers[userId].has(tweet.userId)){
                ans.push(tweet.tweetId);
            }
        }
        return ans;
    }
    
    follow(follower,followee){
        if(!this.followers[follower]) this.followers[follower] = new Set;
        this.followers[follower].add(followee);
    }
    
    unfollow(follower,followee){
        if(!this.followers[follower]) this.followers[follower] = new Set;
        this.followers[follower].delete(followee);
    }
}