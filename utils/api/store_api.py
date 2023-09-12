import requests

from config_data.config import API_STORE_KEY, API_STORE_BASE_URL, API_STORE_HOST


def GetProduct(product_id):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'catalog/product/{product_id}'
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.get(url, headers=headers)

    match response.status_code:
        case 200:
            raw_data = response.json()
            data = f"{raw_data['name']}:\nЦена {raw_data['price']}, категория {raw_data['category']}."
            return data

        case _:
            return None


def GetProductsInCategory(category_name, skip=0):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'catalog/category/{category_name}/products'
    querystring = {'skip': skip,'limit': '10'}
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.get(url, params=querystring, headers=headers)

    match response.status_code:
        case 200:
            raw_data = response.json()
            for i in raw_data['products'].items():
                data = f"{raw_data['name']}, id {raw_data['id']}."
                yield data

        case _:
            return None


def CreateProduct(product_name, price, category_name):
    headers = {'content-type': 'application/json',
               'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = 'catalog/product'
    payload = {'name': f'{product_name}',
               'price': f'{price}',
               'manufacturer': '',
               'category': f'{category_name}',
               'description': '',
               'tags': ''}
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.post(url, json=payload, headers=headers)

    match response.status_code:
        case 201:
            raw_data = response.json()
            data = f"Создан товар {raw_data['name']} c id {raw_data['id']}.\nЦена {raw_data['price']}, категория {raw_data['category']}."
            return data

        case _:
            return None


def DeleteProduct(product_id):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'catalog/product/{product_id}'
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.delete(url, headers=headers)

    match response.status_code:
        case 200:
            raw_data = response.json()
            data = f"Товар с id {raw_data['id']} успешно удален."
            return data

        case _:
            return None


def CreateOrder(user_name, user_address):
    headers = {'content-type': 'application/json',
               'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = 'order/new'
    payload = {'customer': f'{user_name}',
               'address': f'{user_address}'}
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.post(url, json=payload, headers=headers)

    match response.status_code:
        case 201:
            raw_data = response.json()
            data = f"Создан заказ {raw_data['id']}.\nДата создания {raw_data['created']}.\nПолучатель {user_name}, адрес {user_address}."
            return data

        case _:
            return None


def AddToOrder(order_id, product_id):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'order/{order_id}/product/{product_id}'
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.post(url, headers=headers)

    match response.status_code:
        case 201:
            raw_data = response.json()
            print(raw_data)
            data = f"Товар с id {product_id} успешно добавлен в заказ {order_id}."  # TODO
            return data

        case _:
            return None


def DeleteFromOrder(order_id, product_id):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'order/{order_id}/product/{product_id}'
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.delete(url, headers=headers)

    match response.status_code:
        case 200:
            raw_data = response.json()
            print(raw_data)
            data = f"Товар с id {product_id} успешно удален из заказа {order_id}."  # TODO
            return data

        case _:
            return None


def GetOrder(order_id):
    headers = {'X-RapidAPI-Key': API_STORE_KEY, 
               'X-RapidAPI-Host': API_STORE_HOST}

    suffix = f'order/{order_id}'
    url = f'{API_STORE_BASE_URL}{suffix}'

    response = requests.get(url, headers=headers)

    match response.status_code:
        case 200:
            raw_data = response.json()
            data = f"Заказ {raw_data['order']['id']} взят в работу? {raw_data['order']['created']}.\n "\
                   f"Получатель {raw_data['order']['customer']}, адрес {raw_data['order']['address']}.\n "\
                   f"Всего товаров: {raw_data['summary']['totalItems']}. Суммарная стоимость: {raw_data['summary']['totalCost']}.\n\n "\
                   f"Список товаров:\n{raw_data['items']}"
            return data

        case _:
            return None
