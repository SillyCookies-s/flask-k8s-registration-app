# Kubernetes Deployment Guide

## Prerequisites
- Minikube installed and running
- Helm installed
- Docker images available on Docker Hub

## Setup Instructions

### 1. Start Minikube
```bash
minikube start
```

### 2. Configure Values
```bash
# Copy example values and configure
cp k8/values.example.yaml k8/values.yaml
# Edit k8/values.yaml with your MongoDB URL and namespace
```

### 3. Deploy with Helm
```bash
# Install the application
helm install serene ./k8

# Check deployment status
kubectl get pods -n audrie
kubectl get services -n audrie
```

### 4. Access Application
```bash
# Port forward to access frontend
kubectl port-forward svc/frontend 5000:5000 -n audrie

# Access at http://localhost:5000
```

### 5. Verify Backend
```bash
# Check backend logs
kubectl logs -l app=backend -n audrie

# Test API endpoint
curl http://localhost:5000/api
```

## Troubleshooting
- Ensure MongoDB URL is correctly configured in values.yaml
- Check pod logs for connection issues
- Verify namespace exists or create it: `kubectl create namespace audrie`