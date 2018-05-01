var http = require('http');
var request = require('request')
// Redirect text:
//       http://localhost:8082/?request=dog.ceo/api/breeds/image/random

// Bash and run request. We need sync-calls to run jobs.
var exec = require('sync-exec')
var count = 0;
var rqueue = [];    // Store the requests.

function sort_requests(request_queue){
    // Request_queue: {"URL": frequency}
    request_queue.sort();
    res = {};
    for(i=0;i < request_queue.length; i++){
        if (request_queue[i] in res){
            res[request_queue[i]] += 1;
        }
        else{
            res[request_queue[i]] = 1;
        }
    }
    return res;
}

function make_requests(req_list, count){
    // Measurement the cost time.
    console.time('test');
    for (var key in req_list){
        cmd = "hey -c 10 -n " + req_list[key] + " " + key; 
        exec(cmd);
    }
    console.timeEnd('test');
}   

http.createServer(function (req, res) {
    
    if (req.url.slice(2,9) == "request"){
            count += 1;
            var replay = req.url.slice(10,);
            var newurl = 'https://' + replay;
            rqueue.push(newurl);
            if (count == 20) {
            // 100s requests
            rqueue = sort_requests(rqueue, count);
            console.log(rqueue);
            make_requests(rqueue);
            rqueue = [];
            count = 0
        }
    }
    res.writeHead(200, {'Context-Type': 'text/plain'})
    res.end("body");

}).listen(8082);
