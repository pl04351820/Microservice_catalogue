# This will make the fission system crash

fission env create --name nodefrontpage --image fission/node-env:0.7.0
sleep 10s
fission env create --name sizepage --image fission/node-env:0.7.0
sleep 10s
fission env create --name tagpage --image fission/node-env:0.7.0
sleep 10s

# Try to make it in the same container. more than 3 containers will make the system crash based on my test.

# fission env create --name nodefrontpage --image fission/node-env:0.7.0 
# fission env create --name sizepage --image fission/node-env:0.7.0 --poolsize 2
# fission env create --name tagpage --image fission/node-env:0.7.0 --poolsize 2 

# fission fn create --name hello --code hello.js --env node --minscale 1 --maxscale 5  --executortype newdeploy


# fission function create --name frontpage --env nodefrontpage --code front-page.js --maxscale 1
# fission function create --name sizepage --env nodesize --code size-page.js --maxscale 1
# fission function create --name tagpage --env nodetag --code tag-page.js --maxscale 1

fission function create --name frontpage --env nodejs --code front-page.js --maxscale 1
fission function create --name sizepage --env nodejs --code size-page.js --maxscale 1
fission function create --name tagpage --env nodejs --code tag-page.js --maxscale 1


fission route create --function frontpage --url /frontpage
fission route create --function sizepage --url /sizepage
fission route create --function tagpage --url /tagpage

