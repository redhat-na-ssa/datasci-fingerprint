from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.contrib.kubernetes.volume_mount import VolumeMount
from airflow.contrib.kubernetes.volume import Volume
from airflow.kubernetes.secret import Secret
from airflow import DAG
from airflow.utils.dates import days_ago

args = {
    "project_id": "fingerprint-left-right-0519234554",
}

dag = DAG(
    "fingerprint-left-right-0519234554",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="""
Created with Elyra 3.15.0 pipeline editor using `fingerprint-left-right.pipeline`.
    """,
    is_paused_upon_creation=False,
)


# Operator source: datasci-fingerprint/notebooks/1.0-setup.ipynb

op_1354b68c_2663_4ff0_bf01_04707283b05b = KubernetesPodOperator(
    name="1",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fingerprint-left-right' --cos-endpoint http://minio.airflow.svc.cluster.local:9000 --cos-bucket fingerprint-left-right --cos-directory 'fingerprint-left-right-0519234554' --cos-dependencies-archive '1.0-setup-1354b68c-2663-4ff0-bf01-04707283b05b.tar.gz' --file 'datasci-fingerprint/notebooks/1.0-setup.ipynb' "
    ],
    task_id="1",
    env_vars={
        "AWS_S3_BUCKET": "fingerprint-left-right",
        "AWS_S3_ENDPOINT": "minio.airflow.svc.cluster.local:9000",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fingerprint-left-right-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_1354b68c_2663_4ff0_bf01_04707283b05b.image_pull_policy = "Always"


# Operator source: datasci-fingerprint/notebooks/3.0-image-crop-left.ipynb

op_cf96ee47_0088_452c_96d6_ac1a7511cf92 = KubernetesPodOperator(
    name="3",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fingerprint-left-right' --cos-endpoint http://minio.airflow.svc.cluster.local:9000 --cos-bucket fingerprint-left-right --cos-directory 'fingerprint-left-right-0519234554' --cos-dependencies-archive '3.0-image-crop-left-cf96ee47-0088-452c-96d6-ac1a7511cf92.tar.gz' --file 'datasci-fingerprint/notebooks/3.0-image-crop-left.ipynb' "
    ],
    task_id="3",
    env_vars={
        "AWS_S3_ENDPOINT": "minio.airflow.svc.cluster.local:9000",
        "AWS_S3_BUCKET": "fingerprint-left-right",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fingerprint-left-right-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_cf96ee47_0088_452c_96d6_ac1a7511cf92.image_pull_policy = "Always"

op_cf96ee47_0088_452c_96d6_ac1a7511cf92 << op_1354b68c_2663_4ff0_bf01_04707283b05b


# Operator source: datasci-fingerprint/notebooks/3.0-image-crop-right.ipynb

op_9f3093dd_1f4b_4e71_9040_3a9bcbbda435 = KubernetesPodOperator(
    name="3_1",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fingerprint-left-right' --cos-endpoint http://minio.airflow.svc.cluster.local:9000 --cos-bucket fingerprint-left-right --cos-directory 'fingerprint-left-right-0519234554' --cos-dependencies-archive '3.0-image-crop-right-9f3093dd-1f4b-4e71-9040-3a9bcbbda435.tar.gz' --file 'datasci-fingerprint/notebooks/3.0-image-crop-right.ipynb' "
    ],
    task_id="3_1",
    env_vars={
        "AWS_S3_ENDPOINT": "minio.airflow.svc.cluster.local:9000",
        "AWS_S3_BUCKET": "fingerprint-left-right",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fingerprint-left-right-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_9f3093dd_1f4b_4e71_9040_3a9bcbbda435.image_pull_policy = "Always"

op_9f3093dd_1f4b_4e71_9040_3a9bcbbda435 << op_1354b68c_2663_4ff0_bf01_04707283b05b


# Operator source: datasci-fingerprint/notebooks/4.0-dataset-create.ipynb

op_4391fca7_53f7_4ac2_8588_4e993b2b858e = KubernetesPodOperator(
    name="4",
    namespace="airflow",
    image="quay.io/eformat/airflow-runner:2.5.1",
    cmds=["sh", "-c"],
    arguments=[
        "mkdir -p ./jupyter-work-dir/ && cd ./jupyter-work-dir/ && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/elyra/airflow/bootstrapper.py --output bootstrapper.py && echo 'Downloading https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt' && curl --fail -H 'Cache-Control: no-cache' -L https://raw.githubusercontent.com/elyra-ai/elyra/v3.15.0/etc/generic/requirements-elyra.txt --output requirements-elyra.txt && python3 -m pip install packaging && python3 -m pip freeze > requirements-current.txt && python3 bootstrapper.py --pipeline-name 'fingerprint-left-right' --cos-endpoint http://minio.airflow.svc.cluster.local:9000 --cos-bucket fingerprint-left-right --cos-directory 'fingerprint-left-right-0519234554' --cos-dependencies-archive '4.0-dataset-create-4391fca7-53f7-4ac2-8588-4e993b2b858e.tar.gz' --file 'datasci-fingerprint/notebooks/4.0-dataset-create.ipynb' "
    ],
    task_id="4",
    env_vars={
        "AWS_S3_ENDPOINT": "minio.airflow.svc.cluster.local:9000",
        "AWS_S3_BUCKET": "fingerprint-left-right",
        "ELYRA_RUNTIME_ENV": "airflow",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "ELYRA_RUN_NAME": "fingerprint-left-right-{{ ts_nodash }}",
    },
    volumes=[],
    volume_mounts=[],
    secrets=[
        Secret("env", "AWS_ACCESS_KEY_ID", "airflow-storage", "AWS_ACCESS_KEY_ID"),
        Secret(
            "env", "AWS_SECRET_ACCESS_KEY", "airflow-storage", "AWS_SECRET_ACCESS_KEY"
        ),
    ],
    annotations={},
    labels={},
    tolerations=[],
    in_cluster=True,
    config_file="None",
    dag=dag,
)

op_4391fca7_53f7_4ac2_8588_4e993b2b858e.image_pull_policy = "Always"

op_4391fca7_53f7_4ac2_8588_4e993b2b858e << op_cf96ee47_0088_452c_96d6_ac1a7511cf92

op_4391fca7_53f7_4ac2_8588_4e993b2b858e << op_9f3093dd_1f4b_4e71_9040_3a9bcbbda435
