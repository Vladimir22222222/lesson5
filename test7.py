#У Майкла A долларов, у Ивана B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.


summa = int(input("Минимальная сумма инвестиций - "))
mike=int(input("Сколько долларов инвестирует Майкл - "))
ivan=int(input("Сколько долларов инвестирует Иван - "))
if (mike > 0) and (ivan > 0) and (mike + ivan >= summa):
	print(2)
elif (mike > 0) and (ivan < 0):
	print("Mike")
elif (mike < 0) and (ivan > 0):
	print("Ivan")
elif (mike + ivan > summa):
	print(1)
elif (mike <= 0) and (ivan <= 0):
	print(0)
 #(mike < summa) and (ivan < summa)