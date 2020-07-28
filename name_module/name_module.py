# -*- coding: utf-8 -*-
import spacy
import csv

"""
test= [
  ["プロローグ","楽天家ゲルト","村人","人狼なんているわけないじゃん。"],
  ["プロローグ","少女リーザ","村人","こ、こんにちは！村の立て看板は読んできたよ（ルール確認）"],
  ["プロローグ","パン屋オットー","人狼","今はリーザ、ヤコブ、ヴァルターがいるねぇ。"]]
"""

def token_part(test,nlp):
  doc = nlp(test)
  result_list = []
  for sent in doc.sents:
    for token in sent:
      info_dict = {}
      info_dict["num"]             = token.i             # トークン番号（複数文がある場合でも0に戻らず連番になる）
      info_dict["text"]         = token.orth_         # オリジナルテキスト
      info_dict["pos_"]          = token.pos_          # 品詞(UD)
      info_dict["inf"]         = token._.inf         # 活用情報
      info_dict["rank"]          = token.rank          # 頻度のように扱えるかも
      info_dict["is_oov"]        = token.is_oov        # 登録されていない単語か？
      info_dict["list(.lefts)"]   = list(token.lefts)   # 関連語まとめ(左)
      info_dict["list(.rights)"]  = list(token.rights)  # 関連語まとめ(右)
      info_dict["dep_"]          = token.dep_          # 係り受けの関係性
      info_dict["head.i"]        = token.head.i        # 係り受けの相手トークン番号
      info_dict["head.text"]     = token.head.text     # 係り受けの相手のテキスト
      result_list.append(info_dict)
  return result_list

def token(test):
  nlp = spacy.load('ja_ginza')
  for part in test:
    res = token_part(part[3], nlp)
    #print(res)
    part.append(res)
  return test

def name_setlist(token):
  nameset=set()
  for part in token:
    nameset.add(part[1])
  return nameset

def nickname_setlist(token):
  nameset=set()
  for part in token:
    for info in part[4]:
      try:
        if info["pos_"] == "PROPN":
          nameset.add(info["text"])
      except:
        nlp = spacy.load('ja_ginza')
        ex_token = token_part(info, nlp)
        """
        print(type(info))
        print('\033[31m'+info+'\033[0m')
        print(ex_token)
        """
        for ex_info in ex_token:
          if ex_info["pos_"] == "PROPN":
            nameset.add(ex_info["text"])
  return nameset

def csv_read(a):
  with open(a, encoding="utf-8") as f:
    reader = csv.reader(f)
    l = [row for row in reader]
  return l

if __name__ == "__main__":
  test=csv_read("village_g1947.csv")
  token=token(test)
  #f = open('/mnt/a/PG/python/pdm/team-d/name_module/res.txt', 'a')
  #print(token, file=f)
  print(name_setlist(token))
  print(nickname_setlist(token))