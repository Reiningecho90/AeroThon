/*
This file includes the backend for the AeroThon website

The below code communicates with the "physics_simualtion.py" file
*/

const {PythonShell} = require('python-shell');



let options = {
    args:["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "True", "RTA3"]
};

PythonShell.run("../Python Backend\\base_data.py", options).then(results=>{
    for (var i = 0; i<results.length; i++){
        console.log(results[i]);
    }
});