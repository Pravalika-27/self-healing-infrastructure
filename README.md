# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

This project implements a self-healing infrastructure on an EC2 Ubuntu instance where:
- Prometheus monitors services
- Alertmanager triggers alerts when issues are detected
- Ansible automatically remediates the problems

## Architecture

![Architecture Diagram](architecture.png)

## Prerequisites

- AWS account with EC2 access
- Basic knowledge of Linux commands
- Familiarity with YAML syntax

## Setup Instructions

1. Launch an EC2 Ubuntu 22.04 instance with the following ports open:
   - SSH (22)
   - HTTP (80)
   - Prometheus (9090)
   - Alertmanager (9093)
   - Node Exporter (9100)

2. SSH into the instance:
   ```bash
   ssh -i /path/to/your-key.pem ubuntu@<your-ec2-public-ip>

