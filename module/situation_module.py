def CO_check(token):
  for part in token:
    if part[0] == 'プロローグ':
      continue
    if part[2] != '':
      if '■' in part[3]:
        continue
      if '【' in part[3] and '】' in part[3]:
        if 'CO' in part[3].upper():
          print(part)