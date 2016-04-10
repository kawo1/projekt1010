def dodawanie(a, b):
    return(a+b)

try:
l1 = int(input())
l2 = int(input())
print(dodawanie(l1, l2))
except:
    print("Program zakończył się nieoczekiwanym błędem")\
    print("Możesz go zgłosic pod adresem autor.pl")