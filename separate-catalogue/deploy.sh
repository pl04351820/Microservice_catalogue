fission function create --name frontpage --env nodejs --code front-page.js
fission function create --name sizepage --env nodejs --code size-page.js
fission function create --name tagpage --env nodejs --code tag-page.js

fission route create --function frontpage --url /frontpage
fission route create --function sizepage --url /sizepage
fission route create --function tagpage --url /tagpage