import re

dict = ["人狼","占い師","村人","狂人","狩人","霊能力者","霊能者"]

def CO_check(token):
  for part in token:
    if part[0] == 'プロローグ':
      continue
    if part[2] != '':
      if '■' in part[3]:
        continue
      m = re.match(r'【.*】',part[3])
      if m != None:
        n = re.match(r'【.*[^非].*】',part[3])
        if n !=None:
          l = re.findall(r'【.*】',part[3])
          #print(l)
          for role in dict:
            for match_part in l:
              if (role in match_part)==True:
                print(role)
          #print(part[3])
      """
      if '【' in part[3] and '】' in part[3]:
        if 'CO' in part[3].upper():
          print(part)
      """