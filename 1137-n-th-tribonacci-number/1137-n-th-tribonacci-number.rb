# @param {Integer} n
# @return {Integer}
def tribonacci(n)
    tribs = [0,1,1]
    i = 3
    while i <= n
        tribs << tribs[-1]+tribs[-2]+tribs[-3]
        i += 1
    end
    tribs[n]
end