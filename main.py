from rich.panel import Panel 
from rich.console import Console 
from rich.align import Align 
from rich.text import Text 
from colorama import init, Fore, Style

import os, subprocess, sys , json

console = Console()
init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN 
YELLOW = Fore.YELLOW 
BLUE = Fore.BLUE 
RESET = Style.RESET_ALL 

with open("config/info.json", "r") as file:
    info = json.load(file)

print(f"[{BLUE}#{RESET}] - Boring developer stuff")

print(info["pretty_version"])
print(info["boring_version"])

print(f"[{BLUE}#{RESET}] - Other")

banner = """
███████╗███████╗██████╗ ██╗  ██╗ ██████╗ 
██╔════╝╚══███╔╝██╔══██╗██║ ██╔╝██╔════╝ 
█████╗    ███╔╝ ██████╔╝█████╔╝ ██║  ███╗
██╔══╝   ███╔╝  ██╔═══╝ ██╔═██╗ ██║   ██║
███████╗███████╗██║     ██║  ██╗╚██████╔╝
╚══════╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ 

           type HELP for more
"""

cmd = f"[{BLUE}>{RESET}] {BLUE}ez{RESET}pkg -$ "

help = """
[help]  - Lists available commands,
[exit]  - Exits the program,
[clear] - Clears the terminal
"""

def clear():
    os.system("clear")

def refresh():
    os.system("clear")
    console.print(
        Align.center(banner)
    )


def main():
    refresh()

    while True:
        userinput = input(cmd).lower()

        if userinput == "":
            continue

        elif userinput == "help":
            console.print(
                Align.center(
                    Panel.fit(Text.from_ansi(help), title="Help", border_style="bold blue")
                )
            )
        
        elif userinput == "exit":
            clear()
            sys.exit()

        elif userinput == "clear":
            refresh()
        
        elif userinput == "c":
            refresh()

        else:
            print(f"[{RED}-{RESET}] - Unkown command: {userinput}")

if __name__ == "__main__":
    main()



