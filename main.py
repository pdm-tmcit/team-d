import module.sentence_module as sentence
import module.status_module as status
import module.io_module as io
import module.token_module as tokens
import module.situation_module as situation
import module.name_module as name

def run(PATH):
    csv_path = PATH
    csv = io.csv_read(csv_path)
    terget_role = io.csv_terget(csv_path)

    

    if terget_role == None:
        print("入力データが不正です")
        exit

    status.init()
    tokenize_csv = tokens.token(csv)

    names = name.name_setlist(csv)
    nicknames = name.nickname_setlist(tokenize_csv)
    names_dict = name.name_dict(name.name_similar_nickname(names,nicknames))


    for n in names:
      status.save("プレイヤー名ID",str(names.index(n)),n)
      status.save("プレイヤー名",n,str(names.index(n)))
      status.save("プレイヤーニックネーム",str(names.index(n)),names_dict[n][0])

   
    situation.CO_check(csv)

    output_sentence = sentence.sentence_moddule(terget_role)
    io.csv_write(csv_path,output_sentence)

    print(output_sentence)


if __name__ == "__main__":
    run("sample/wolf/village_g12.csv")