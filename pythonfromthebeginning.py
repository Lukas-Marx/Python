# Lukas Marx 03.05.1994
# Lukas.Marx@FAU.de
print ('just like this') #String
a = 1 + 2 * 3 #Berechnung
print(a)
print ("Can't use single quotation marks here!") #Integer

print(12) #Integer
print('12') #String

b = 99 > 100
print(b)
c = 4+3+2+1 ==10 #wahr falsch abfrage ein ist gleich waere die belegung eines parameters
print(c)
print('a==b wahr wenn gleich'
      'a<b wahr wenn a kleiner b'
      'a<=b wahr wenn a kleiner gleich b'
      'a>b wahr wenn a groesser b'
      'a>=b wahr wenn a groesser gleich b'
      'a!=b wahr wenn a nicht gleich b')

d = 1 ==1 or 10 > 9
e = 1 ==1 and 9 > 10

print (d)
print (e)
print ('and wird vor or durchgefuehrt also a and b or c ist wie (a and) or c')

print ('Vergleichs operatoren haben eine hoehere Prioritaet als logische operatoren')
print (type(a))
print (type(b))
print (type('hilfe'))
print ('str = string, bool = booleans und int = integers')

print('antworten auf chapter 1 Fragen')
print ('17, 11, False, True, False, %, 11, True, 3, onetwo, 1two, 111, 111, 111')

f = 'bacon'<'egg'

x = 200
z = x*x*x

x = 5 + 5

z = x*x*x
print ('x ist eine Variable')
print ('um Woerter zu trennen wird ein Unterstricht verwendet')

def cube(x): return x*x*x

y = cube (35)

print (y)

answer = cube (7000)

print (answer)

print ('funktion machen geht per def, gefolgt vom namen und das argument in Klammern und abschliessend ein doppelpunkt '
       'und dann die formel')

def print_twice(x):
      print (x)
      print (x)
print_twice('lol')

def neg(x):
      if x < 0:
            return True
      else:
            return False
print (neg(1))
print (neg(-1))
#Seite 18
