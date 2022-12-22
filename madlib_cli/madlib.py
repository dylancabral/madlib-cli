import re

def read_template(file):
    try:
        with open(file,'r') as f:
            return f.read()

    except FileNotFoundError as Error_in_file:
        raise Error_in_file

def parse_template(string):
    pieces = tuple(re.findall(r"{(.*?)}", string))
    print(pieces)
    for x in pieces:
        string = string.replace(x, "")
    return string,pieces


def merge(stripped, inputs):
    return stripped.format(*inputs)

message = """
*** welcome to my program, This is a madlibs function    ***
*** your input will change the outcome of the madlib     ***
*** I Hope you enjoy it, its always Fun if you let it be ***
"""

def main():
    print(message)
    file_path = input(" Enter File Path or hit 'Enter' for the default > ")
    if file_path == "":
        file_path = "../assets/madlib.txt"
    try:
        script = read_template(file_path)
        empty_string, parts = parse_template(script)
        filled_list = []
        for i in parts:
            user_input = input(f"  Enter {i} > ")
            filled_list.append(user_input)
        result = merge(empty_string, filled_list)
        print(f"\nHere is your Madlib:\n\n" + result)
        with open('assets/result.txt', 'w') as writer:
            writer.write(result)
    except:
        print('An error occurred')


if __name__ == '__main__':
    main()