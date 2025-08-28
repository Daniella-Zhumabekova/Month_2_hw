"""
Библиотека: colorama
"""
from colorama import Fore, Back, Style, init

init(autoreset=True)

def demo_colors():
    print(Fore.RED + "красный текст")
    print(Fore.GREEN + "зелёный текст")
    print(Fore.BLUE + "синий текст")
    print(Back.YELLOW + Fore.BLACK + "Чёрный текст на жёлтом фоне")
    print(Style.BRIGHT + "Яркий стиль текста")
    print("Обычный текст (после autoreset)")


demo_colors()