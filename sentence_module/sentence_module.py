# -*- coding: utf-8 -*-
import status_module_demo as status

def sentence_moddule(role_name):
	uid_dict = {1:'ならず者ディーター',2:'シスターフレーデル'}
	ans_dict = {True:'白',False:'黒'}

	if role_name == '占い師' :

		if status.load(role_name,'自身がCOしているか') == False:
			status.save(role_name,'自身がCOしているか',True)
			return '私は占い師です。'

		elif status.load(role_name,'占いを既に言ったか',) == False:
			status.save(role_name,'占いを既に言ったか',True)
			uid = status.load(role_name,'スキル対象')
			ans = status.load(role_name,'スキル結果')
			return ('%sは%sでした。' %(uid_dict[uid],ans_dict[ans]))

		elif status.load(role_name,'占い先を指定されたか') == True:
			status.save(role_name,'占い先を指定されたか',False)
			uid = status.load(role_name,'占い先指定')
			return ('%sさんを占います。' %(uid_dict[uid]))

		else:
			return '今日もいい天気	'

	elif role_name == '霊媒師':
		return '今日もいい天気	'

	elif role_name == '狂人':
		return '今日もいい天気	'

	elif role_name == '狩人':
		return '今日もいい天気	'

	elif role_name == '共有者':
		return '今日もいい天気	'

	elif role_name == '村人':
		return '今日もいい天気	'

	elif role_name == '人狼':
		return '今日もいい天気	'


	else:
		return


def main():
	while True:
		print('Input:role name')
		text = input()
		print('Output:sentences ')
		print(sentence_moddule(text))
		if text == '':
			break


if __name__ == "__main__":
    main()
	