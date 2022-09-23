## ArgoCD Manifests 

The ArgoCD manifests in this directory:
- `argocd-server-nodeport.yaml` the YAML manifest for the NodePort service
- `helm-techtrends-prod.yaml` ArgoCD applications manifest resources to deploy TechTrends to production environment
- `helm-techtrends-staging.yaml` ArgoCD applications manifest resources to deploy TechTrends to staging environment

To Deploy TechTrends with ArgoCD:
- Copy manifests from this folder to the vagrant box
- Given the k3s cluster, run next commands:
    `kubectl apply -f helm-techtrends-staging.yaml`
    `kubectl apply -f helm-techtrends-prod.yaml`