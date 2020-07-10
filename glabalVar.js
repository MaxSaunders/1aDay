var myGlobal = 10;

function fun1(){
    oopsGlobal = 5 //because we didn't use "var" this variable becomes global
}

function fun2(){
    var output = "";
    if (typeof myGlobal != "undefined"){
        output += "myGlobal: " + myGlobal + "\n";
    }
    if (typeof oopsGlobal != "undefined"){
        output += "oopsGlobal: " + oopsGlobal + "\n";
    }
    console.log(output);
}

fun1()
fun2()