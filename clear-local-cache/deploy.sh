# This script deploys the cache test file.
fission env create --name nodejs --image fission/node-env:0.7.0 
fission env create --name nodejsnew --image fission/node-env:0.6.0 

# Two container
fission function create --env nodejs --name randomtag --code tag-page.js 
fission function create --env nodejsnew --name randomtagnew --code tag-page.js 

# One container
fission function create --env nodejs --name randomtag --code tag-page.js 
fission function create --env nodejs --name randomtagnew --code tag-page.js 

fission route create --url /randomtag --function randomtag 
fission route create --url /randomtagnew --function randomtagnew 