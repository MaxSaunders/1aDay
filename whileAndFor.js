var myArray = []

var i = 0
while(i < 5){
    myArray.push(i)
    i++
} 

//console.log(myArray)

myArray = []

for (var i = 0; i < 5; i++){
    myArray.push(i)
}

//console.log(myArray)

var ourArray = []

for (var i = 1; i < 10; i += 2){ //only odd number
    ourArray.push(i)
}

console.log(ourArray)

ourArray = []

for (var i = 10; i > 0; i -= 2){ //even numbers backwards
    ourArray.push(i)
}

console.log(ourArray)