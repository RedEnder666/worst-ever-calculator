with open('file.py', 'w') as file:
    n = 100000
    file.write('a = -1\nb = -1\nc = -1\n')
    for i in range(n):
        file.write('\nif a == -1:\n    ')
        file.write(f'if input("Is first number is {i}? (Yes/No)") == "Yes":\n        a={i}\n    ')
    for i in range(n):
        file.write('\nif b == -1:\n    ')
        file.write(f'if input("Is second number is {i}? (Yes/No)") == "Yes":\n        b={i}\n    ')
    for i in ['+', '-', '*', '/']:
        file.write('\nif c == -1:\n        ')
        file.write(f'if input("Do you want to {i} numbers?? (Yes/No)") == "Yes":\n            c="{i}"\n    ')

    file.write("\nif c == '+':\n    ")
    file.write('print(a+b)\n')

    file.write("if c == '-':\n    ")
    file.write('print(a-b)\n')

    file.write("if c == '*':\n    ")
    file.write('print(a*b)\n')

    file.write("if c == '/':\n    ")
    file.write('print(a/b)\n')
    file.write('\n\ninput()')
    

        

