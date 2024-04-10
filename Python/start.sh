#!/bin/bash
cd /home/peter
source /home/peter/.env 
source /home/peter/.venv/bin/activate
cd /home/peter/sunwriter/Python
sleep 10
git pull
python ./chatgpt-test.py 

