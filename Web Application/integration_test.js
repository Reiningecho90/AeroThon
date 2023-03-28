/*
This file includes the backend for the AeroThon website

The below code communicates with the "physics_simualtion.py" file
*/

const {PythonShell} = require('python-shell');

var testData = [];

PythonShell.run('Web Application\\base_data.py', function(err, results){
    if (err) throw err;
    console.log(results);
    console.log('Done');
});