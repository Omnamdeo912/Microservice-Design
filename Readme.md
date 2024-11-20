# Microservices Architecture
This project is a microservices-based architecture designed to provide a scalable and modular solution. Each microservice is an independent Flask application that performs a specific function. The microservices communicate with each other using REST APIs, and the entire system is containerized using Docker and orchestrated using Kubernetes.

This repository contains a microservices-based architecture with the following components:

## Services

### 1. Auth Service
- **Location:** `auth/`
- **Description:** Handles user authentication and authorization.
- **Endpoints:**
  - `POST /login`: User login
  - `POST /register`: User registration

### 2. Converter Service
- **Location:** `converter/`
- **Description:** Handles file conversion tasks.
- **Endpoints:**
  - `POST /convert`: Convert files

### 3. Gateway Service
- **Location:** `gateway/`
- **Description:** Acts as an API gateway, routing requests to the appropriate microservices.
- **Endpoints:**
  - `GET /`: Health check
  - `POST /auth/*`: Proxy to Auth Service
  - `POST /convert/*`: Proxy to Converter Service

### 4. Notification Service
- **Location:** `notification/`
- **Description:** Handles sending notifications.
- **Endpoints:**
  - `POST /send`: Send notifications

### 5. RabbitMQ
- **Location:** `rabbit/`
- **Description:** Message broker for inter-service communication.

## Kubernetes Deployment

### Steps to Deploy:

1. **Start Minikube:**
   ```bash
   minikube start
   ```
2. **Deploy Kubernetes**
    - kubectl apply -f auth/manifests/
    - kubectl apply -f converter/manifests/
    - kubectl apply -f gateway/manifests/
    - kubectl apply -f notification/manifests/
    - kubectl apply -f rabbit/manifests/

