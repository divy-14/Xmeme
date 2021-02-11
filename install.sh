#!/bin/bash
sudo apt-get upgrade -y
sudo apt-get update -y
sudo apt install python3.8 -y
sudo apt-get -y install python3-pip
sudo apt-get install curl -y
pip3 install -r requirements.txt