import requests
import time
from threading import Thread
key = 'key'
def on_sales():
    while True:
        sales_update1 = requests.get(f'https://market.csgo.com/api/v2/ping?key={key}')
        sales_update2 = requests.get(f'https://market.dota2.net/api/PingPong/?key={key}')
        print(sales_update1)
        print(sales_update2)
        time.sleep(181)
def set_order():
    hash_name = input('Введите hash-name предмета(Заглавными буквами с пробелами):\n')
    kolvo = input('Введите количество ордеров:\n')
    price = input('Введите цену в копейках:\n')
    buy_order_request = f'https://market.csgo.com/api/v2/set-order?key={key}&market_hash_name={hash_name}&count={kolvo}&price={price}'
    buy_order = requests.get(buy_order_request)
    print(buy_order.json())
def get_orders():
    get_orders_request = f'https://market.csgo.com/api/v2/get-orders?key={key}&page=0'
    get_orders = requests.get(get_orders_request)
    orders = get_orders.json()
    orders = orders['orders']
    for order in orders:
        print(order['hash_name'] + ' количество:' + order['count'] + ' цена: ' + order['price'])
def check_profit():
    buy_price = int(input('Введите цену(в копейках) за которую вы покупаете вещь:\n'))* 1.05
    sell_price = int(input('Введите цену(в копейках) за которую вы продаете вещь:\n')) * 0.87
    price = buy_price/sell_price
    print(price)
def main():
    while True:
        command = input('S - set_order\nG - get_orders\nP - check_profit\n')
        if command == 'S':
            set_order()
        elif command == 'G':
            get_orders()
        elif command == 'P':
            check_profit()
        else:
            pass
thread1 = Thread(target=on_sales)
thread2 = Thread(target=main)
thread1.start()
thread2.start()

