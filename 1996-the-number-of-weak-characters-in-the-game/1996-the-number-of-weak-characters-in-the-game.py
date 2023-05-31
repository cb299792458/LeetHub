class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        res=0
        properties.sort(key=lambda x:(-x[0],x[1]))

        lowest = properties[0][1]
        for char in properties:
            if char[1]<lowest:
                res+=1
            else: lowest = char[1]
        return res  