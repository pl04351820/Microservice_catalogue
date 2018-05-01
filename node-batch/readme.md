### Batch requests
According to tests, the interlevaing between containers or function inside same container will improve the costs. To accelerate this process, we use batch technology to handle requests.

#### Package install
```
$ npm install sync-exec
$ npm install hey
```

#### Testing command line
The command requests can be write in following format, url did not include http:
http://localhost:8082/?request=<url>
```
$ hey -c 10 -n 20 http://localhost:8082/?request=dog.ceo/api/breeds/image/random
```

