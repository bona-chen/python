admit=input("请输入年份:")
if admit.isdigit()==0:
	admit=input("请输入阿拉伯数字:")
year=int(admit)
if year%400==0:
	print("该年份是闰年")
elif year%100==0:
	print("该年份不是闰年")
elif year%4==0:
	print("该年份是闰年")
else:
	print("该年份不是闰年")
