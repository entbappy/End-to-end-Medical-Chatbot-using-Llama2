#!/bin/bash

#Install 1.28.0
curl -LO https://dl.k8s.io/release/v1.28.0/bin/linux/amd64/kubectl

#Validate binary
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"

#Validate the kubectl binary against the checksum file:
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check

#Install kubectl
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

#Check kubectl version
kubectl version --client