import requests

def create_work(api_key, owned_by, product_id):
    url= "https://api.devrev.ai/works.create"
    data = {
        "type": "issue",
        "applies_to_part": product_id,
        "owned_by": [owned_by],
        "title": "Work",
        
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Issue creation successful!")
        print(response.json())  # Print the response content
        return response.json()["work"]["id"]
    else:
        print("Error creating issue:")
        print(response.text)
        return None

def create_parts(api_key, url, owned_by, product_id):
    data = {
        "type": "capability",
        "name": "RCB",
        "owned_by": [owned_by],
        "parent_part": [product_id],
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Part creation successful!")
        print(response.json())
        part_id = response.json()["part"]["id"]
        create_work(api_key, owned_by, part_id)
        return part_id
    else:
        print("Error creating part:")
        print(response.text)
        return None

def create_product(api_key, url, owned_by):
    data = {
        "type": "product",
        "name": "ankith",
        "owned_by": [owned_by],
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print("Product creation successful!")
        print(response.json())
        product_id = response.json()["part"]["id"]
        create_parts(api_key, url, owned_by, product_id)
        return product_id
    else:
        print("Error creating product:")
        print(response.text)
        return None

api_key = "eyJhbGciOiJSUzI1NiIsImlzcyI6Imh0dHBzOi8vYXV0aC10b2tlbi5kZXZyZXYuYWkvIiwia2lkIjoic3RzX2tpZF9yc2EiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOlsiamFudXMiXSwiYXpwIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFxbjZoMFYwU1M6ZGV2dS8xIiwiZXhwIjoxODA3MDg2MzEzLCJodHRwOi8vZGV2cmV2LmFpL2F1dGgwX3VpZCI6ImRvbjppZGVudGl0eTpkdnJ2LXVzLTE6ZGV2by9zdXBlcjphdXRoMF91c2VyL2dvb2dsZS1vYXV0aDJ8MTA4NjgxNDA5ODQwMTA3NDY1NTQwIiwiaHR0cDovL2RldnJldi5haS9hdXRoMF91c2VyX2lkIjoiZ29vZ2xlLW9hdXRoMnwxMDg2ODE0MDk4NDAxMDc0NjU1NDAiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9fZG9uIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFxbjZoMFYwU1MiLCJodHRwOi8vZGV2cmV2LmFpL2Rldm9pZCI6IkRFVi0xcW42aDBWMFNTIiwiaHR0cDovL2RldnJldi5haS9kZXZ1aWQiOiJERVZVLTEiLCJodHRwOi8vZGV2cmV2LmFpL2Rpc3BsYXluYW1lIjoiNG5tMjBjbTAwNSIsImh0dHA6Ly9kZXZyZXYuYWkvZW1haWwiOiI0bm0yMGNtMDA1QG5tYW1pdC5pbiIsImh0dHA6Ly9kZXZyZXYuYWkvZnVsbG5hbWUiOiI0Tk0yMENNMDA1IEFua2l0aCBIIiwiaHR0cDovL2RldnJldi5haS9pc192ZXJpZmllZCI6dHJ1ZSwiaHR0cDovL2RldnJldi5haS90b2tlbnR5cGUiOiJ1cm46ZGV2cmV2OnBhcmFtczpvYXV0aDp0b2tlbi10eXBlOnBhdCIsImlhdCI6MTcxMjQ3ODMxMywiaXNzIjoiaHR0cHM6Ly9hdXRoLXRva2VuLmRldnJldi5haS8iLCJqdGkiOiJkb246aWRlbnRpdHk6ZHZydi11cy0xOmRldm8vMXFuNmgwVjBTUzp0b2tlbi9yYVpMS1IwSyIsIm9yZ19pZCI6Im9yZ18wRVlLM3Y3VlNVbEZGSlhxIiwic3ViIjoiZG9uOmlkZW50aXR5OmR2cnYtdXMtMTpkZXZvLzFxbjZoMFYwU1M6ZGV2dS8xIn0.lCPunWkHQhgWH-ajXbCWBvTU3nVnuSgN6mQGIpIsSYo8fKimNsh0RHL_q9Abls1d2kY6C9FwAnGIuDh0-e6Bss72h1nAHq0OvoQd5TW_p13IEkeEtHoHmvK4QQQ7-XIk9X2d0cUP13NQQz7r_0jHqXkzxaLMcn58hgAjJ5S9ak-oDs7pTd3782uaFgbWQ1UPGc4tfgdvEmO3GqWzdtsqWtvMe2YUscIwUz7Ylr9NLKc66hs0ia6kt_TLmizzQre75eXmpgaFpS76LBp_HUtlXm98VHZYjWfU9IoARDo30a9xew2612eRtSzKOzUXbhNgO_2lKS3nErcY3BK6Y-KJ0A"
url = "https://api.devrev.ai/parts.create"
owned_by = "don:identity:dvrv-us-1:devo/1qn6h0V0SS:devu/1"

create_product(api_key, url, owned_by)
