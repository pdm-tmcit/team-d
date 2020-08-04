# -*- coding: utf-8 -*-
import spacy

def name_setlist(token):
  nameset=set()
  for part in token:
    nameset.add(part[1])
  return list(nameset)

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
  return list(nameset)

def name_similar_nickname(names, nicknames):
  nlp = spacy.load('ja_ginza')
  names_list = []
  for name in names:
    name_list = []
    for nickname in nicknames:
      doc1 = nlp(name)
      doc2 = nlp(nickname)
      vec = doc1.similarity(doc2)
      if vec >= 0.65:
        name_list.append((nickname, vec))
    names_list.append(name_list)
  name_dict = dict(zip(names, names_list))
  return name_dict

def name_dict_can(token):
  names = name_setlist(token)
  nicknames = nickname_setlist(token)
  name_dict_can = name_similar_nickname(names, nicknames)
  return name_dict_can

def name_dict(names_dict_can):
  names_dict = {}
  for key in names_dict_can:
    value=("",0)
    for name_value in names_dict_can[key]:
      if name_value[1] > value[1]:
        value=(name_value[0],name_value[1])
    names_dict[key]=value
  return names_dict

if __name__ == "__main__":
  names_dict_can = name_dict_can(token)
  names_dict = name_dict(names_dict_can)
  #print(names_dict, file=f)