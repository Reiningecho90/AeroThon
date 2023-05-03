/*
This file includes the backend for the AeroThon website

The below code communicates with several python files
*/

const {PythonShell} = require('python-shell');

function baseData(baseCondition, argus) {
    var baseInfoCondition = baseCondition;

    let options = {
        args: argus
    };

    PythonShell.run("../Python Backend/base_data.py", options).then(results=>{
        for(i=0; i<results.length; i++){
            if(i == "False"){
                console.log("TYPECHECKING FAILED");
            }else{
                console.log("\x1b[42mTYPECHECKING PASSED\x1b[0m");
                return 0;
            }
        }
    });
}


function calculateStability(argus){
    var return_data = [];

    let options = {
        args: argus
    };

    PythonShell.run("../Python Backend/calc_stab.py", options).then(results=>{
        for(var i=0; i<results.length; i++){
            return_data.append(results[i]);
        }
    })

    return return_data;
}

baseData("False", ["1.0", "2.0", "3.0", "4.0", "5.0", "6.0"]);
calculateStability(["1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0"])

