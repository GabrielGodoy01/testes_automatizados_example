import requests


class GetData:

    def get_data(url: str):
        response = requests.get(url)
        return response