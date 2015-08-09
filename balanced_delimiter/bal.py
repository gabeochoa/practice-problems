#!/usr/bin/python


def bal(string):
    popu = []

    try:
        for char in string:
            if char == '(' or char == '[' or char == '{':
                popu.append(char)
                continue
            if char == ')':
                if popu.pop() != '(':
                    return False
            if char == ']':
                if popu.pop() != '[':
                    return False
            if char == '}':
                if popu.pop() != '{':
                    return False
    except IndexError:
        return False
    return True if len(popu) == 0 else False


def main():
    assert(bal("([{}])")) == True
    assert(bal("([)]")) == False
    assert(bal("([]")) == False
    assert(bal("[])")) == False
    assert(bal("([})")) == False


main()