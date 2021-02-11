sudo apt-get upgrade -y
sudo apt-get update -y
sudo apt install python3.8 -y
sudo apt-get install python3-venv -y
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt