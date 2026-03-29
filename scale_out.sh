#!/bin/bash
echo "Initiating cloud burst sequence..."
echo "Resizing GCP Managed Instance Group (vcc-mig) to size 1..."

gcloud compute instance-groups managed resize vcc-mig --size=1 --zone=asia-south1-a --quiet

echo "GCP VM is provisioning. Waiting 15 seconds for Google to assign a Public IP..."
sleep 15

# Automatically fetch the newly assigned IP so we don't have to hunt for it in the console
PUBLIC_IP=$(gcloud compute instances list --filter="name~'vcc-mig.*'" --format="get(networkInterfaces[0].accessConfigs[0].natIP)" | head -n 1)

echo "====================================================="
echo "Workload Migrated Successfully!"
echo "Open this link in your host browser: http://$PUBLIC_IP:5000"
echo "====================================================="
