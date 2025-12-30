import random

# -------------------------------
# 🔥 PYTHON QUIZ APPLICATION 🔥
# -------------------------------

quiz = {
    1: {
        'question': "Which of the following is used to get user input in Python?",
        'options': ("input()", "scanf()", "get()", " read()"),
        'answer': "input()"
    },
    2: {
        'question': "What is the output of: print(10 // 3)?",
        'options': ("3.33", "3", "4", "Error"),
        'answer': "3"
    },
    3: {
        'question': "Which operator is used for exponent in Python?",
        'options': ("^", "**", "exp()", "%"),
        'answer': "**"
    },
    4: {
        'question': "Which function returns the length of a list?",
        'options': ("count()", "size()", "len()", "length()"),
        'answer': "len()"
    },
    5: {
        'question': "What is the output of: print(type([]))?",
        'options': ("<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'set'>"),
        'answer': "<class 'list'>"
    },
    6: {
        'question': "Which of the following is immutable?",
        'options': ("List", "Dictionary", "Tuple", "Set"),
        'answer': "Tuple"
    },
    7: {
        'question': "What is the correct file extension for Python files?",
        'options': (".py", ".python", ".pt", ".exe"),
        'answer': ".py"
    },
    8: {
        'question': "What does the 'break' statement do?",
        'options': ("Skips iteration", "Ends loop", "Ends function", "Restarts loop"),
        'answer': "Ends loop"
    },
    9: {
        'question': "Which of the following creates a dictionary?",
        'options': ("{}", "[]", "()", "None"),
        'answer': "{}"
    },
    10: {
        'question': "What is the output of: print('5' + '3')?",
        'options': ("8", "53", "Error", "35"),
        'answer': "53"
    },
    11: {
        'question': "Which keyword is used to define a function?",
        'options': ("fun", "function", "def", "define"),
        'answer': "def"
    },
    12: {
        'question': "Which function converts a string to integer?",
        'options': ("toInt()", "int()", "str()", "float()"),
        'answer': "int()"
    },
    13: {
        'question': "Which symbol is used for comments in Python?",
        'options': ("//", "#", "/* */", "<!-- -->"),
        'answer': "#"
    },
    14: {
        'question': "What will print(len('Python')) return?",
        'options': ("5", "7", "6", "8"),
        'answer': "6"
    },
    15: {
        'question': "Which of the following is a logical operator?",
        'options': ("and", "&", "%", "!=="),
        'answer': "and"
    },
    16: {
        'question': "Which module is used for generating random numbers?",
        'options': ("math", "os", "random", "numbers"),
        'answer': "random"
    },
    17: {
        'question': "Which loop runs at least once?",
        'options': ("for", "while", "do-while", "None (Python has no do-while)"),
        'answer': "None (Python has no do-while)"
    },
    18: {
        'question': "What is the output of: print(bool('Hello'))?",
        'options': ("False", "True", "None", "Error"),
        'answer': "True"
    },
    19: {
        'question': "Which of these converts list to set?",
        'options': ("set()", "tuple()", "list()", "dict()"),
        'answer': "set()"
    },
    20: {
        'question': "Which keyword is used to handle exceptions?",
        'options': ("catch", "try", "error", "handle"),
        'answer': "try"
    },
    21: {
        'question': "What is the output of print(2 ** 3 ** 1)?",
        'options': ("64", "16", "8", "4"),
        'answer': "8"
    },
    22: {
        'question': "Which of the following creates an empty set?",
        'options': ("{}", "set()", "[]", "()"),
        'answer': "set()"
    },
    23: {
        'question': "Which method adds an item to the end of a list?",
        'options': ("insert()", "append()", "add()", "push()"),
        'answer': "append()"
    },
    24: {
        'question': "Which function returns maximum from list?",
        'options': ("largest()", "max()", "big()", "top()"),
        'answer': "max()"
    },
    25: {
        'question': "Which keyword is used to stop function execution?",
        'options': ("stop", "quit", "return", "end"),
        'answer': "return"
    }
}

print("\n🎯 WELCOME TO THE PYTHON QUIZ 🎯")
print("--------------------------------------------------")
print("You will be given 15 random questions.\nChoose the correct option (a/b/c/d).")
print("--------------------------------------------------\n")

score = 0
opt_index = {'a':0, 'b':1, 'c':2, 'd':3}

selected_questions = random.sample(range(1, 26), 15) 

for q in selected_questions:
    print(f"Q{q}. {quiz[q]['question']}\n")
    
    options_list = quiz[q]['options'] 
    option_letters = ["a", "b", "c", "d"]

    for i, op in enumerate(options_list):
        print(f"  {option_letters[i]}. {op}")
    
    print()

    while True:
        user = input("👉 Enter your answer: ").lower()
        if user in "abcd":
            if options_list[opt_index[user]] == quiz[q]['answer']:
                print("✔ Correct! +1 point\n")
                score += 1
                break
            else:
                print(f"✘ Wrong! Correct answer: {quiz[q]['answer']}\n")
                break
        else:
            print("⚠ Invalid input! Please choose a/b/c/d.\n")

print("--------------------------------------------------")
print(f"🏁 Final Score: {score}/15")
print("--------------------------------------------------")

if score == 15:
    print("🌟 PERFECT SCORE! Outstanding performance!")
elif score >= 10:
    print("💪 Great job! You have strong Python skills!")
elif score >= 5:
    print("🙂 Not bad! Keep practicing to improve.")
else:
    print("😕 Needs improvement. Keep learning and trying!")

