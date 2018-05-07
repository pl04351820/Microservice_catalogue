fission env create --name nodejs --image fission/node-env:0.7.0 

fission function create --name hello --env nodejs --code hello.js --maxscale 1
fission function create --name hello --env nodejs --code hello.js --maxscale 1

# fission function test --name hello

