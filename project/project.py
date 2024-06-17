#Project title: Slot machine Game
#Name: Callum McEvoy
#Githud and Edx username: cmcevoy0405
#City, Country: Belfast, Northern Ireland
#Date: 17th of June, 2024


import random
COLS = 3
ROWS = 3
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

def main():
    balance = deposit()
    while True:
        if balance < MIN_BET:
            print("Too low a balance to continue")
            break
        number_of_lines = bet_number()
        print(f"You are betting on {number_of_lines} lines")
        bet = get_bet(number_of_lines)
        for line, amount in bet.items():
            print(f"On line {line} you have bet £{amount}")
        total_bets = sum(bet.values())
        if total_bets > balance:
            print("Not enough funds")
        else:
            remaining_balance = (balance - total_bets)
            print(f"Remaining balance: £{remaining_balance}")
        slots = get_slot_spin(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings = match_numbers(slots, line, bet, symbol_values)
        print(f"You won £{winnings}")
        if winnings == 0:
            balance = remaining_balance
            print(f"Your new balance is now £{balance}")
        else:
            balance = winnings + balance
            print(f"Your new balance is now £{balance}")

        play_again = input("Press y to play again or any other key to quit?: ").lower()
        if play_again != "y":
            break
    print(f"You finished with £{balance}")



def deposit():
    balance = 0
    while True:
        try:
            amount = input("Enter money to play: ")
            if amount.isdigit() and int(amount) > 0:
                balance += int(amount)
                print(f"Balance: £{balance}")
            else:
                print("Please input coins only")
        except EOFError:
            print(f"\n Your Total balance is: £{balance}")
            break
    return balance

def bet_number():
    while True:
        lines = input(f"How many lines would you like to bet on (1-3)? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                return lines
            else:
                print("Must be a number between 1 and 3")
        else:
            print("Must be a number")

def get_bet(number_of_lines):
    bets = {}
    for i in range(1, number_of_lines + 1):
        while True:
            amount = input(f"How much do you want to bet on line {i}? ")
            if amount.isdigit():
                amount = int(amount)
                if  MIN_BET <= amount <= MAX_BET:
                    bets[i] = amount
                    break
                else:
                    print("Must be between minimum and maximum bets")
            else:
                print("Ensure bet is a number")
    return bets

symbol_count = {
    "🪙": 4,
    "🥈": 5,
    "💀": 7,
    "💩": 10
}

symbol_values = {
    "🪙": 8,
    "🥈": 6,
    "💀": 4,
    "💩": 2
}

def get_slot_spin(rows, cols, symbol_count):
    all_symbols = []
    for symbol, symbol_count in symbol_count.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end= "")
        print()

def match_numbers(columns, lines, bet, value):
    winnings = 0
    for line in range(1, lines + 1):
        symbol = columns[0][line -1]
        for column in columns:
            symbol_check = column[line -1]
            if symbol != symbol_check:
                break
        else:
            winnings += value[symbol] * bet[line]

    return winnings




if __name__ == "__main__":
    main()
