import websocket
import datetime
import sys
import db

def on_message(ws, message):
    print()
    print(str(datetime.datetime.now()) + ": ")
    print(message)
    db.log_db(message)

def on_error(ws, error):
    print(error)

def on_close(close_msg):
    print(" CLOSED " + close_msg)

def streamKline(currency, interval):
    websocket.enableTrace(False)
    socket = f'wss://stream.binance.com:9443/ws/{currency}@kline_{interval}'
    ws = websocket.WebSocketApp(socket, 
                                on_message=on_message,
                                on_error=on_error, 
                                on_close=on_close)
    ws.run_forever()

db.init_db()

if __name__ == "__main__":
    symbol = sys.argv[1]
    interval = sys.argv[2]

    print("symbol: " + symbol)
    print("interval: " + interval)

    streamKline(symbol, interval)
