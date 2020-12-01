import json
import requests


def main():
    # URLは自分の担当箇所に変更
    url = "https://werewolf.world/village/example/0.3/server2client/noon.jsonld"
    response = requests.get(url)
    json_data = response.json()
    some_module(json_data)


def some_module(json_data):
    print(json_data)

    # kokoni書いてちょ
if __name__ == "__main__":
    main()
