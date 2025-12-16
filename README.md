## Self-Healing DevOps Application

This application is intentionally designed to simulate real-world failures
such as CPU spikes, memory leaks, and crashes to test Kubernetes self-healing,
auto-scaling, and rollback mechanisms.

Endpoints:
- /health – health monitoring
- /cpu-stress – simulate high CPU load
- /memory-stress – simulate memory leak
- /crash – force application crash
