def load(role_name,key):
	if role_name == '占い師' :
		if key == '自身がCOしているか' :
			return True
		elif key == 'スキル対象':
			uid = 2
			return uid
		elif key == 'スキル結果':
			return False
		elif key == '占いを既に言ったか':
			return False
		else:
			return
	else:
		return

def save(role_name,key,value):
	if role_name == '占い師':
		if key == '自身がCOしているか' and value == True:
			return
		else:
			return
	else:
		return 

