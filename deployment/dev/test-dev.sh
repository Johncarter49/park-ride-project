#!/bin/bash

MY_IP=$(curl -s ifconfig.me)
URL="http://$MY_IP:30085/ride"

echo "[+] Detected Public IP: $MY_IP"
echo "[+] Sending request to $URL"

# Wait loop for up to 30 seconds
for i in {1..10}; do
  response=$(curl -s --max-time 2 "$URL")
  if [[ $response == *"["* ]]; then
    echo "[+] Response:"
    echo "$response"
    exit 0
  else
    echo "[!] No response yet, retrying in 3 seconds... ($i/10)"
    sleep 3
  fi
done

echo "[x] Error: App did not respond within timeout."
exit 1