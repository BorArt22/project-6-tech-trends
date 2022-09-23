


# TechTrends

TechTrends is an online website used as a news sharing platform, that enables consumers to access the latest news within the cloud-native ecosystem. In addition to accessing the available articles, readers are able to create new media articles and share them.

The web application is written using the Python Flask framework. It uses SQLite, a lightweight disk-based database to store the submitted articles.

Below you can examine the main components of the firsts prototype of the application:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff782da_screenshot-2021-01-07-at-21.53.16/screenshot-2021-01-07-at-21.53.16.png"
  alt="TechTrends web application components">
  <figcaption>TechTrends web application components</figcaption>
</figure>

Additionally, the initial sitemap of the website can be found below:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff78576_screenshot-2021-01-07-at-22.04.29/screenshot-2021-01-07-at-22.04.29.png"
  alt="Diagram with the sitemap of the web applciation">
  <figcaption>TechTreds sitemap</figcaption>
</figure>

Where:
 - **About** page - presents a quick overview of the TechTrends site 
 - **Index** page - contains the content of the main page, with a list of all available posts within TechTrends 
 - **New Post** page - provides a form to submit a new post 
 - **404** page - is rendered when an article ID does not exist is accessed

And lastly, the first prototype of the application is storing and accessing posts from the "POSTS" SQL table. A post entry contains the post ID (primary key), creation timestamp, title, and content. The "POSTS" table schema can be examined below:
<figure>
  <img
  src="https://video.udacity-data.com/topher/2021/January/5ff81ebb_screenshot-2021-01-07-at-22.16.30/screenshot-2021-01-07-at-22.16.30.png"
  alt="Table with the SQL schema for the posts table">
  <figcaption>The schema for the "posts" table</figcaption>
</figure>

