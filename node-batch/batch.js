var http = require('http');
var request = require('request')
// Redirect text:
//       http://localhost:8082/?request=dog.ceo/api/breeds/image/random

// Problem -> node mode is single thread, so it cannot handle async model easily.

var count = 0;
var rqueue = [];
http.createServer(function (req, res) {
    if (req.url.slice(2,9) == "request"){
            count += 1;
            console.log(count);
            var replay = req.url.slice(10,);
            var newurl = 'https://' + replay;
            rqueue.push(newurl);
                if (count == 3) {
                    // 100s requests
                    console.log(rqueue[0])
                    count -= 1;
                    for(var i=0; i<3; i++){
                        request(rqueue[i], function(error, response, body){
                            res.writeHead(200, {'Content-Type': 'text/plain'});
                            res.end(body);
                        })}
                        rqueue = [];
                    console.log("out")
                    }
        }
}).listen(8082);
