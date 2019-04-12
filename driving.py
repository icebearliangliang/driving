country = input('please input your country: ')
age = input('please input your age: ')
age = int(age)
if country == 'China':
	if age >= 18:
		print('you can get a driving license')
	else:
		print("you can't get a driving license yet")
elif country == 'American':
	if age >= 16:
		print('you can get a driving license')
	else:
		print("you can't get a driving license yet")
else:
	print('you can only input China or American')