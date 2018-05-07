## Fission performance tests

| Testname      | Description   |
| ------------- |:-------------:| 
| bigJson       | 100kb json to clen the effect of caching | 
| clearLocalCache | Small random json to clean effect of caching|
| inOrderTest   | Schedule jobs in parallel and serilize order  |
| nodeBatch | Add proxy to improve serverless performance  | 
| separateCatalogue | Separate serverless into three components | 

<p>This tests directory records the roadmap to improve serverless performance.</p>
<p>All tests limit CPU core number as 1 for fission resource</P>

<h3>separateCatalogue:</h3>
<p>Separate whole catalogue service into three independent services and deploy it in same container or different container. </p>

<h3>inOderTest</h3>
<p>Measure the performance between serialized and parallel accessing.</p>

<h3>clearLocalCache</h3>
<p>Clear the effec of L2 cache by random rendering json file.</p>

<h3>bigJson</h3>
<p>Render 100kB json file to eliminate all cache effect.</p>
<p>Todo: Filesize that is larger than 512kB will be rejected by serverless platform service. Hack into fission to change max filesize.</p>

