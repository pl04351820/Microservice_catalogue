module.exports = async function(context) {
    return {
        status: 200,
        body: JSON.stringify({"tags":["brown","geek","formal","blue","skin","red","action","sport","black","magic","green"],"err":null})
    };
}