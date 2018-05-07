'use strict';
// Please use request-promise-native package to update.
const rp = require('request-promise-native');

module.exports = async function (context) {
    try {
        // Blocking http request.
        const response = await rp(`http://router.fission/hello`);
        const condition = JSON.parse(response);
        return {
            status: 200,
            body: {
                text: `this works to access API`
            },
            headers: {
                'Content-Type': 'application/json'
            }
        };
    } catch (e) {
        console.error(e);
        return {
            status: 500,
            body: e
        };
    }
}