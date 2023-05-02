/*
This file includes the backend for the AeroThon website

The below code communicates with several python files
*/

const {PythonShell} = require('python-shell');

function baseData(baseCondition) {
    var baseInfoCondition = baseCondition;

    let options = {
        args:["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", baseInfoCondition, "RTA3"]
    };

    PythonShell.run("../Python Backend/base_data.py", options).then(results=>{
        for(i=0; i<results.length; i++){
            if(i == "False"){
                console.log("TYPECHECKING FAILED")
            }else{
                console.log("\x1b[42mTYPECHECKING PASSED\x1b[0m")
                return 0;
            }
        }
    });
}

baseData("False")


