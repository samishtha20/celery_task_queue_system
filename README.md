# Celery Task Queue Autoscaling System

## Overview
This project demonstrates how to autoscale Celery workers in Kubernetes (Minikube or EKS) based on queue load. It features CPU-bound and IO-bound tasks, a load generator, Horizontal Pod Autoscaler (HPA) configuration, and full monitoring with Prometheus and Grafana. The system uses RabbitMQ as the message broker and includes a Prometheus exporter for Celery metrics.

## Architecture
- **Celery App**: Python application with multiple task types.
- **RabbitMQ**: Message broker (deployed via Helm).
- **Kubernetes**: Runs Celery workers, autoscaled by HPA.
- **Monitoring**: Prometheus and Grafana dashboards, plus Celery Prometheus exporter for queue/task metrics.

## Setup Instructions

### 1. Prerequisites
- Python 3.10+
- Docker
- Minikube or EKS
- Helm
- kubectl

### 2. Build and Deploy
1. **Build Docker image:**
   ```zsh
   docker build -t celery-autoscaler .
   ```

2. **Start Minikube:**
   ```zsh
   minikube start --driver=docker
   ```

3. **Deploy RabbitMQ:**
   ```zsh
   helm repo add bitnami https://charts.bitnami.com/bitnami
   helm install rabbitmq bitnami/rabbitmq
   ```

4. **Deploy Celery workers and HPA:**
   ```zsh
   kubectl apply -f k8s/celery-worker-deployment.yaml
   kubectl apply -f k8s/hpa.yaml
   ```

5. **Deploy Celery Prometheus exporter:**
   ```zsh
   kubectl apply -f k8s/celery-exporter-deployment.yaml
   kubectl apply -f k8s/celery-exporter-service.yaml
   kubectl apply -f k8s/celery-exporter-servicemonitor.yaml
   ```

6. **Deploy Prometheus and Grafana:**
   ```zsh
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo update
   helm install prometheus-stack prometheus-community/kube-prometheus-stack
   ```

### 3. Monitoring
- **Port-forward Grafana:**
  ```zsh
  kubectl port-forward svc/prometheus-stack-grafana 3000:80
  ```
  Access Grafana at [http://localhost:3000](http://localhost:3000) (user: `admin`, password: `prom-operator`).

- **Port-forward Prometheus:**
  ```zsh
  kubectl port-forward svc/prometheus-stack-kube-prom-prometheus 9090:9090
  ```
  Access Prometheus at [http://localhost:9090](http://localhost:9090).

- **Grafana Dashboards:**
  - Search for metrics such as `celery_queue_length`, `celery_task_received_total`, `celery_task_succeeded_total`, etc.
  - Create dashboards to visualize queue depth, task rates, and worker status.

### 4. Simulate Load
- **Run the load generator to trigger autoscaling:**
  ```zsh
  PYTHONPATH=. python3 scripts/simulate_load.py
  ```

- **Watch HPA and pod scaling:**
  ```zsh
  kubectl get hpa
  kubectl get pods
  kubectl top pods
  ```

## Troubleshooting
- If Celery exporter metrics are not visible in Prometheus, ensure the ServiceMonitor port matches the service port name (`metrics`).
- Restart Prometheus operator and Prometheus server if targets do not appear.
- Check pod logs for errors.

## File Structure

```
celery_task_queue/
├── analysis.md
├── Dockerfile
├── README.md
├── requirements.txt
├── celery_app/
│   ├── celeryconfig.py
│   └── tasks.py
├── k8s/
│   ├── celery-exporter-deployment.yaml
│   ├── celery-exporter-service.yaml
│   ├── celery-exporter-servicemonitor.yaml
│   ├── celery-worker-deployment.yaml
│   ├── hpa.yaml
│   └── service.yaml
└── scripts/
    └── simulate_load.py
```

## License
MIT
