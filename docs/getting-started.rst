Getting started
===============

From your terminal/bastion

```
# SSH to your cluster node with cluster-admin
oc login --token=sha256~<your_token>

# clone this repo for the bootstrap scripts
git clone https://github.com/redhat-na-ssa/demo-rosa-sagemaker.git
cd demo-rosa-sagemaker/

# run bootstrap to provision the demo on your cluster
./scripts/bootstrap.sh

# optionally, you can `source ./scripts/bootstrap.sh` and run commands individually, i.e.
setup_demo
delete_demo
```

