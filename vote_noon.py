import json
import requests
import sys


class Character:
    at_context = "https://werewolf.world/village/context/0.3/character.jsonld"
    at_id = "https://licos.online/state/0.3/village#3/character"
    is_mine = None
    name = {'ja': '', 'en': ''}
    image = ""
    id = 0
    status = ""
    update = {'@id'}


my_character = None


def main():
    url = "https://werewolf.world/village/example/0.3/client2server/noonVote.jsonld"
    args = sys.argv
    response = requests.get(url)
    json_data = response.json()
    get_phase_noon()
    print(vote(json_data, int(args[1]), get_phase_noon()))


# 午後のフェーズのjsonを取得してキャラクターのリストを返す
def get_phase_noon():
    url = "https://werewolf.world/village/example/0.3/server2client/noon.jsonld"
    response = requests.get(url)
    json_data = response.json()
    character_list = []

    for character in json_data['character']:
        if character['isMine']:
            my_character = character
        character_list.append(character)

    return character_list


# jsonと投票する人のid、キャラクターのリストを受け取ってvoteのjsonを生成する
def vote(json_data, id, character_list):
    for target in character_list:
        if target['id'] == id:
            json_data['character']['id'] = target['id']
            json_data['character']['name']['en'] = target['name']['en']
            json_data['character']['name']['ja'] = target['name']['ja']
            json_data['character']['image'] = target['image']

    return json_data


if __name__ == "__main__":
    main()
