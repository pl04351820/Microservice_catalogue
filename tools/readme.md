### Useful program 

| ToolName      | Description   |        
| ------------- |:-------------:| 
| accessTempDir | Access container local fs| 
| helloTest   | Demo test file to check if fission install correctly  |
| httpRequest | Send http request using native environment  | 
| namespaceAccess | Invoke another fission function | 
| timeScale | Acquire timestamp |
| triggle | Triggle fission functions in serilized order|

```
$ fission function create --env nodejs --name accessTempDir --code accessTempDir.js
$ fission function create --env nodejs --name helloTest --code helloTest.js
$ fission function create --env nodejs --name httpRequest --code httpRequest.js
$ fission function create --env nodejs --name namespaceAccess --code namespaceAccess.js
$ fission function create --env nodejs --name timeScale --code timeScale.js
```