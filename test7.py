summa = int(input("Минимальная сумма инвестиций - "))
mike=int(input("Сколько долларов инвестирует Майкл - "))
ivan=int(input("Сколько долларов инвестирует Иван - "))
if (mike >= summa) and (ivan >= summa) and (mike + ivan >= summa):
	print(2)
elif (mike >= summa) and (ivan <= 0):
	print("Mike")
elif (mike <= 0) and (ivan >= summa):
	print("Ivan")
elif (mike + ivan >= summa):
	print(1)
elif (mike <= 0) and (ivan <= 0):
	print(0)
 