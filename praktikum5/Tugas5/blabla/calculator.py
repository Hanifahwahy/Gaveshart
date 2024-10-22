import math
from docopt import docopt

class MyCalculator:
    def get_options(self):
        self.args = docopt(__doc__)

        # Loop via commands getting what is needed
        if self.args["add"]:
            self.addition()
        elif self.args["mult"]:
            self.multiply()
        elif self.args["current"]:
            self.calculate_current()
        elif self.args["square"]:
            self.get_square()
        elif self.args["root"]:
            self.get_root()

    def addition(self):
        """Get the sum of all numbers passed."""
        summation = sum([int(number) for number in self.args["<number>"]])
        print(f"Sum: {summation}")

    def multiply(self):
        """Get the product of the list of numbers."""
        product = math.prod([int(number) for number in self.args["<number>"]])
        print(f"Product: {product}")

    def calculate_current(self):
        """Calculate current based on voltage and resistance."""
        voltage = float(self.args["<voltage>"])
        resistance = float(self.args["<resistance>"])

        if resistance == 0:
            print("Error: Resistance (R) cannot be zero.")
        else:
            current = voltage / resistance  # I = V / R
            print(f"Current (I) is {current} ampere")

    def get_square(self):
        """Calculate the square of a number."""
        number = float(self.args["<number>"])
        square = number ** 2
        if self.args["--verbose"]:
            print(f"The square of {number} is {square}.")
        else:
            print(square)

    def get_root(self):
        """Calculate the square root of a number."""
        number = float(self.args["<number>"])
        root = math.sqrt(number)
        print(f"The square root of {number} is {root}.")

if __name__ == "__main__":
    arguments = docopt(__doc__, version="My Advanced Calculator 1.0")
    calculator = MyCalculator()
    calculator.get_options()
