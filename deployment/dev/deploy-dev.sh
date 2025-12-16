#!/bin/bash
set -e

NAMESPACE="dev"

echo "[+] Ensuring namespace '$NAMESPACE' exists..."
kubectl get ns $NAMESPACE >/dev/null 2>&1 || kubectl create ns $NAMESPACE

echo "[+] Cleaning up old resources (if any)..."
kubectl delete all --all -n $NAMESPACE --ignore-not-found
kubectl delete ingress --all -n $NAMESPACE --ignore-not-found

echo "[+] Applying fresh manifests..."
kubectl apply -f namespace.yaml
kubectl apply -f service.yaml
kubectl apply -f deployment.yaml
kubectl apply -f ingress.yaml

echo "[+] Done. Current state in '$NAMESPACE':"
kubectl get all -n $NAMESPACE