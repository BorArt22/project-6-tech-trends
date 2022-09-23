## Kubernetes Declarative Manifests 

The Kubernetes declarative manifests in this directory:
- `namespace.yaml` declarative approach for create namespace `sandbox`
- `deploy.yaml` declarative approach for create Deployment for deploy TechTrends in `sandbox` namespace
- `service.yaml` declarative approach for create Service for TechTrends in `sandbox` namespace

For Deploy the application to a Kubernetes cluster in sandbox environment:
- Copy manifests from this folder to the vagrant box
- Run next command:
    `kubectl apply -f namespace.yaml`
    `kubectl apply -f deployment.yaml`
    `kubectl apply -f service.yaml`
