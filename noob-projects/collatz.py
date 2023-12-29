"""An implementation of the collatz conjecture"""
import time
from typing import Tuple


class Collatz:
    def collatz_conjecture(self, number: int) -> int:
        """The collatz conjecture is a fascinating unproven mathematical
        conjecture whereby the basis is divide a integer by two if its even
        and mutliply the integer by 3 and add 1, all currently known numbers
        end up in a loop of 4 -> 2 -> 1 -> 4. This function prints the current
        number we are on.
        """
        print(number)
        if number == 1:
            return 1
        elif number % 2 == 0:
            return int(number / 2)
        else:
            return int(number * 3 + 1)

    def validate_input(self, command: str) -> Tuple[bool, int]:
        """This validates the input from the user to be an integer"""
        try:
            command = int(command)
            return True, command
        except ValueError:
            print("Please input a valid integer")
        return False, 0

    def get_user_input(self) -> str:
        """This function gets the user input"""
        print("Input an integer to find the collatz chain or q to quit.")
        command = input("> ")
        return command

    def render_collatz(self, number: int) -> None:
        """This renders the beautiful collatz process."""
        while number != 1:
            number = self.collatz_conjecture(number=number)
            time.sleep(0.03)
        print(number)

    def find_collatz(self) -> None:
        """Function handles the logic to view the conjecture."""
        while True:
            command = self.get_user_input()
            if command.lower() == "q":
                return
            validity, number = self.validate_input(command=command)
            if not validity:
                continue
            self.render_collatz(number=number)


Collatz().find_collatz()
