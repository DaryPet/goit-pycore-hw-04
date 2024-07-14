
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
    if len(sys.argv) != 2:
        print(Fore.RED + "Використання: cd /Users/mac/Desktop/IT_Developer/FULL\ STACK\ DEV/GitHub/goit-pycore-hw-04/task-3")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)
