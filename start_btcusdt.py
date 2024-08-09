import subprocess

BASE_ASSET = 'BTC'
QUOTE_ASSET = 'USDT'
coefficient = 1.2

# Вызов blzusdt.py со значениями BASE_ASSET, QUOTE_ASSET и coefficient
subprocess.run(["python3", "trading.py", BASE_ASSET, QUOTE_ASSET, str(coefficient)])