# Table of Contents
1. [Project Description](#project-description)
2. [Project Files](#project-files)
3. [Deploy a Kubernetes cluster](#deploy-a-kubernetes-cluster)
4. [Deploy the ArgoCD](#deploy-the-argocd) 

# Project Description
In this project implemented a CI/CD pipeline for package and deploy TechTrends to Kubernetes.

The Continuous Integration (CI) implemented using GitHub Actions to build, tag, and push the TechTrends Docker image to DockerHub.

The Continuous Delivery (CD)  implemented using ArgoCD to release the application to staging and production environments using the templated manifests from the Helm chart.

# Project Files
```
.
├── README.md
├── .gitignore
├── docker_commands
├── Dockerfile
├── Vagrantfile
├── techtrends
	├── README.md
	├── __init__.py
	├── app.py
	├── init_db.py
	├── requirements.txt
	├── schema.sql
	├── static
	│   └── css
	│       └── main.css
	└── templates
	    ├── 404.html
	    ├── about.html
	    ├── base.html
	    ├── create.html
	    ├── index.html
	    └── post.html
├── .github
	└── workflows
	    └── techtrends-dockerhub.yml
├── kubernetes
	├── namespace.yaml
	├── deploy.yaml
	├── service.yaml	
	├── README.md
├── helm
	├── Chart.yaml
	├── values.yaml
	├── values-prod.yaml
	├── values-staging.yaml
	├── README.md
	└── workflows
		├── deploy.yaml
		├── namespace.yaml
		└── service.yaml				    
├── argocd
	├── argocd-server-nodeport.yaml
	├── helm-techtrends-prod.yaml
	├── helm-techtrends-staging.yaml
	└── README.md
└── screenshots
	├── argocd-techtrends-prod.PNG
	├── argocd-techtrends-staging.PNG
	├── argocd-ui.PNG
	├── ci-dockerhub.PNG
	├── ci-github-actions.PNG
	├── docker-run-local.PNG
	├── k8s-nodes.PNG
	├── kubernetes-declarative-manifests.PNG
	└── README.md
```
- `README.md` provides discussion on the project
- `.gitignore` file specifies intentionally untracked files that Git should ignore
- `docker_commands` docker commands for local launching TechTrends
- `Dockerfile` document that contains all the commands a user could call on the command line to assemble an image
- `Vagrantfile` describe the type of machine required for a project, and how to configure and provision these machines
- `techtrends/README.md`  contains the main steps of how to execute the TechTrends application
- `techtrends/__init__.py`  is a reserved method used to indicate that a directory is a Python package
- `techtrends/app.py`  contains the main logging of the TechTrends application
- `techtrends/init_db.py`  is a file that is used to initialize the  `posts`  database with a set of articles
- `techtrends/requirements.txt`  contains a list of packages that need to be installed before running the TechTrends application
- `techtrends/schema.sql`  outlines the  `posts`  database schema
- `techtrends/static/`  folder contains the CSS files
- `techtrends/templates/`  folder outlines the HTML structure of the TechTrends application
- `.github\workflows\template\python-version.yml` configuration file for a GitHub Action that will package and push the new image for the TechTrends application to DockerHub
- `kubernetes\namespace.yaml` declarative approach for create namespace `sandbox`
- `kubernetes\deploy.yaml` declarative approach for create Deployment for deploy TechTrends in `sandbox` namespace
- `kubernetes\service.yaml` declarative approach for create Service for TechTrends in `sandbox` namespace
- `kubernetes\README.md` provides discussion to release the application to the sandbox environment
- `helm\Chart.yaml` the chart's metainformation
- `helm\values.yaml` contains general values for release
- `helm\values-prod.yaml` contains values for release to the prod environment
- `helm\values-staging.yaml` contains values for release to the staging environment
- `helm\README.md` provides discussion to implement helm templates
- `helm\templates\deploy.yaml` template for declarative approach for create deployment
- `helm\templates\namespace.yaml` template for declarative approach for create namespace
- `helm\templates\service.yaml` template for declarative approach for create service
- `argocd\argocd-server-nodeport.yaml` the YAML manifest for the NodePort service
- `argocd\helm-techtrends-prod.yaml` ArgoCD applications manifest resources to deploy TechTrends to production environment
- `argocd\helm-techtrends-staging.yaml` ArgoCD applications manifest resources to deploy TechTrends to staging environment
- `argocd\README.md` provides discussion to implement ArgoCD
- `screenshots/` folder contains the screenshots and description of implementing the CI/CD pipeline

# Deploy a Kubernetes cluster

Using vagrant, create a Kubernetes cluster with k3s. Refer to the Vagrantfile from the repository. Make sure to have vagrant and VirtualBox 6.1.16 or higher installed.

To create a vagrant box and ssh into it, use the following commands:
```
# create a vagrant box using the Vagrantfile in the current directory
vagrant up

# SSH into the vagrant box
# Note: this command uses the .vagrant folder to identify the details of the vagrant box
vagrant ssh
```

To deploy the Kubernetes cluster, refer to the  [k3s](https://k3s.io/)  documentation.  **_Note:_**  To interact with the cluster kubectl, you need to have root access to the kubeconfig file. Hence, use  `sudo su -`  to become root and use kubectl commands.

Verify if the cluster is operational by evaluating if the node in the cluster is up and running. You can use the  `kubectl get no`  command.

Next follow the instructions in `kubernetes\README.md` for deployment the application to a Kubernetes cluster in sandbox environment.

# Deploy the ArgoCD
Given the k3s cluster, install ArgoCD and access it through the browser. Make sure to reference the instructions below:

-   Official  [install guide for ArgoCD](https://argoproj.github.io/argo-cd/getting_started/#1-install-argo-cd)
-   The YAML manifest for the NodePort service can be found under `argocd\argocd-server-nodeport.yaml` in this repository
-   Access the ArgoCD UI by going to  `https://192.168.50.4:30008`  or  `http://192.168.50.4:30007`
-   Login credentials can be retrieved using the steps in the  [credentials guide](https://argoproj.github.io/argo-cd/getting_started/#4-login-using-the-cli)

To Deploy TechTrends with ArgoCD follow instructions in `argocd\README.md`