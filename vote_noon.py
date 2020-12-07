import json
import requests


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
character_list = []


def main():
    # URLは自分の担当箇所に変更
    url = "https://werewolf.world/village/example/0.3/client2server/noonVote.jsonld"
    response = requests.get(url)
    json_data = response.json()
    get_phase_noon()
    print(vote(json_data, 2))


def get_phase_noon():
    url = "https://werewolf.world/village/example/0.3/server2client/noon.jsonld"
    response = requests.get(url)
    json_data = response.json()

    for character in json_data['character']:
        if character['isMine']:
            my_character = character
        character_list.append(character)

    # print(my_character)
    # print(character_list)


def vote(json_data, id):
    """
    jsonと投票する人のidを受け取ってvoteのjsonを生成する
    """
    #print(json_data['day'], "日目")

    # TODO: phase_noonから生存キャラクターのid, キャラ名, imageを受け取って持ってくるようにする。
    for target in character_list:
        if target['id'] == id:
            json_data['character']['id'] = target['id']
            json_data['character']['name']['en'] = target['name']['en']
            json_data['character']['name']['ja'] = target['name']['ja']
            json_data['character']['image'] = target['image']

    print(json_data)
    return json_data


    # kokoni書いてちょ
if __name__ == "__main__":
    main()
