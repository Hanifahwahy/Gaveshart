"""
My Advanced Calculator v1.1

Usage:
  rumus2.py add (<number>...)
  rumus2.py mult (<number>...)
  rumus2.py current <voltage> <resistance>
  rumus2.py square [--verbose] <number>
  rumus2.py root <number>
  rumus2.py force <q1> <q2> <distance>
  rumus2.py (-h | --help)
  rumus2.py --version

Examples:
  rumus2.py add 9 4 67 101
  rumus2.py mult 88 43 20458 1 134 
  rumus2.py current 10 2
  rumus2.py square --verbose 9 
  rumus2.py root 16
  rumus2.py force 2.0e-6 3.0e-6 0.5

Options:
  -h --help        Show this screen.
  -v --version     Show version.
  --verbose        Show details verbosely.
"""

import math
from docopt import docopt

# Konstanta Coulomb dalam N·m²/C²
COULOMB_CONSTANT = 8.99 * (10 ** 9)

class MyCalculator:
    def get_options(self):
        self.args = docopt(__doc__)  # Make sure __doc__ is not None

        # Handle the commands based on the arguments
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
        elif self.args["force"]:
            self.calculate_force()

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

    def calculate_force(self):
        """Calculate the Coulomb force between two charges."""
        q1 = float(self.args["<q1>"])
        q2 = float(self.args["<q2>"])
        distance = float(self.args["<distance>"])

        if distance == 0:
            print("Error: Distance (r) cannot be zero.")
        else:
            force = COULOMB_CONSTANT * abs(q1 * q2) / (distance ** 2)
            print(f"The Coulomb force (F) is {force} Newtons")

if __name__ == "__main__":
    calculator = MyCalculator()
    calculator.get_options()
