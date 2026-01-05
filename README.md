# DevOps_Project

Repository for deploying Application Docker Image on Kubernetes

1. Install docker desktop
2. Install kubectl
3. Install Helm
4. Install minikube
5. minikube start --driver=docker
6. minikube status
7. Get into this Deployment folder directory
8. helm install fake-news-detector ./helm-chart
9. If pod takes so much time to start, pull docker image in minikube 1st- minikube ssh docker pull sakshineeraj/cicd:latest
10. kubectl port-forward svc/fake-news-detector 8080:80

Simple Docker deployment
1. docker pull sakshineeraj/cicd:latest
2. docker run -d -p 1000:5000 --name cicd-app sakshineeraj/cicd:latest