import os
import sys
from colorama import init, Fore, Style

init(autoreset=True)

def list_directory(path, level=0):
    try:
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                print(f"{' ' * level * 2}{Fore.BLUE}{item}")
                list_directory(item_path, level + 1)
            else:
                print(f"{' ' * level * 2}{Fore.GREEN}{item}")
    except FileNotFoundError:
        print(f"Cannot find directory by path - {path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Use your derrictory: python hw04.py /шлях/до/вашої/директорії")
    else:
        directory_path = sys.argv[1]
        list_directory(directory_path)