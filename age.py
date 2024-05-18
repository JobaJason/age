drive = input ('你有開過車嗎?')
if drive == '有':
	age = input ('請輸入你的年齡: ')
	age = int(age)
	if age >= 18:
		print ('ok 沒問題')
	else:
		print ('不行,你無照駕駛')
else:
	print ('好,沒事') #其他選項