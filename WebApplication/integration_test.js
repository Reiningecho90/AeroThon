/*
This file includes the backend for the AeroThon website

The below code communicates with several python files
*/

import {PythonShell} from 'python-shell';

function baseData(argus){
    let options = {
        args: argus
    };

    document.getElementById("opt").innerText = "Running Check...";
    PythonShell.run("../PythonBackend/base_data.py", options).then(results=>{
        console.log(resultingData)
        console.log("Hello")
    });
    
    document.getElementById("opt").innerText = "TCF";
}
