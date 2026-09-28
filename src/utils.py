def get_float_input(prompt: str) -> float:
    """Validates and collects positive float inputs from CLI."""
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Error: Input must be greater than 0.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid number.")

def get_int_input(prompt: str) -> int:
    """Validates and collects positive integer inputs from CLI."""
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Error: Input must be greater than 0.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid whole number.")
