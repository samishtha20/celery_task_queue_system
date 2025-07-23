# Autoscaling Analysis Report

## Load Scenarios

### Low Load
- Few tasks submitted.
- HPA keeps worker count at minimum (1 pod).
- CPU utilization remains low.

### Medium Load
- Moderate number of tasks submitted.
- HPA increases worker pods as CPU utilization rises.
- Queue depth decreases as more workers process tasks.

### High Load
- Large burst of tasks submitted.
- HPA scales up to max pods (5).
- CPU utilization peaks, queue depth handled efficiently.

### Oscillating Load
- Alternating bursts and lulls.
- HPA responds by scaling up/down as needed.
- No excessive thrashing due to reasonable thresholds.

## Observations
- Scaling is triggered by CPU utilization (can be customized).
- System responds quickly to bursts, scales down after load subsides.
- `kubectl get hpa` shows real-time scaling events.

## Recommendations
- For production, consider custom metrics (queue depth).
- Add monitoring for deeper insights (Prometheus/Grafana).

## Example Output
```
NAME          REFERENCE            TARGETS         MINPODS   MAXPODS   REPLICAS   AGE
celery-hpa    Deployment/celery-worker   80%/60%         1         5         4         10m
```

## Screenshots
(Add screenshots of HPA scaling, pod counts, Grafana dashboards if available)


<img width="362" height="48" alt="Screenshot 2025-07-23 at 11 06 07 PM" src="https://github.com/user-attachments/assets/5f1e7568-3e38-42d6-9dde-fd718f6cc417" />



