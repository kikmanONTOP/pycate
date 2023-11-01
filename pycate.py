import base64
import colorama
from colorama import Fore


ascii = '''
 ██▓███ ▓██   ██▓ ▄████▄   ▄▄▄     ▄▄▄█████▓▓█████ 
▓██░  ██▒▒██  ██▒▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▓█   ▀ 
▓██░ ██▓▒ ▒██ ██░▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒███   
▒██▄█▓▒ ▒ ░ ▐██▓░▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒▓█  ▄ 
▒██▒ ░  ░ ░ ██▒▓░▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░▒████▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░░ ▒░ ░
░▒ ░     ▓██ ░▒░   ░  ▒     ▒   ▒▒ ░   ░     ░ ░  ░
░░       ▒ ▒ ░░  ░          ░   ▒    ░         ░   
         ░ ░     ░ ░            ░  ░           ░  ░
         ░ ░     ░                                 '''

print(Fore.LIGHTCYAN_EX + ascii)
vstupni_soubor = input(Fore.LIGHTMAGENTA_EX + "name of file: ")
vystupni_soubor = input("name of new obfuscated file: ")

with open(vstupni_soubor, 'rb') as vstupni_file:
    obsah = vstupni_file.read()


with open(vystupni_soubor, 'w') as vystupni_file:
    vystupni_file.write(f"import base64\n\n")
    vystupni_file.write(f"base64_obsah = {base64.b64encode(obsah)}\n")
    vystupni_file.write(f"exec(base64.b64decode(base64_obsah))\n")

print(f"file'{vstupni_soubor}' has been obfuscated to '{vystupni_soubor}'.")
