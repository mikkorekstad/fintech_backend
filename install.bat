echo "Installing python39-venv"
conda create -n fintechpy39 python=3.9 anaconda

echo "Creating python virtual environment"
conda activate fintechpy39

echo "Upgrading pip"
pip install --upgrade pip
echo "Pip install wheel"
pip install wheel
echo "Pip install requirements.txt"
pip install -r requirements.txt

echo "Install complete"
