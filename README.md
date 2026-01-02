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
configmap.yaml – Metaflow configuration  
secret.yaml –  MinIO credentials  
metapolis-flow-sa-rbac.yaml – ServiceAccount and RBAC  
metaflow-argo-cluster-rbac.yaml – ClusterRole and ClusterRoleBinding  


## Setup Instructions

Start Minikube:

minikube start

Deploy MinIO:

kubectl apply -f minio-deployment.yaml

Deploy Metaflow services using Helm:

helm install metaflow ./charts/metaflow -n metaflow --create-namespace

Deploy Argo Workflows in the argo namespace:

kubectl create namespace argo  
kubectl apply -n argo -f <argo-install-manifest>.yaml

Apply RBAC:

kubectl apply -f metapolis-flow-sa-rbac.yaml  
kubectl apply -f metaflow-argo-cluster-rbac.yaml

This enables workflow execution, pod creation, and cross-namespace visibility.

## Port Forwarding (Local Access)

Port-forward the MinIO, Metaflow, and Argo services to your local machine so the CLI and UIs can be accessed from the browser. The local ports can be chosen based on availability.

## Environment Variables (Local CLI)

Before running Metaflow from your local machine, configure the required environment variables to point to the MinIO and Metaflow services exposed via port-forwarding.



## Monitoring

Argo UI: http://localhost:2746  
Metaflow UI: http://localhost:8083  
MinIO UI: http://localhost:9001  

## Running a Metaflow Pipeline

Create the Argo WorkflowTemplate:

python argo_hello_demo_flow.py argo-workflows create

Trigger a workflow run:

python argo_hello_demo_flow.py argo-workflows trigger

## Issues

Environment variables and resource limits defined using Metaflow decorators are not automatically injected into Argo WorkflowTemplates and must be manually updated in the template after creation. 


## Conclusion

This project demonstrates how Metaflow pipelines can be executed on Kubernetes using Argo Workflows with MinIO for storage. 


