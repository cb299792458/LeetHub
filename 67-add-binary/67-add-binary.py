class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        def a_digit(i):
            a_start = len(a)-1
            if(a_start-i<0):
                return False
            return a[a_start-i] == '1'
        
        def b_digit(i):
            b_start = len(b)-1
            if(b_start-i<0):
                return False
            return b[b_start-i] == '1'
        
        
        res = ''
        carry = 0
        for i in range( 1 + max(len(a),len(b)) ):

            if(a_digit(i)):
                carry += 1
            if(b_digit(i)):
                carry += 1
                
            if(carry%2 == 1):
                res = '1' + res
            else:
                res = '0' + res
            
            if(carry>1):
                carry = 1
            else:
                carry = 0
            
        if(res[0]=='0'):
            res = res[1:]
        return res