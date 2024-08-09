from binance.client import Client
import time

API_KEY = 'LmnKGBTeUUWdxRPN6TAjlCgUP5A0K2cwIzydqkU3r2N03mWtlhCgU8IRVobwSqLr'  # Замените на ваш API ключ
API_SECRET = 'ySD7lElbzfPQ8Vst1saE0PVS7MHkFqVnLMpkt8ffmSDUCNdOz3szc73nIe0yzDRD'  # Замените на ваш секретный ключ

client = Client(API_KEY, API_SECRET)

def get_market_depth(symbol, limit=5):
    """ Получить глубину стакана для данного символа """
    depth = client.get_order_book(symbol=symbol, limit=limit)
    
    best_ask = float(depth['asks'][0][0])
    best_bid = float(depth['bids'][0][0])

    return best_ask, best_bid

symbol = "BTCUSDT"

while True:
    best_ask, best_bid = get_market_depth(symbol)

    print(f"\nВерхняя цена  {symbol}: {best_ask}")
    print(f"Нижняя цена {symbol}: {best_bid}")

    time.sleep(3)  # Пауза в 3 секунды перед следующим запросом
