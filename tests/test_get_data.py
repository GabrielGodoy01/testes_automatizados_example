import requests

from src.get_data import GetData


class Test_GetData() :

    def test_get_data(self) :

        result = GetData.get_data(url="https://pokeapi.co/api/v2/pokemon/1/")

        assert result.status_code == 200
        assert result.json()["forms"][0]["name"]  == "bulbasaur"

    def test_get_data_failed(self):
        result = GetData.get_data(url="https://pokeapi.co/api/v2/pokem/1/")

        assert result.status_code == 404