import nbformat as nbf
import os

def create_notebook(filename, cells):
    nb = nbf.v4.new_notebook()
    nb['cells'] = [nbf.v4.new_markdown_cell(c[1]) if c[0] == 'md' else nbf.v4.new_code_cell(c[1]) for c in cells]

    # Set kernel metadata for Pyodide
    nb['metadata'] = {
        "kernelspec": {
            "display_name": "Python (Pyodide)",
            "language": "python",
            "name": "python"
        }
    }

    with open(filename, 'w') as f:
        nbf.write(nb, f)

notebooks_data = {
    '01_Print_Statement.ipynb': [
        ('md', '# 1. PRINT STATEMENT\n\nWelcome! The `print()` function is used to display information.\n\n**Note on Safety:** This environment is sandboxed in your browser. Dangerous commands like deleting files on your computer are blocked for your safety.'),
        ('md', '### Example:'),
        ('code', 'print("You are welcome to PYTHON PROGRAMMING class.")'),
        ('md', '### Practice 1:\nTry printing your own name below!'),
        ('code', '# Write your code here\n'),
        ('md', '### Practice 2:\nPrint a welcome message for your friend.'),
        ('code', '# Write your code here\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\nprint("Hello, friend!")\n```\n</details>')
    ],
    '02_Input_Statement.ipynb': [
        ('md', '# 2. INPUT STATEMENT\n\nThe `input()` function allows you to get information from the user.'),
        ('md', '### Example:'),
        ('code', 'name = input("What is your name: ")\nprint("Hello, " + name)'),
        ('md', '### Practice 1:\nAsk the user "What is your favorite color?" and then print it.'),
        ('code', '# Write your code here\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\ncolor = input("What is your favorite color? ")\nprint(color)\n```\n</details>')
    ],
    '03_Variables_Data_Types.ipynb': [
        ('md', '# 3. VARIABLES & DATA TYPES\n\nVariables store values. Data types include String, Integer, Float, and Boolean.'),
        ('code', 'string = "Bolaji"  # String\ninteger = 12       # Integer\nfloat_num = 12.5   # Float\nboolean = True     # Boolean\n\nprint(string)\nprint(integer)'),
        ('md', '## Example: Area of a Triangle'),
        ('code', 'breadth = 3\nheight = 8\ntriangle_area = 0.5 * breadth * height\nprint("THE AREA OF THE TRIANGLE =", triangle_area)'),
        ('md', '### Practice:\nCreate a variable `age` and assign it your age. Then print it.'),
        ('code', '# Write your code here\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\nage = 15\nprint(age)\n```\n</details>')
    ],
    '04_Control_Structures.ipynb': [
        ('md', '# 4. CONTROL STRUCTURES\n\nDecisions in Python!'),
        ('md', '## IF-ELSE Statement'),
        ('code', 'age = 14\nif age >= 18:\n     print("You are eligible to vote")\nelse:\n     print("You are not eligible to vote")'),
        ('md', '### Practice:\nCheck if a number is positive.'),
        ('code', 'number = 5\n# Write your if-else statement below\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\nif number > 0:\n    print("Positive number")\nelse:\n    print("Not a positive number")\n```\n</details>')
    ],
    '05_Loops.ipynb': [
        ('md', '# 5. LOOPS\n\nRepeat actions with For and While.'),
        ('md', '## FOR Loop'),
        ('code', 'for i in range(1, 6):\n    print(i)'),
        ('md', '## WHILE Loop'),
        ('code', 'number = 0\nwhile number <= 3:\n    print("LOOP")\n    number = number + 1'),
        ('md', '### Practice:\nPrint "Hello" 3 times using a loop.'),
        ('code', '# Write your code here\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\nfor i in range(3):\n    print("Hello")\n```\n</details>')
    ],
    '06_Concatenation_Type_Conversion.ipynb': [
        ('md', '# 6. CONCATENATION & TYPE CONVERSION\n\nJoin strings and convert types!'),
        ('code', 'first = "Taiwo"\nlast = "Alofe"\nprint(first + " " + last)'),
        ('md', '## Type Conversion with `int()`'),
        ('code', 'breadth = int(input("Enter breadth: "))\nheight = int(input("Enter height: "))\nprint("Area:", 0.5 * breadth * height)'),
        ('md', '### Practice:\nAdd two numbers from input.'),
        ('code', '# Write your code here\n'),
        ('md', '<details><summary><b>Click to see Solution</b></summary>\n\n```python\na = int(input("First: "))\nb = int(input("Second: "))\nprint(a + b)\n```\n</details>')
    ]
}

os.makedirs('content', exist_ok=True)
for filename, cells in notebooks_data.items():
    create_notebook(os.path.join('content', filename), cells)

print("Notebooks updated with solutions and safety notes.")
