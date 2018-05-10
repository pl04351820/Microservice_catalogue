module.exports = {

sortByDeadline: function(reqList){
    reqList.sort(function compare(kv1, kv2){
        return kv1["deadline"] - kv2["deadline"]; 
    })
    
    outList = {};
    reqList.forEach(function(req){
        if (req["url"] in outList){
            outList[req["url"]] += 1;
        }
        else{
            outList[req["url"]] = 1;
        }
    })
    return outList;
},

sortByArrive: function(reqList){
    outList = {};
    reqList.forEach(function(req){
        if (req["url"] in outList){
            outList[req["url"]] += 1;
        }
        else{
            outList[req["url"]] = 1;
        }
    })
    return outList;
},


sortByPriority: function(reqList){
    outList = {};
    reqList.sort(function compare(kv1, kv2){
        return kv2["priority"] - kv1["priority"]
    })
    reqList.forEach(function(req){
        if (req["url"] in outList){
            outList[req["url"]] += 1;
        }
        else{
            outList[req["url"]] = 1;
        }
    })
    return outList;
}

};