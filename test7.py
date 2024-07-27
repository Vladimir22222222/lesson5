summa = int(input("Минимальная сумма инвестиций - "))
mike=int(input("Сколько долларов инвестирует Майкл - "))
ivan=int(input("Сколько долларов инвестирует Иван - "))
if (mike >= summa) and (ivan >= summa) and (mike + ivan >= summa):
	print(2)
elif (mike >= summa) and (ivan <= summa):
	print("Mike")
elif (mike <= summa) and (ivan >= summa):
	print("Ivan")
elif (mike + ivan >= summa):
	print(1)
elif (mike <= summa) and (ivan <= summa):
	print(0)
 