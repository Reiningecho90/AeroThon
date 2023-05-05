/*
This file includes the backend for the AeroThon website

The below code communicates with several python files
*/

const {PythonShell} = require('python-shell');

function baseData(argus){

    alert('Base Start');

    let options = {
        args: argus
    };
    
    PythonShell.run("../Python Backend/base_data.py", options, function(err, results){
        if(err){
            console.log("ERROR");
        } else{
            for(i=0; i<results.length; i++){
                if(i == "False"){
                    console.log("TYPECHECKING FAILED");
                }else{
                    console.log("\x1b[42mTYPECHECKING PASSED\x1b[0m");
                    return 0;
                }
        }
        console.log(results);
        }
    });
    console.log("HERE");
    document.getElementById("opt").innerText = "hello";
}


function calculateStability(argus){
    var return_data = [];
    alert("STARTING");

    let options = {
        args: argus
    };

    PythonShell.run("../Python Backend/calc_stab.py", options).then(results=>{
        alert("YES");
        for(var i=0; i<results.length; i++){
            return_data.append(results[i]);
            alert("HELLO");
        }
        document.getElementById("opt").innerText = "hello";
    });
    return return_data;
}

baseData([1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]);
