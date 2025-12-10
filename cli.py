import time
from rich import print as rprint
from core import start_game, difficulty_level, generate_number, get_user_guess

def play_once():
    start_game()
    remaining_attempts = difficulty_level()
    attempts = 0
    # Further game logic can be added here using the attempts variable
    
    start_time = time.time()
    num = generate_number()
    while remaining_attempts > 0:
        attempts += 1
        guess = get_user_guess()
        if guess == num:
            elapsed_time = time.time() - start_time
            rprint(f"[bold green]Congratulations! You've guessed the correct number in {attempts} attempts![/bold green]")
            rprint(f"[bold green]Time taken: {elapsed_time:.2f} seconds[/bold green]")
            break
        elif guess < num:
            remaining_attempts -= 1
            rprint("[bold red]Too low! Try again.[/bold red]\n")
        elif guess > num:
            remaining_attempts -= 1
            rprint("[bold red]Too high! Try again.[/bold red]\n")
    
    elapsed_time = time.time() - start_time
    rprint(f"[bold red]Sorry, you've run out of attempts. The correct number was {num}.[/bold red]")
    rprint(f"[bold red]Time taken: {elapsed_time:.2f} seconds[/bold red]")

def main():
    while True:
        play_once()
        retry = input("\nWanna try again? (y/n): ").strip().lower()
        if retry not in ("y", "yes"):
            rprint("\n[bold cyan]Thanks for playing! Bye 👋[/bold cyan]")
            break

if __name__ == "__main__":
    main()
