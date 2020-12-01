import json
import requests


def main():
    # URLは自分の担当箇所に変更
    url = "https://werewolf.world/village/example/0.3/server2client/noon.jsonld"
    response = requests.get(url)
    json_data = response.json()
    some_module(json_data)


def some_module(json_data):
    print(json_data['day'], "日目")

    for i in json_data['character']:
        print(i['name']['ja'], " : ", i['status'])


if __name__ == "__main__":
    main()
