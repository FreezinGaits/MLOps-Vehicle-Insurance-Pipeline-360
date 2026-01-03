````markdown
# 🚗 Vehicle Insurance Response Prediction  
## Production-Grade End-to-End MLOps System

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?logo=docker)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20EC2%20%7C%20ECR-orange?logo=amazonaws)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-success?logo=githubactions)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb)

---

## Overview

This repository implements a **production-oriented MLOps pipeline** for predicting customer response to vehicle insurance offers.

The project emphasizes **engineering rigor over experimentation**, demonstrating how machine learning systems are:

- validated before training
- evaluated before deployment
- versioned and promoted safely
- served reliably via an API

This is **not a notebook-only project** — it is a deployable ML system.

---

## Problem Definition

Predict whether a customer will respond positively (`1`) or negatively (`0`) to an insurance offer, based on demographic and vehicle attributes.

- **Task**: Binary classification  
- **Challenge**: Class imbalance  
- **Primary metrics**: F1 Score, Precision, Recall  

Accuracy is intentionally avoided as the primary metric.

---

## High-Level Architecture

```
MongoDB Atlas
|
v
Data Ingestion
|
v
Schema-Driven Validation
|
v
Feature Engineering & Transformation
|
v
Model Training (RandomForest)
|
v
Model Evaluation Gate
|
v
Model Registry (AWS S3)
|
v
FastAPI Inference Service
|
v
Docker + CI/CD + EC2 Deployment
```

---

## Technology Stack

### Machine Learning
- Python 3.10
- pandas, NumPy
- scikit-learn
- imbalanced-learn (SMOTEENN)

### MLOps & Engineering
- Modular pipeline architecture
- YAML-based schema validation
- Artifact-driven workflow
- Custom logging and exception handling
- Model evaluation gate before promotion

### Cloud & DevOps
- MongoDB Atlas (data source)
- AWS S3 (model registry)
- AWS EC2 (deployment)
- Docker & AWS ECR
- GitHub Actions (CI/CD)

### API Layer
- FastAPI
- Jinja2 templates (web UI)
- Async request handling
- In-memory model caching

---

## Pipeline Breakdown

### 1. Data Ingestion
- Fetches raw documents from MongoDB Atlas
- Converts to pandas DataFrame
- Persists feature store artifacts

### 2. Data Validation
- Enforced via `schema.yaml`
- Column presence and data-type checks
- Validation report generated before training

### 3. Data Transformation
- Feature engineering & encoding
- Scaling and preprocessing pipeline
- Class imbalance handled using SMOTEENN
- Preprocessor saved as an artifact

### 4. Model Training
- RandomForest classifier
- Production-style training (no hyperparameter search)
- Metrics logged and stored

### 5. Model Evaluation
- Compares newly trained model with current production model
- Promotion occurs only if improvement exceeds a defined threshold
- Prevents silent performance regression

### 6. Model Registry
- Versioned model artifacts stored in AWS S3
- Loaded lazily and cached in memory during inference

---

## Model Performance (Latest Training Run)

| Metric     | Value |
|------------|-------|
| **F1 Score** | ~0.93 |
| **Precision** | ~0.88 |
| **Recall**   | ~0.99 |

Metrics reflect strong recall performance while maintaining acceptable precision.

---

## Inference API

The FastAPI service exposes:

| Route   | Method | Description                  |
|---------|--------|------------------------------|
| `/`     | GET    | Render prediction UI         |
| `/`     | POST   | Generate prediction          |
| `/train`| GET    | Trigger full training pipeline |

- Production model is loaded from S3
- Cached in memory to reduce latency and cloud costs

### Inference Optimization (Production Detail)

- The production model is loaded **once at application startup** using FastAPI lifespan events.
- The model artifact is fetched from **AWS S3 a single time** and cached **in memory**.
- All subsequent prediction requests reuse the same in-memory model instance.
- This design eliminates repeated S3 downloads, reduces inference latency, and minimizes cloud costs.

---

## CI/CD Workflow

```
Code Push
|
v
GitHub Actions
|
v
Docker Build
|
v
Push Image to AWS ECR
|
v
Deploy Container on EC2
```

The pipeline is fully automated from commit to deployment.

---

## Security & Configuration

- Secrets managed via environment variables
- IAM-based access control
- No credentials committed to version control
- Artifacts excluded from git history

---

## Why This Project Demonstrates Strong MLOps Engineering

- Clear separation of pipeline stages
- Schema enforcement before training
- Lifecycle-managed model loading with in-memory caching to avoid repeated cloud fetches during inference
- Model promotion gates
- Cloud-native deployment
- Cost-aware design decisions
- Resume-ready codebase

---

## Author

**Gautam**  
Computer Science Engineer | B.Tech (CSE)
Focus: **MLOps · Production ML Systems · Cloud Deployment · Backend Engineering**

---

⭐ This repository demonstrates how machine learning systems are **built, evaluated, deployed, and maintained** in real production environments.

````markdown