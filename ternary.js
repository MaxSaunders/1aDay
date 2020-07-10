function checkSign(num){
    return num < 0 ? "negative": num > 0 ? "positive": "Zero" 
}

console.log(checkSign(-1))

console.log(checkSign(2))

console.log(checkSign(0))