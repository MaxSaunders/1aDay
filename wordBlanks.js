function wordBlanks(noun, adj, verb, adverb){
    var result = "";
    result += "The " + adj + " " + noun + " " + verb + " to the store " + adverb

    return result;
}

console.log(wordBlanks("dog", "big", "ran", "quickly"));
console.log(wordBlanks("cat", "small", "pranced", "slowly"));