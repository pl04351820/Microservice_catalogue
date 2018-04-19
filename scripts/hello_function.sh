fission env create --name nodejs --image fission/node-env:0.7.0
curl -LO https://raw.githubusercontent.com/fission/fission/master/examples/nodejs/hello.js
fission function create --name hello --env nodejs --code hello.js
sleep 10s
fission function test --name hello
fission route create --function hello --url /hello