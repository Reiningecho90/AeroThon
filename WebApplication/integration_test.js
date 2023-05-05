/*
This file includes the backend for the AeroThon website

The below code communicates with several python files
*/

const {PythonShell} = require('python-shell');
const stabCalc = document.getElementById('calcstab');

var shell;

function startShell(scriptname){
    document.getElementById("opt").innerText = "Starting Shell";
    shell = PythonShell(`../PythonBackend/${scriptname}.py/`);
    document.getElementById("opt").innerText = "SHELL ON";
}

function baseData(argus){

    let options = {
        args: argus
    };

    document.getElementById("opt").innerText = "Running Check...";
    shell.run("../PythonBackend/base_data.py", options).then(results=>{
        console.log(resultingData)
        console.log("Hello")
    });
    
    document.getElementById("opt").innerText = "TCF";
}


stabCalc.addEventListener('click', function(argus){
    var return_data = [];

    let options = {
        args: argus
    };

    PythonShell.run("../PythonBackend/calc_stab.py", options).then(results=>{
        for(var i=0; i<results.length; i++){
            return_data.append(results[i]);
        }
        
    });
    document.getElementById("opt").innerText = "hello";
});


