HISTORY_FILE="calc_history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("\nNo calculation history found.")
            else:
                print("\n--- Calculation History ---")
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("\nNo calculation history found.")



def clear_history():
    open(HISTORY_FILE, 'w').close()
    print("Calculation history cleared.")


def save_calculation(eq, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{eq} = {result}\n")


def calculate():
    try:
        val1 = float(input("Enter first number: "))
        op = input("Enter operator (+ - * /): ").strip()
        val2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered. Please try again.")
        return

    if op == "+":
        result = val1 + val2
    elif op == "-":
        result = val1 - val2
    elif op == "*":
        result = val1 * val2
    elif op == "/":
        if val2 == 0:
            print("Invalid calculation — cannot divide by 0.")
            return
        result = val1 / val2
    else:
        print("Use only +, -, *, / operators.")
        return

    if result.is_integer():
        result = int(result)

    expression = f"{val1} {op} {val2}"
    print("\nResult:", result)
    save_calculation(expression, str(result))

    # 💬 New message after calculation
    print("\n✅ Calculation complete! You can now start a new calculation or enter a command (history, clear, exit).")
def main():
    print("Welcome to the Python Calculator!")
    print("You can type: c | h | clr | q")

    while True:
        user_input = input("\nEnter command or type 'calc' to perform a calculation: ").strip().lower()

        if user_input == "q":
            print("You are exiting from the calculator. Goodbye!")
            break
        elif user_input == "h":
            show_history()
        elif user_input == "clr":
            clear_history()
        elif user_input == "c":
            calculate()
        elif user_input == "":
            print("Please type a command or 'calc' to start a new calculation.")
        else:
            print("Unknown command. Try: c | h | clr | q")


if __name__ == "__main__":
    main()