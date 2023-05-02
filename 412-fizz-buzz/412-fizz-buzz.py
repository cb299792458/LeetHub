class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res=[]
        for i in range(1,n+1):
            fb=''
            if i%3==0: fb+='Fizz'
            if i%5==0: fb+='Buzz'
            res.append(fb or str(i))
        return res