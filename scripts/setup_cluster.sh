
#!/bin/bash

echo "Setting up Cluster environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements/base.txt
pip install -r requirements/dev.txt
echo "Cluster setup complete. Use 'source venv/bin/activate' to activate the environment."
