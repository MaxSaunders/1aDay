var ourDog = {
    'name': "Camper",
    'legs': 4,
    'tails': 1,
    'friends': ['everything']
}

var testObj = {
    'hat': 'ballcap',
    'shirt': 'jersey',
    'shoes': 'cleats'
}

var hatValue = testObj.hat
var shirtValue = testObj.shirt

console.log(hatValue)

var testObj2 = {
    'an entree': 'hamburger',
    'my side': 'veggies',
    'the drink': 'water'
}

var entreeValue = testObj2["an entree"]
console.log(entreeValue)

var testObj3 = {
    12: 'Namath',
    16: 'Montana',
    19: 'Unitas',
}

var playerNumber = 16
var player = testObj3[playerNumber]
console.log(player)


var myDog = {
    'name': "Max",
    'legs': 3,
    'tails': 2,
    'friends': []
}

myDog.name = 'Happy' //changing properties on an object

console.log(myDog.name)

myDog.bark = 'Bow-Wow' //adding properties to an object
myDog.color = "Brown"

console.log(myDog)

delete myDog.bark //delete a property

console.log(myDog)