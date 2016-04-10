def dodawanie(a, b):
    return(a+b)

def get_info():
    print("Program kalkulator. Autor: Kasia")

get_info()

try:
    l1 = int(input())
    l2 = int(input())
    print(dodawanie(l1, l2))
except:
    print("Program zakoĹ„czyĹ‚ siÄ™ nieoczekiwanym bĹ‚Ä™dem")
    print("MoĹĽesz go zgĹ‚osic pod adresem autor.pl")
