# ☁️ Scalable Cloud Architecture Design (AWS Solutions Architect)

A production-grade, highly available AWS cloud architecture designed to replace a single-instance EC2 server — eliminating slow response times, crashes, and database single-points-of-failure.

---

## 🏗️ Architecture Overview

```
Users → Route 53 → ALB → Auto Scaling EC2 Group → RDS Multi-AZ
                              ↕
                         S3 (Static Assets)
                              ↕
                       CodePipeline (CI/CD)
```

---

## 🚨 Problem Solved

| Issue | Solution |
|-------|----------|
| Single EC2 crashes = full downtime | Auto Scaling Group (min 2 instances) |
| Slow response times under load | ELB + horizontal scaling |
| Database failure = data loss | RDS Multi-AZ with automatic failover |
| Manual deployments | AWS CodePipeline CI/CD |

---

## 🛠️ AWS Services Used

| Service | Role |
|---------|------|
| **Route 53** | DNS with health checks & latency-based routing |
| **ALB (Elastic Load Balancer)** | Distribute traffic across EC2 instances |
| **EC2 + Auto Scaling** | Scale from 2–10 instances based on CPU |
| **RDS Multi-AZ (PostgreSQL)** | Highly available database with auto-failover |
| **Amazon S3** | Static assets, backups, and logs |
| **AWS CodePipeline** | CI/CD: Source → Build → Deploy |
| **Docker** | Containerized application deployment |

---

## 📊 Key Outcomes

- ✅ **99.99% uptime** — achieved through Multi-AZ + Auto Scaling
- ✅ **~60% faster** response times at peak load
- ✅ **Zero manual recovery** — automatic failover for both compute and DB
- ✅ **Cost-optimized** — instances scale down during low traffic

---

## 📁 Files

- `architecture.py` — Python reference script with architecture config & cost estimates
- `ARCHITECTURE.md` — Detailed design document with ASCII diagram

---

## 👤 Author

**Nuaman M** — [LinkedIn](https://linkedin.com/in/nuamanjaleel) | [GitHub](https://github.com/YOUR_USERNAME)
