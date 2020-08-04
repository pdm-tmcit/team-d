import module.status_module as status
import module.io_module as io
import module.sentence_module as sentence

def test_status_module():
    status.init()
    status.save("霊媒師","OCしてる",1)
    print(status.load("霊媒師","OCしてる"))

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
    # test_status_module()
    print("### test_io_module ###")
    test_io_module()
    print("### test_sentence_module ###")
    test_sentence_module()