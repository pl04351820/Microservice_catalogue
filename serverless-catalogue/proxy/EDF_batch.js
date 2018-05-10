var http = require('http');
var request = require('request')
var exec = require('sync-exec')

var count = 0;
var rqueue = [];    // Store the requests.

// Sort requests in order of deadline.
function sort_requests(request_queue){
    // Sort by deadline first.

    request_queue.sort();
    var dic = {};
    for(i=0;i < request_queue.length; i++){
        if (request_queue[i] in dic){
            dic[request_queue[i]] += 1;
        }
        else{
            dic[request_queue[i]] = 1;
        }
    }
    return dic;
}


