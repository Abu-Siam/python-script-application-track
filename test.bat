@echo off
pip3 install -r requirements.txt
timeout /t 10
start python main.py  %* & start python send_email.py %*
pause