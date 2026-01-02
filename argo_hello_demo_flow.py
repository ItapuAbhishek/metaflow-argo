from metaflow import FlowSpec, step,kubernetes,environment
from datetime import datetime


class ArgoHelloDemoFlow(FlowSpec):
    
    
    @environment(vars={
        "METAFLOW_S3_ENDPOINT_URL": "http://minio.minio.svc.cluster.local:9000",
        "METAFLOW_DEFAULT_DATASTORE": "s3",
        "METAFLOW_DATASTORE_SYSROOT_S3": "s3://metaflow",
        "METAFLOW_DEFAULT_METADATA": "service",
        "METAFLOW_SERVICE_URL": "http://metaflow-metaflow-service.metaflow.svc.cluster.local:8080",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123"
    })
    @step
    def start(self):
        print("Hello from Metaflow running on Argo!")
        print("Execution time:", datetime.now().isoformat())
        self.next(self.end)

    @environment(vars={
        "METAFLOW_S3_ENDPOINT_URL": "http://minio.minio.svc.cluster.local:9000",
        "METAFLOW_DEFAULT_DATASTORE": "s3",
        "METAFLOW_DATASTORE_SYSROOT_S3": "s3://metaflow",
        "METAFLOW_DEFAULT_METADATA": "service",
        "METAFLOW_SERVICE_URL": "http://metaflow-metaflow-service.metaflow.svc.cluster.local:8080",
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123"
    })
    @step
    def end(self):
        print("ArgoHelloDemoFlow completed successfully")


if __name__ == "__main__":
    ArgoHelloDemoFlow()
