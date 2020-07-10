function golfScore(par, strokes){
    if (strokes == 1){
        return 'Hole-in-One!'
    }else if(strokes <= par - 2){
        return 'Eagle'
    }else if(strokes == par - 2){
        return 'Birdie'
    }else if(strokes == par){
        return 'Par'
    }else if(strokes == par + 1){
        return 'Bogey'
    }else if(strokes == par + 2){
        return 'Double Bogey'
    }else if(strokes >= par + 3){
        return 'Go Home!'
    }
}

console.log(golfScore(5, 3))
console.log(golfScore(6, 10))
console.log(golfScore(4, 1))

var names = ["Hole-in-One!", 'Eagle', 'Birdie', 'Par', "Bogey", "Double Bogey", "Go Home!!"]
function golfScore2(par, strokes){
    if (strokes == 1){
        return names[0]
    }else if(strokes <= par - 2){
        return names[1]
    }else if(strokes == par - 2){
        return names[2]
    }else if(strokes == par){
        return names[3]
    }else if(strokes == par + 1){
        return names[4]
    }else if(strokes == par + 2){
        return names[5]
    }else if(strokes >= par + 3){
        return names[6]
    }
}

console.log(golfScore2(5, 3))
console.log(golfScore2(6, 10))
console.log(golfScore2(4, 1))