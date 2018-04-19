curl https://raw.githubusercontent.com/fission/fission-workflows/0.2.0/examples/whales/fortune.sh > fortune.sh
curl https://raw.githubusercontent.com/fission/fission-workflows/0.2.0/examples/whales/whalesay.sh > whalesay.sh
curl https://raw.githubusercontent.com/fission/fission-workflows/0.2.0/examples/whales/fortunewhale.wf.yaml > fortunewhale.wf.yaml

fission env create --name binary --image fission/binary-env
fission function create --name whalesay --env binary --deploy ./whalesay.sh
fission function create --name fortune --env binary --deploy ./fortune.sh

fission function create --name fortunewhale --env workflow --src ./fortunewhale.wf.yaml
fission route create --method GET --url /fortunewhale --function fortunewhale
