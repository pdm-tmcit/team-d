import module.sentence_module as sentence
import module.status_module as status
import module.io_module as io
import module.token_module as tokens
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
    #print(tokenize_csv)
    #print(terget_role)
    output_sentence = sentence.sentence_moddule(terget_role)
    #output_sentence = sentence.sentence_moddule('占い師')
    print(output_sentence)