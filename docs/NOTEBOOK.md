# A collections of hacks

## Make all CUDA based GPUs work with a RHODS notebook

Imperative `oc` commands

```
# new project
oc new-project standalone-notebooks \
  --description "A collection of standalone jupyter notebooks" \
  --display-name "Standalone Jupyter Notebooks"

# setup gpu-notebook container
CONTAINER_IMAGE="quay.io/modh/cuda-notebooks:cuda-jupyter-tensorflow-ubi9-python-3.9"
APP_NAME=gpu-notebook
APP_LABEL="app.kubernetes.io/part-of=${APP_NAME}"

oc new-app \
  "${CONTAINER_IMAGE}" \
  --name "${APP_NAME}" \
  -l "${APP_LABEL}"

# setup env vars for gpu-notebook
oc set env \
  "deployment/${APP_NAME}" \
  -e NOTEBOOK_PORT="8080" \
  -e JUPYTER_TOKEN="thisisfine"

# create service
# oc expose deployment \
#  "${APP_NAME}" \
#  --port 8080 \
#  -l "${APP_LABEL}"

# create route
oc expose service \
  "${APP_NAME}" \
  --overrides='{"spec":{"tls":{"termination":"edge"}}}' \
  -l "${APP_LABEL}"

oc get route "${APP_NAME}" -o jsonpath='{"https://"}{.status.ingress[0].host}{"\n"}'
```

```
# make gpu-notebook media persistent
oc set volume \
  "deployment/${APP_NAME}" \
  --add \
  --name="${APP_NAME}"-media \
  --mount-path=/opt/app-root/src \
  -t pvc \
  --claim-size=5G \
  --overwrite
```

```
# run on nvidia gpu nodes
oc patch "deployment/${APP_NAME}" \
  -p '{"spec": {"template": {"spec": {"nodeSelector": {"nvidia.com/gpu.present": "true"}}}}}'
```
