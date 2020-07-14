import spacy
import pprint

nlp = spacy.load('ja_ginza')
print('文章を入力')
str = input()
doc = nlp(str)
result_list = []
for sent in doc.sents:
    for token in sent:
        info_dict = {}
        info_dict["num"]             = token.i             # トークン番号（複数文がある場合でも0に戻らず連番になる）
        info_dict["text"]         = token.orth_         # オリジナルテキスト
        info_dict["reading"]     = token._.reading     # 読み仮名
        info_dict["pos_"]          = token.pos_          # 品詞(UD)
        info_dict["tag_"]          = token.tag_          # 品詞(日本語)
        info_dict["lemma_"]        = token.lemma_        # 基本形（名寄せ後）
        info_dict["inf"]         = token._.inf         # 活用情報
        info_dict["rank"]          = token.rank          # 頻度のように扱えるかも
        info_dict["norm_"]         = token.norm_         # 原型
        info_dict["is_oov"]        = token.is_oov        # 登録されていない単語か？
        info_dict["is_stop"]       = token.is_stop       # ストップワードか？
        info_dict["has_vector"]    = token.has_vector    # word2vecの情報を持っているか？
        info_dict["list(.lefts)"]   = list(token.lefts)   # 関連語まとめ(左)
        info_dict["list(.rights)"]  = list(token.rights)  # 関連語まとめ(右)
        info_dict["dep_"]          = token.dep_          # 係り受けの関係性
        info_dict["head.i"]        = token.head.i        # 係り受けの相手トークン番号
        info_dict["head.text"]     = token.head.text     # 係り受けの相手のテキスト
        result_list.append(info_dict)



for i in result_list:
    pprint.pprint(i)
    print('\n')