/*
This file includes the backend for the AeroThon website

The below code communicates with the "physics_simualtion.py" file
*/

const {PythonShell} = require('python-shell');

var condition = "False";

let options = {
    args:["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", condition, "RTA3"]
};

PythonShell.run("../Python Backend\\base_data.py", options).then(results=>{
    
    var refList = options.args.slice(0, -2);
    var newList = [];

    for (var i = 0; i<results.length; i++){
        if ("False" == condition){
            if (i <= 1){
                continue;
            }else{
                console.log(results[i].slice(20, 25));
                newList.push(results[i].slice(20, 25));
            }
        }else{
            console.log(results[i]);
        }
    }
    if (newList.toString() == refList.toString()){
        console.log("LIST CHECK \u001b[32mOK\u001b[37m");
    }else{
        console.log("LIST CHECK \u001b[31mFAILED\u001b[37m");
        console.log(newList);
        console.log(refList);
    }
});