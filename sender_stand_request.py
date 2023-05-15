import configuration
import requests
import data

#Функция на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)

def get_order_data(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_NUMBER + track)
'''
response = post_new_order(data.create_order_body)
track = str(response.json()['track'])
response_order = get_order_data(track)
print(response_order.status_code)
'''
