# fission workflow
helm repo add fission-charts https://fission.github.io/fission-charts/
helm repo update
helm install --wait -n fission-workflows fission-charts/fission-workflows --version 0.2.0