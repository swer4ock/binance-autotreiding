import subprocess

BASE_ASSET = 'BTC'
QUOTE_ASSET = 'RUB'
coefficient = 1.2

# Вызов blzusdt.py со значениями BASE_ASSET, QUOTE_ASSET и coefficient
subprocess.run(["python3", "blzusdt2.py", BASE_ASSET, QUOTE_ASSET, str(coefficient)])
