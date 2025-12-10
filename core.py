from rich import print as rprint
import random

def start_game():
    rprint("[bold green]Game has started successfully![/bold green]")
    rprint("[bold blue]Welcome to the Number Guessing Game![/bold blue]")
    rprint("[bold yellow]Try to guess the number I'm thinking of between 1 and 100.[/bold yellow]")

def difficulty_level():
    rprint("[bold magenta]Choose your difficulty level:[/bold magenta]")
    rprint("1. Easy (10 Chances)")
    rprint("2. Medium (5 Chances)")
    rprint("3. Hard (3 Chances)")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        attempt = 10
        rprint("\n[bold green]You have selected Easy level with 10 attempts.[/bold green]")
        rprint("[bold green]Let's start the game![/bold green]\n")
    elif choice == 2:
        attempt = 5
        rprint("\n[bold green]You have selected Medium level with 5 attempts.[/bold green]")
        rprint("[bold green]Let's start the game![/bold green]\n")
    elif choice == 3:
        attempt = 3 
        rprint("\n[bold green]You have selected Hard level with 3 attempts.[/bold green]")
        rprint("[bold green]Let's start the game![/bold green]\n")
    else:
        rprint("\n[bold red]Invalid choice! Please select a valid difficulty level.[/bold red]")
        return difficulty_level()
    
    return attempt

def generate_number():
    return random.randint(1, 100)

def get_user_guess():
        while True:
            try:
                guess = int(input("Enter your guess : "))
                return guess
            except ValueError:
                rprint("[bold red]Enter a valid number![/bold red]")



