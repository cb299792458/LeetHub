var topKFrequent = function(words, k) {
    let objectCounts = {};
    let wordSet = new Set();
    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        wordSet.add(word);
        if (!objectCounts[word]) {
            objectCounts[word] = 0;
        }
        objectCounts[word]++;
    };
    let wordArray = Array.from(wordSet);
    wordArray.sort((a, b) => {
        if (objectCounts[a] > objectCounts[b]) {
            return -1;
        } else if (objectCounts[a] < objectCounts[b]) {
            return 1;
        } else if (a < b) {
            return -1;
        } else {
            return 1;
        }
    })
    // console.log(objectCounts, 'set:', wordSet, 'array:', wordArray)
    return wordArray.slice(0, k);
};