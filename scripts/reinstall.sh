minikube stop
minikube delete
sudo rm -r ~/.kube ~/.minikube
sudo rm -rf /etc/kubernetes/
rm  -r ~/.helm
rm /usr/local/bin/helm
rm /usr/local/bin/fission

sleep 10s
minikube start
curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.7.0-darwin-amd64.tar.gz
tar xzf helm-v2.7.0-darwin-amd64.tar.gz
mv darwin-amd64/helm /usr/local/bin
helm init
sleep 60s 
helm install --namespace fission --set serviceType=NodePort https://github.com/fission/fission/releases/download/0.7.0/fission-all-0.7.0.tgz
curl -Lo fission https://github.com/fission/fission/releases/download/0.7.0/fission-cli-osx && chmod +x fission && sudo mv fission /usr/local/bin/
rm -r darwin-amd64
rm helm-v2.7.0-darwin-amd64.tar.gz

sleep 20s 
fission env create --name nodejs --image fission/node-env:0.7.0
curl -LO https://raw.githubusercontent.com/fission/fission/master/examples/nodejs/hello.js
fission function create --name hello --env nodejs --code hello.js
sleep 10s # Waiting for container start
fission function test --name hello
fission route create --function hello --url /hello
rm hello.js