# Metaflow on Argo Workflows

This project shows how to run Metaflow pipelines on Kubernetes using Argo Workflows, with MinIO used for storing data. It is set up for local testing with Minikube.


## Project Overview

This project runs a Metaflow pipeline on Kubernetes using Argo Workflows. The pipeline is triggered from a local machine using the Metaflow CLI, and Argo executes each step as a Kubernetes pod. Workflow data is stored in MinIO, and run details are tracked by the Metaflow service. You can monitor executions using both Argo UI and Metaflow UI.


## Architecture

Local Machine (Metaflow CLI) submits workflows to Metaflow Service.  
Metaflow Service creates Argo WorkflowTemplates.  
Argo Workflows executes each step as Kubernetes pods.  
Pods store artifacts in MinIO and metadata in Metaflow Service.

## Namespaces Used

metaflow: Metaflow service, UI, PostgreSQL  
argo: Argo workflow controller and Argo UI  
minio: MinIO object storage  
default: Optional namespace where workflows can also run  

Workflows can be executed in either the argo or default namespace.

## Prerequisites

Kubernetes cluster  
kubectl  
Helm  
Python 3.x  
Metaflow (pip install metaflow)  
Argo CLI  
Docker  

## Repository Structure

argo_hello_demo_flow.py – example Metaflow pipeline  
charts/ – Helm charts for Metaflow services  
minio-deployment.yaml – MinIO deployment and service  
configmap.yaml – Metaflow configuration used by Argo workflows  
secret.yaml – MinIO credentials and S3 endpoint for Argo pods   
metapolis-flow-sa-rbac.yaml – ServiceAccount and RBAC  
metaflow-argo-cluster-rbac.yaml – ClusterRole and ClusterRoleBinding  


## Setup Instructions

Start Minikube:

minikube start

Deploy MinIO:

kubectl apply -f minio-deployment.yaml

Deploy Metaflow services using Helm:

helm install metaflow ./charts/metaflow -n metaflow --create-namespace

Deploy Argo Workflows in the argo namespace (using official Argo quick start):

kubectl create namespace argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/latest/download/install.yaml


Apply RBAC:

kubectl apply -f metapolis-flow-sa-rbac.yaml  
kubectl apply -f metaflow-argo-cluster-rbac.yaml

Apply Metaflow configuration and secrets in the argo namespace:

kubectl apply -n argo -f configmap.yaml
kubectl apply -n argo -f secret.yaml


This enables workflow execution, pod creation, and cross-namespace visibility.

## Port Forwarding (Local Access)

Port-forward the MinIO, Metaflow, and Argo services to your local machine so the CLI and UIs can be accessed from the browser. The local ports can be chosen based on availability.

## Environment Variables (Local CLI)

Before running Metaflow from your local machine, configure the required environment variables to point to the MinIO and Metaflow services exposed via port-forwarding.

- METAFLOW_S3_ENDPOINT_URL is used only for local runs via port-forward.
- Argo pods do not use this value.
- Kubernetes pods get the MinIO endpoint via secrets.
- METAFLOW_ARGO_WORKFLOWS_ENV_VARS_TO_SKIP prevents local values from being baked into Argo templates.


## Monitoring

Argo UI: http://localhost:2746  
Metaflow UI: http://localhost:8083  
MinIO UI: http://localhost:9001  

## Running a Metaflow Pipeline

Create the Argo WorkflowTemplate:

python argo_hello_demo_flow.py --datastore=s3 argo-workflows --name argohellodemoflow create

Trigger a workflow run:

python argo_hello_demo_flow.py --datastore=s3 argo-workflows --name argohellodemoflow trigger



## Conclusion

This project demonstrates how Metaflow pipelines can be executed on Kubernetes using Argo Workflows with MinIO for storage. 



export METAFLOW_S3_ENDPOINT_URL=http://127.0.0.1:19000

export METAFLOW_SERVICE_URL=http://127.0.0.1:18080

export AWS_ACCESS_KEY_ID=minio

export AWS_SECRET_ACCESS_KEY=minio123

export METAFLOW_DEFAULT_DATASTORE=s3

export METAFLOW_DATASTORE_SYSROOT_S3=s3://metaflow

export METAFLOW_ARGO_WORKFLOWS_NAMESPACE=argo

export METAFLOW_KUBERNETES_NAMESPACE=argo

export METAFLOW_ARGO_WORKFLOWS_NAMESPACE=argo

export METAFLOW_ARGO_WORKFLOWS_ENV_VARS_TO_SKIP=METAFLOW_S3_ENDPOINT_URL

export METAFLOW_SERVICE_INTERNAL_URL=http://metaflow-metaflow-service.metaflow.svc.cluster.local:8080



