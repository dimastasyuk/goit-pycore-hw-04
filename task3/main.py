
import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)


def show_directory(path, indent=0):
    try:
        for item in path.iterdir():
            if item.name == ".venv" or item.name == ".git":
                continue

            if item.is_dir():
                print("    " * indent + Fore.BLUE + item.name + "/")
                show_directory(item, indent + 1)
            else:
                print("    " * indent + Fore.GREEN + item.name)

    except OSError as error:
        print(Fore.RED + f"Помилка: {error}")


if len(sys.argv) < 2:
    print("Вкажіть шлях до директорії!")
else:
    path = Path(sys.argv[1])

    if not path.exists():
        print("Директорія не існує!")
    elif not path.is_dir():
        print("Це не директорія!")
    else:
        print(Fore.BLUE + path.name + "/")
        show_directory(path, 1)
