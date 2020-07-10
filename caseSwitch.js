function caseInSwitch(x){
    switch(x){
        case 1:
            return 'alpha'
            break;
        case 2:
            return 'beta'
        case 3:
            return 'gamma'
        case 4:
            return 'delta'
        case 5:
        case 6:
        default:
            return 'Try Again'
    }
}

console.log(caseInSwitch(1))
console.log(caseInSwitch(4))
console.log(caseInSwitch(5))
console.log(caseInSwitch(9))