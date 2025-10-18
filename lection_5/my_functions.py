from rich import print
# task 1
# создать файл my_functions.py с функциями greet и change_name
# change_name - принимает строку, а возвращает измененное имя, где каждая вторая буква - большая
# greet - принимает строку, ничего не возвращает, а просто принтит "Hello имя" с помощью украшений из rich print
def change_name(f: str):
    g = 0
    gg = ""
    for i in f:
        if g % 2 == 0:
            gg += i.title()
        else:
            gg += i
        g += 1
    return gg

print(change_name("hkljfgilofgjhl"))

def greet(f: str):
    return f"[blue]Hello[/blue] {f}"
    
print(greet("GAY"))