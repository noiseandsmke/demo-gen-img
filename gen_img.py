import requests
def reqGenImg(prompt: str):
    url = "https://api.limewire.com/api/image/generation"

    payload = {
    "prompt": prompt,
    "aspect_ratio": "1:1"
    }

    headers = {
    "Content-Type": "application/json",
    "X-Api-Version": "v1",
    "Accept": "application/json",
    "Authorization": "Bearer lmwr_sk_DrjsmxRI5H_USeeIw2InSZPYogxbzuI0Nd1YgaVMEPgX9d79"
    }

    response = requests.post(url, json=payload, headers=headers)
    # return response.json()

    first_image_data = response.json()['data'][0]
    return first_image_data.get('asset_url')
