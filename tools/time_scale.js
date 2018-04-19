// This code shows how to use time in fission serverless function.

module.exports = async function(context) {
    var d = new Date(); // Show current time
    await sleep(200);   // Delay request
    console.log("work");
        return {
            status: 200,
            body: d,
            headers: {
                'Foo': 'Bar'
            }
        }
}