# This is a simple calculator which take string and calculate this expression
# Author: Vladyslav Dyshkant

import re

class Calculator(object):
    def calc(self, a, b, operator):
        if operator == '*':
            return int(a) * int(b)
        if operator == '/':
            return int(a) / int(b)
        if operator == '+':
            return int(a) + int(b)
        if operator == '-':
            return int(a) - int(b)

    def calcExpression(self, array):
        while '*' in array or '/' in array:
            for i in range(len(array)):
                if array[i] == '*' or array[i] == '/':
                    temp = self.calc(array[i-1], array[i+1], array[i])
                    array = array[:i-1] + array[i+2:]
                    array.insert(i-1, temp)
                    break
        while '+' in array or '-' in array:
            for i in range(len(array)):
                if array[i] == '+' or array[i] == '-':
                    temp = self.calc(array[i-1], array[i+1], array[i])
                    array = array[:i-1] + array[i+2:]
                    array.insert(i-1, temp)
                    break
        return array[0]

    def evaluate(self, string):
        global temp
        array = [i for i in re.split('\s*', string) if i]
        if '(' in array or ')' in array:
            if array.count('(') ==  array.count(')'):
                isBracket = True
                while isBracket:
                    count = 0
                    index = 1
                    tempArray = []
                    for i in range(len(array)):
                        if array[i] == '(':
                            count += 1
                        if count == array.count('('):
                            while array[i + index] != ')':
                                tempArray.append(array[i + index])
                                index += 1
                            if len(tempArray) == 3:
                                temp = self.calc(tempArray[0], tempArray[2], tempArray[1])
                            else:
                                temp = self.calcExpression(tempArray)
                            array = array[:i] + array[i + index + 1:]
                            array.insert(i, temp)
                            break
                    if array.count('(') == 0:
                        isBracket = False
        result = self.calcExpression(array)
        return result

if __name__ == "__main__":
    calc = Calculator()
    print(calc.evaluate("2*(2*(2*(2*1)))"))