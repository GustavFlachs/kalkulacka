x = input ("Zadejte hodnotu x: ")
y = input ("Zadejte hodnotu y: ")

x = int(x)
y = int(y)
print ("Pro sčíání zadejte +")
print ("Pro odčítání zadejte -")
print ("Pro násobení zadejte *")
print ("Pro dělení zadejte /")
print ("Pro mocnění zadejte **")
print ("Pro odmocnění zadejte /*")

znaménko = input ("Zvolte znaménko")

if znaménko == "+":
    výsledek = x + y
    výsledek = str(výsledek)
    print (x+y)
elif znaménko == "-":
    výsledek = x - y
    výsledek = str(výsledek)
    print (x-y)
elif znaménko == "*":
    výsledek = x * y
    výsledek = str(výsledek)
    print (x*y)
elif znaménko == "/":
    if y != 0:
        výsledek = x / y
        výsledek = str(výsledek)
        print (x/y)
    else:
        print ("co dělíš nulou co chceš bombu?")
elif znaménko == "**":
    výsledek = x ** y
    výsledek = str(výsledek)
    print (x**y)
elif znaménko == "/*":
    if y != 0:
        výsledek = x **(1/y)
        výsledek = str(výsledek)
        print (x **(1/y)) 
    else:
        print ("to se ale nesmí dělit nulou nevíš?")