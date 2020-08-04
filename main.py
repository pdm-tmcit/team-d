import module.sentence_module as sentence
import module.status_module as status
import module.io_module as io

if __name__ == "__main__":
    csv_path = "sample/wolf/village_g21.csv"
    terget_rool = io.csv_terget(csv_path)

    if terget_rool == None:
        print("入力データが不正です")
        exit

    output_sentence = sentence.sentence_moddule(terget_rool)
    print(output_sentence)