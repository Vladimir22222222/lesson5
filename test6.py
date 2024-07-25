s = input("Ведите слово из маленьких латинских букв:" )
eg = s.count('e')
ag = s.count('a')
ig = s.count('i')
ug = s.count('u')
og = s.count('o')
vowel = eg+ag+ig+ug+og
print("всего гласных",vowel)
print("всего согласных",len(s)-vowel)
if (eg==0):
	print ("e False")
else:
	print("e =",eg)
if (ag==0):
	print ("a False")
else:
	print("a =",ag)
if (ig==0):
	print ("i False")
else:
	print("i =",ig)
if (ug==0):
	print ("u False")
else:
	print("u =",ug)
if (og==0):
	print ("o False")
else:
	print("o =",og)