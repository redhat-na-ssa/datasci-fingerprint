Getting started
===============

From your terminal/bastion

```
# SSH to your cluster node with cluster-admin
oc login --token=sha256~<your_token>

# clone this repo for the bootstrap scripts
git clone https://github.com/redhat-na-ssa/datasci-fingerprint.git
cd datasci-fingerprint/

# run bootstrap to provision the demo on your cluster
./setup.sh

# optionally, you can `source ./scripts/bootstrap.sh` and run commands individually, i.e.
setup_demo
delete_demo
```

