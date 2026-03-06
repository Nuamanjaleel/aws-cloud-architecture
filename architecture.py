"""
AWS Scalable Cloud Architecture — Design & Deployment Reference
Author: Nuaman M

This script documents the architecture decisions and can be used as a
reference for deploying a highly available, scalable AWS infrastructure.

Architecture Overview:
    Internet → Route 53 → ELB → Auto Scaling EC2 → RDS Multi-AZ
                                       ↕
                                       S3 (static assets)
"""

import boto3
import json

# ─────────────────────────────────────────────
# ARCHITECTURE CONFIGURATION
# ─────────────────────────────────────────────

ARCHITECTURE = {
    "region": "us-east-1",
    "availability_zones": ["us-east-1a", "us-east-1b", "us-east-1c"],
    "components": {
        "dns": {
            "service": "Route 53",
            "purpose": "DNS routing with health checks and failover policies",
            "routing_policy": "Latency-based"
        },
        "load_balancer": {
            "service": "Elastic Load Balancer (ALB)",
            "purpose": "Distribute traffic across EC2 instances",
            "health_check_path": "/health",
            "health_check_interval": 30
        },
        "compute": {
            "service": "EC2 with Auto Scaling Group",
            "instance_type": "t3.medium",
            "min_instances": 2,
            "max_instances": 10,
            "desired_capacity": 3,
            "scaling_policy": "Target Tracking — CPU 70%"
        },
        "database": {
            "service": "Amazon RDS (PostgreSQL)",
            "deployment": "Multi-AZ",
            "instance_class": "db.t3.medium",
            "purpose": "Eliminates single-point-of-failure, automatic failover",
            "backup_retention_days": 7
        },
        "storage": {
            "service": "Amazon S3",
            "purpose": "Static asset hosting, backups, and logs",
            "versioning": True
        },
        "ci_cd": {
            "service": "AWS CodePipeline",
            "stages": ["Source (GitHub)", "Build (CodeBuild)", "Deploy (CodeDeploy)"]
        }
    }
}


def print_architecture_summary():
    """Print a readable summary of the architecture."""
    print("=" * 60)
    print("   AWS SCALABLE CLOUD ARCHITECTURE SUMMARY")
    print("=" * 60)
    for component, details in ARCHITECTURE["components"].items():
        print(f"\n📦 {component.upper().replace('_', ' ')}")
        for key, value in details.items():
            print(f"   {key}: {value}")
    print("\n" + "=" * 60)


def estimate_monthly_cost():
    """Rough monthly cost estimate for the architecture."""
    costs = {
        "EC2 (3x t3.medium)": 120.00,
        "RDS Multi-AZ (db.t3.medium)": 95.00,
        "Load Balancer (ALB)": 22.00,
        "S3 (100GB)": 2.30,
        "Route 53": 0.50,
        "Data Transfer": 15.00,
    }
    total = sum(costs.values())
    print("\n💰 ESTIMATED MONTHLY COST")
    print("-" * 35)
    for service, cost in costs.items():
        print(f"  {service:<30} ${cost:.2f}")
    print("-" * 35)
    print(f"  {'TOTAL':<30} ${total:.2f}")
    return total


def get_architecture_json():
    """Export architecture as JSON (useful for documentation)."""
    return json.dumps(ARCHITECTURE, indent=2)


if __name__ == "__main__":
    print_architecture_summary()
    estimate_monthly_cost()
    print("\n📄 Architecture JSON exported to architecture.json")
    with open("architecture.json", "w") as f:
        f.write(get_architecture_json())
