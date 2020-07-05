class ParenthesisValidator:
    def __init__(self, parenthesis_string):
        self.parenthesis_string = parenthesis_string

    def is_valid_parenthesis(self):
        parentheses = {'(': ')', '{': '}', '[': ']'}
        parenthesis_array = []

        for parenthesis in self.parenthesis_string:
            if parenthesis in parentheses:
                parenthesis_array.append(parenthesis)
            elif len(parenthesis_array) == 0 or parentheses[parenthesis_array.pop()] != parenthesis:
                return False

        return True


parenthesis_1 = ParenthesisValidator('()')
print(parenthesis_1.is_valid_parenthesis())

parenthesis_2 = ParenthesisValidator('(})]{]')
print(parenthesis_2.is_valid_parenthesis())

parenthesis_3 = ParenthesisValidator('(){}[]')
print(parenthesis_3.is_valid_parenthesis())
