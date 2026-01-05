from metaflow import FlowSpec, step,kubernetes,environment
from datetime import datetime


class ArgoHelloDemoFlow(FlowSpec):
    
    @kubernetes(namespace='argo',cpu='0.1',memory='400',secrets=['mf-minio-creds'])
    @environment(vars={
        'METAFLOW_DEFAULT_DATASTORE': 's3',
        'METAFLOW_DATASTORE_SYSROOT_S3': 's3://metaflow',
        'METAFLOW_DEFAULT_METADATA': 'service',
        'METAFLOW_SERVICE_INTERNAL_URL': 'http://metaflow-metaflow-service.metaflow.svc.cluster.local:8080',
        
    })
    @step
    def start(self):
        print("Hello from Metaflow running on Argo!")
        print("Execution time:", datetime.now().isoformat())
        self.next(self.end)
    @kubernetes(namespace='argo',cpu='0.1',memory='400',secrets=['mf-minio-creds'])
    @environment(vars={
        'METAFLOW_DEFAULT_DATASTORE': 's3',
        'METAFLOW_DATASTORE_SYSROOT_S3': 's3://metaflow',
        'METAFLOW_DEFAULT_METADATA': 'service',
        'METAFLOW_SERVICE_INTERNAL_URL': 'http://metaflow-metaflow-service.metaflow.svc.cluster.local:8080',
    })
    @step
    def end(self):
        print("ArgoHelloDemoFlow completed successfully")


if __name__ == "__main__":
    ArgoHelloDemoFlow()
