minikube start
curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.7.0-darwin-amd64.tar.gz
tar xzf helm-v2.7.0-darwin-amd64.tar.gz
mv darwin-amd64/helm /usr/local/bin
helm init
sleep 60s 
helm install --namespace fission --set serviceType=NodePort https://github.com/fission/fission/releases/download/0.7.2/fission-all-0.7.2.tgz
curl -Lo fission https://github.com/fission/fission/releases/download/0.7.2/fission-cli-osx && chmod +x fission && sudo mv fission /usr/local/bin/
rm -r darwin-amd64
rm helm-v2.7.0-darwin-amd64.tar.gz
