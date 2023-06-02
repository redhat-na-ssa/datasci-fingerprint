datasci-fingerprint
==============================

![fingerprint-overview](datasci-fingerprint/docs/fingerprint-prediction.png)

# Fingerprint Left or Right Hand Prediction

## About the data
Sokoto Coventry Fingerprint Dataset (SOCOFing) is a biometric fingerprint database designed for academic research purposes. SOCOFing is made up of 6,000 fingerprint images from 600 African subjects and contains unique attributes such as labels for gender, hand and finger name as well as synthetically altered versions with three different levels of alteration for obliteration, central rotation, and z-cut. For a complete formal description and usage policy please refer to the following paper: https://arxiv.org/abs/1807.10609.

## About the notebooks
The intention of this notebook is to demonstrate steps from data ingestion to model saving that provides an accurate enough model that predicts if a fingerprint comes from a left or right hand. Coupled with other models that accurately predict finger and gender is valuable when matching against other identifiable information.

1. *Data Ingestion* [from object storage](#working-with-s3-buckets)
1. *Data Exploration* visualize, convert to arrays, counts
1. *Create Datasets* split into train, validate, test
1. *Experiment* use a default keras sequential model and see how it performs
1. *Train and Tune* spend more resources to search for optimal parameters and fit a model
1. *Prediction Sampling* in the notebook get a feel for predictions against real fingerprints

## About pipeline
Elyra is used to connects the notebooks and export a DAG pipeline.py code that can orchestrated with Airflow to automate the training when new data is available or on some event.

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
