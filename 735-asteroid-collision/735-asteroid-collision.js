var asteroidCollision = function(asteroids) {
    let stack = [asteroids[0]]
    for (let i = 1; i < asteroids.length; i++) {
        stack.push(asteroids[i])
        while (stack.length >= 2 && stack[stack.length-1] < 0 && stack[stack.length-2] > 0 ) {
            let ast1 = stack.pop()
            let ast2 = stack.pop()
            if (Math.abs(ast1) > Math.abs(ast2)) {
                stack.push(ast1)
            } else if (Math.abs(ast1) < Math.abs(ast2)) {
                stack.push(ast2)
            }
        }
    }
    return stack
};