import module.sentence_module as sentence
import module.status_module as status
import module.io_module as io
import module.token_module as tokens
import module.name_module as name
import module.situation_module as situation

if __name__ == "__main__":
    csv_path = "sample/wolf/village_g21.csv"
    csv = io.csv_read(csv_path)
    terget_role = io.csv_terget(csv_path)

    #tokenize_csv = tokens.token(csv)
    situation.CO_check(csv)


    if terget_role == None:
        print("入力データが不正です")
        exit

    status.init()
    tokenize_csv = tokens.token(csv)

    names = name.name_setlist(csv)
    nicknames = name.nickname_setlist(tokenize_csv)
    names_dict = name.name_dict(name.name_similar_nickname(names,nicknames))

    #print("### names_dict ###")
    #print(names_dict)

    for n in names:
      status.save("プレイヤー名ID",str(names.index(n)),n)
      status.save("プレイヤー名",n,str(names.index(n)))
      status.save("プレイヤーニックネーム",str(names.index(n)),names_dict[n][0])

    #for id in range(len(names)):
    #  print(id,status.load("プレイヤー名ID",str(id)))
    #  print(id,status.load("プレイヤーニックネーム",str(id)))

    #print("### CO_check ###")
    situation.CO_check(csv)

    #print(tokenize_csv)
    #print(terget_role)
    output_sentence = sentence.sentence_moddule(terget_role)
    #output_sentence = sentence.sentence_moddule('占い師')
    print(output_sentence)