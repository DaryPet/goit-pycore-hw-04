
import sys
from colorama import init, Fore, Style
from pathlib import Path

init(autoreset=True)


def print_directory_structure(directory, prefix=""):
    try:
        directory = Path(directory)
        if not directory.exists() or not directory.is_dir():
            print(Fore.RED + f"Помилка: Шлях '{directory}' не існує або це не директорія.")
            return

        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(Fore.BLUE + prefix + "📂 " + item.name)
                print_directory_structure(item, prefix + "┃  ")
            else:
                print(Fore.GREEN + prefix + "📜 " + item.name)
    except Exception as e:
        print(Fore.RED + f"Помилка: {e}")

if __name__ == "__main__":
     pictures_directory = Path(__file__).resolve().parent / "pictures"
     print_directory_structure(pictures_directory)
   
