import math
import os

print('Zadanie 1')
def fabs(x):
    if x<0:
        return -x
    else:
        return x
x=int(input('Wprowadź liczbę całkowitą x '))
print('Wartość bezwględna z liczby x wynosi',fabs(x))
print('----')
print('Zadanie 2')
def check(x,y):
    if x==y:
        return 'Liczby są równe'
    elif x>y:
        return 'Pierwsza liczba jest większa'
    else:
        return 'Druga liczba jest większa'
x=int(input('Podaj x\n'))
y=int(input('Podaj y\n'))
print(check(x,y))
print('----')
print('Zadanie 3')
def check(x,y,z):
    if x==y==z:
        return 'Liczby są równe'
    elif x>y>z:
        return 'Liczba x jest największa'
    elif x>z>y:
        return 'Liczba x jest największa'
    elif y>x>z:
        return 'Liczba y jest największa'
    elif y>z>x:
        return 'Liczba y jest największa'
    elif z>x>y:
        return 'Liczba z jest największa'
    elif z>y>x:
        return 'Liczba z jest największa'
x=int(input('Podaj x '))
y=int(input('Podaj y '))
z=int(input('Podaj z '))
print(check(x,y,z))
print('----')
print('Zadanie 4')
def fabs(x):
    if x<0:
        return -x
    else:
        return x
def fabs(y):
    if y<0:
        return -y
    else:
        return y
def check(x,y):
    if x==y:
        return 'Liczby x i y są równe'
    if x>y:
        return 'Liczba x jest większa'
    else:
        return 'Liczba y jest większa'
x=int(input('Podaj x '))
y=int(input('Podaj y '))
print(check(x,y))
print('----')
print('Zadanie 5')
print('1) Obliczanie pola trójkąta za pomocą długości podstawy oraz długości wysokości\n2) Obliczanie pola trójkąta za pomocą długości wszystkich boków')
opcja=int(input('Wybierz opcje wpisując 1 lub 2 '))
if opcja==1:
    a=float(input('Podaj długość podstawy '))
    h=float(input('Podaj długość wysokości '))
    print('Pole trójkąta wynosi',a*h/2)
if opcja==2:
    a=float(input('Podaj długośc pierwszego boku '))
    b=float(input('Podaj długośc pierwszego boku '))
    c=float(input('Podaj długośc pierwszego boku '))
    print('Niemożliwe jest obliczenie pola trójkąta na podstawie długości boków')
if opcja>2:
    print('Nie wybrałeś poprawnej opcji')
if opcja<1:
    print('Nie wybrałeś poprawnej opcji')
print('----')
print('Zadanie 6')
print('Niemożliwe jest wykonanie tego zadania')
print('----')
print('Zadanie 7')
print('Wzór na równanie kwadratowe z jedną niewiadomą ax2+bx+c=0')
a=float(input('Podaj a '))
b=float(input('Podaj b '))
c=float(input('Podaj c '))
delta=(b*b)-(4*a*c)
print(delta)
if delta>0:
    pdelta=pow(delta,1/2.0)
    print(pdelta)
    x1=(-b+pdelta)/2*a
    x2=(-b-pdelta)/2*a
    print('x1=', x1 ,'\nx2=',x2)
if delta==0:
    x=-b/(2*a)
    print('x=', x)
if delta<0:
    print('brak miejsc zerowych')
print('----')
print('Zadanie 8')
print('1) Kwadrat\n2) Prostokąt\n3) Trójkąt')
opcja=int(input('Wybierz opcje 1,2, lub 3 '))
if opcja==1:
    a=float(input('Podaj a '))
    print('Pole kwadratu wynosi ',a*a)
if opcja==2:
    a=float(input('Podaj a '))
    b=float(input('Podaj b '))
    print('Pole prostokąta wynosi ',a*b)
if opcja==3:
    a=float(input('Podaj a'))
    h=float(input('Podaj h '))
    print('Pole trójkąta wynosi ',a*h/2)
if opcja>3:
    print('Wybierz właściwą opcję')
if opcja<1:
    print('Wybierz właściwą opcję')
print('----')
print('Zadanie 9')
print('Kalkulator obłsuguje funkcje +,-,*,/,%,√')
x=float(input('Podaj pierwszą liczbę '))
y=float(input('Podaj drugą liczbę '))
z=input('Podaj działanie ')
if z=='+':
    print(x+y)
if z=='-':
    print(x-y)
if z=='*':
    print(x*y)
if z=='**':
    print(x**y)
if z=='/':
    print(x/y)
if z=='%':
    print(x%y)
if z=='√':
    print(x*(1.0/y))
print('----')
print('Zadanie 10')
def fabs(x):
    if x<0:
        return -x
    else:
        return x
x=int(input('Wprowadź liczbę całkowitą x '))
print('Wartość bezwględna z liczby x wynosi',fabs(x))
