## 🚀 Quickstart Guide – Local & Kubernetes Deployment

### Step 1: Test the App Locally via Docker

```
# Pull the public Docker image
docker pull registry.gitlab.com/jhiberne/theme-park-ride-gradle:latest

# Run the container locally
docker run -d --name theme-park-ride -p 80:5000 \
  registry.gitlab.com/jhiberne/theme-park-ride-gradle:latest

# Test the endpoint
curl http://localhost/ride

# Stop and remove the container
docker rm -f theme-park-ride
```

---

### Step 2: Deploy to Kubernetes (Dev Environment)

```
# Pull latest Kubernetes changes
git pull origin develop

# Deploy to the cluster using predefined manifests
cd theme-park-devops/deployment/dev
./deploy-dev.sh

# Test the running app (Option 1 - in browser)
http://<YOUR_VM_IP>:30085/ride

# OR (Option 2 - test script)
./test-dev.sh
```

> The output should match the Docker test response.

---

### Step 3: Deploy with Terraform + Helm

Terraform configuration is available under `deployment/terraform` and installs the existing Helm chart (`deployment/charts/theme-park-ride`) into your cluster.

```
cd deployment/terraform
cp terraform.tfvars.example terraform.tfvars

# Optional: edit terraform.tfvars (environment=dev|prod, namespace, context)
terraform init
terraform plan
terraform apply
```

To remove resources:

```
terraform destroy
```
