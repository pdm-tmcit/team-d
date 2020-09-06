import module.status_module as status
import module.io_module as io
import module.sentence_module as sentence

def test_status_module():
    player = ["ならず者ディーター","パン屋オットー","仕立て屋エルナ","少女リーザ","少年ペーター","旅人ニコラス","木こりトーマス","楽天家ゲルト","神父ジムゾン","羊飼いカタリナ","行商人アルビン","負傷兵シモン","農夫ヤコブ","青年ヨアヒム"]
    status.init()
    status.save("霊媒師","OCしてる",1)
    print(status.load("霊媒師","OCしてる"))
    for n in player:
      status.save("プレイヤー名ID",str(player.index(n)),n)
      status.save("プレイヤー名",n,str(player.index(n)))
    for id in range(len(player)):
      print(id,status.load("プレイヤー名ID",str(id)))

def test_io_module():
    io.csv_read("sample/wolf/village_g21.csv")
    print(io.csv_terget("sample/wolf/village_g21.csv"))

def test_sentence_module():
  status.init()
  dict = ["人狼","占い師","村人","狂人","狩人","霊能者"]
  for role_name in dict:
    print(role_name)
    print(sentence.sentence_moddule(role_name))

if __name__ == "__main__":
    print("### test_io_module ###")
    test_io_module()
    print("### test_sentence_module ###")
    test_sentence_module()
    print("### test_status_module ###")
    test_status_module()