import re


class ValidCarNumber:

    def __init__(self, number):
        self.number = number

    def is_valid(self):
        num = re.search(r"0([0-9]{1})KG([0-9]{3})([A-Z]{3})", self.number)
        if num and self.number == self.number[num.start():num.end()]:
            print('Number is valid')
        else:
            print('Number is not valid')


nums = ValidCarNumber('01KG555ASD')
nums.is_valid()
