## Migrate microservice architecture to serverless architecture based on Fission.
Environment: OS X <br>
Fission: 0.7.1 <br>
Kubernete: Minikube v0.26.0 <br>

## Start service
Check front-end/helper/index.js and replace fission port number with your native configuration.

```
$ fission function create --name serverless-catalogue --code /serverless-catalogue/native/serverless-catalogue.js
$ fission route create --url /serverless-catalogue --function serverless-catalogue
$ cd front-end
$ npm install && npm start
$ cd ../microservice-catalogue
$ docker-compose up
```

## Install guidance
#### Install Virtual box:
https://www.virtualbox.org/wiki/Downloads

#### Install Kubectl:
```
$ brew install kubectl
```

#### Install Minikube:
```
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.26.0/minikube-darwin-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

#### Install Fission
```
$ minikube start
$ curl -LO https://storage.googleapis.com/kubernetes-helm/helm-v2.7.0-darwin-amd64.tar.gz
$ tar xzf helm-v2.7.0-darwin-amd64.tar.gz
$ mv darwin-amd64/helm /usr/local/bin
$ helm init
$ helm install --namespace fission --set serviceType=NodePort https://github.com/fission/fission/releases/download/0.7.1/fission-all-0.7.1.tgz
$ curl -Lo fission https://github.com/fission/fission/releases/download/0.7.1/fission-cli-osx && chmod +x fission && sudo mv fission /usr/local/bin/
```

#### Demo test 
```
$ fission env create --name nodejs --image fission/node-env
$ curl https://raw.githubusercontent.com/fission/fission/master/examples/nodejs/hello.js > hello.js
$ fission function create --name hello --env nodejs --code hello.js
$ fission route create --method GET --url /hello --function hello
$ fission function test --name hello
```

## Pipeline 

## Scheduler and workflow 

## Scripts
Some workflow to improve efficiency. 

## Useful fission command line:
#### list all fission function and route deployment
```
$ fission function list
$ fission route list
```

#### Test fission function 
```
$ fission function test --name <function-name>
```

#### Check function logs
```
$ fission function logs --name <function-name>
```

## Useful kubenetes command line:
#### Check namesapces
```
$ kubectl get namespaces
```

#### Chcek kubernete system management
```
$ kubectl get pods -n kube-system
```

#### Check helm deploy
```
$ helm list
```

#### Check fission function deploy
```
$ kubectl get pods -n fission-function
``` 

#### Check fission deployment
```
$ kubectl get svc -n fission
```

## Useful docker command line:
#### Stop all docker container
```
$ docker stop (docker ps -aq)
```

#### Remove all docker container
```
$ docker rmi (docker images -aq)
```

## Other useful command line:
#### Check port usage
```
$ sudo lsof -i:80
```

#### Check cpu usage
```
$ top
```