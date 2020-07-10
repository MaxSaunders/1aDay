function greaterThan(val){
    if (val > 100){
        return 'Over 100'
    }
    if (val > 10){
        return 'Over 10'
    }
    return '10 or Under'
}

console.log(greaterThan(10))

function greaterOrEqual(val){
    if (val >= 100){
        return '100 or over'
    }
    if (val >= 10){
        return '10 or over'
    }
    return 'Under 10'
}

console.log(greaterOrEqual(22))

function testAnd(x){
    if (x >= 50 && x <= 100){
        return 'Between 50 and 100'
    }
    return 'Not between'
}

console.log(testAnd(60))
console.log(testAnd(22))

function testOr(x){
    if (x < 10 || x > 20){
        return 'outside'
    }return 'inside'
}

console.log(testOr(30))
console.log(testOr(15))