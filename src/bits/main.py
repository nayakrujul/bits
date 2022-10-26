from string import ascii_lowercase, ascii_uppercase
from bits.List import List

def run(code, stack=()):
    if code.count('0') + code.count('1') != len(code):
        raise SyntaxError(
            'Code does not consist of just 0s and 1s')
    stack = List(stack)
    index = 0
    while index < len(code):
        count = 0
        while code[index] == '1':
            count += 1
            index += 1
        index += 1
        if count == 0:
            binary = code[index:index+5]
            num = int(binary, 2)
            if 1 <= num <= 26:
                char = ascii_lowercase[num - 1]
            else:
                char = {0: '\n', 27: '.', 28: ',', 29: '!', 30: '?', 31: ' '}[num]
            if stack and isinstance(stack[0], str):
                stack[0] += char
            else:
                stack.push(char)
            print('DEBUG|0')
            index += 5
        elif count == 1:
            binary = code[index:index+5]
            num = int(binary, 2)
            if 1 <= num <= 26:
                char = ascii_uppercase[num - 1]
            else:
                char = {0: '\t', 27: '@', 28: '£', 29: '$', 30: '"', 31: "'"}[num]
            if stack and isinstance(stack[0], str):
                stack[0] += char
            else:
                stack.push(char)
            print('DEBUG|1')
            index += 5
        elif count == 2:
            binary = code[index:index+4]
            num = int(binary, 2)
            if num <= 9:
                if stack and isinstance(stack[0], int):
                    stack[0] = eval(str(stack[0]) + str(num))
                else:
                    stack.push(num)
            elif num == 10:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 + num2)
            elif num == 11:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 - num2)
            elif num == 12:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 * num2)
            elif num == 13:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 / num2)
            elif num == 14:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 % num2)
            elif num == 15:
                for i, item1 in enumerate(stack):
                    if isinstance(item1, (int, float)):
                        num2 = item1
                        break
                for item2 in stack[i+1:]:
                    if isinstance(item2, (int, float)):
                        num1 = item2
                        break
                stack.push(num1 ** num2)
            print('DEBUG|2')
            index += 4
        elif count == 3:
            binary = code[index:index+4]
            num = int(binary, 2) 
            if num == 0:
                print(stack[0])
            elif num == 1:
                stack.push(input())
            elif num == 2:
                for item in stack:
                    if isinstance(item, str):
                        for i in item:
                            stack = run(code[index+4:code.index('11100011')], [i] + stack)
                        break
                index = code.index('11100011') + 4
            elif num == 4:
                while True:
                    stack = run(code[index+4:], stack)
            elif num == 5:
                return stack
            elif num == 6:
                if stack[0]:
                    stack = run(code[index+4:code.index('11100111')], stack)
                    index = code.index('11101000') + 4
                else:
                    stack = run(code[code.index('11100111')+8:code.index('11101000')])
                    index = code.index('11101000') + 4
            elif num == 9:
                stack.push(stack[0] > stack[1])
            elif num == 10:
                stack.push(stack[0] >= stack[1])
            elif num == 11:
                stack.push(stack[0] < stack[1])
            elif num == 12:
                stack.push(stack[0] <= stack[1])
            elif num == 13:
                stack.push(stack[0] == stack[1])
            elif num == 14:
                stack.push(stack[0] != stack[1])
            elif num == 15:
                if stack and isinstance(stack[0], str):
                    stack[0] += '='
                else:
                    stack.push('=')
            print('DEBUG|3')
            index += 4
        elif count == 4:
            binary = code[index:index+2]
            num = int(binary, 2) 
            if num == 0:
                stack.push(stack[0] and stack[1])
            elif num == 1:
                stack.push(stack[0] or stack[1])
            elif num == 2:
                stack.push(bool(stack[0]) ^ bool(stack[1]))
            elif num == 3:
                stack.push(not stack[0])
            print('DEBUG|4')
            index += 2
        elif count == 5:
            binary = code[index:index+4]
            num = int(binary, 2) 
            lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '>', '<']
            char = lst[num]
            if stack and isinstance(stack[0], str):
                stack[0] += char
            else:
                stack.push(char)
            print('DEBUG|5')
            index += 4
        elif count == 6:
            binary = code[index:index+7]
            num = int(binary, 2) 
            char = chr(num)
            if stack and isinstance(stack[0], str):
                stack[0] += char
            else:
                stack.push(char)
            print('DEBUG|6')
            index += 7
        elif count == 7:
            binary = code[index]
            num = int(binary, 2)
            if num == 0:
                stack.push(chr(stack[0]))
            else:
                stack.push(ord(stack[0]))
            print('DEBUG|7')
            index += 1
    return stack

def from_cmdline():
    code = input().replace(' ', '')
    out = run(code)[0]
    print('Output:', out)
    print('Length of code:', len(code), 'bits =', round(len(code) / 8, 3), 'bytes')
