var fs = require('fs');

module.exports = async function(context) {
    fs.writeFile("/tmp/test", "Hey there!", function(err) {
        if(err) {
            return console.log(err);
        }
        console.log("The file was saved!");

        fs.readFile('/tmp/test', 'utf8', function(err, contents) {
            console.log(contents);
            return {
                status: 200,
                body: contents
            }
        });
    }); 

}