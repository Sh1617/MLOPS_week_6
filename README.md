# Iris Classification API (FastAPI + Docker + Kubernetes)

This project serves an Iris flower classifier model as a REST API using FastAPI. The API is containerized using Docker and deployed to a Kubernetes cluster on Google Cloud.

---

## FastAPI - Run Locally

### Start the FastAPI Server
```bash
uvicorn iris_fastapi_v2:app --host 0.0.0.0 --port 8000
````

### Test `/predict` Route

```powershell
Invoke-RestMethod -Uri "http://34.66.154.77:8000/predict" `
  -Method Post `
  -Body '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}' `
  -ContentType "application/json"
```

---

## Docker Instructions

### 1. One-time setup: Add current user to Docker group

```bash
sudo usermod -aG docker $USER
```

### 2. Build Docker Image

```bash
docker build -t iris-api .
```

### 3. Run Container

```bash
docker run -d -p 8200:8200 iris-api
```

### 4. Docker Utilities

* List Docker Images:

  ```bash
  docker images
  ```
* View Container Logs:

  ```bash
  docker logs <container-id>
  ```
* List Running Containers:

  ```bash
  docker ps
  ```
* Stop a Container:

  ```bash
  docker stop <container-id>
  ```

---

## ☸️ Kubernetes (GKE) Deployment

### 1. Enable Kubernetes API and Artifact Registry

```bash
gcloud services enable artifactregistry.googleapis.com
```

### 2. Create Docker Repository

```bash
gcloud artifacts repositories create my-repo \
  --repository-format=docker \
  --location=us-central1 \
  --description="Docker repo for ML models"
```

### 3. Configure Docker to Use Artifact Registry

```bash
gcloud auth configure-docker us-central1-docker.pkg.dev
```

### 4. Tag Docker Image

```bash
docker tag iris-api us-central1-docker.pkg.dev/<PROJECT-ID>/my-repo/iris-api
```

### 5. Push Image to Artifact Registry

```bash
docker push us-central1-docker.pkg.dev/<PROJECT-ID>/my-repo/iris-api
```

> Replace `<PROJECT-ID>` with your actual GCP Project ID.

---

## Deploy to Kubernetes Cluster

Once your GKE cluster is created and credentials are configured:

```bash
kubectl apply -f deployment.yaml
```

To check running pods:

```bash
kubectl get pods
```
