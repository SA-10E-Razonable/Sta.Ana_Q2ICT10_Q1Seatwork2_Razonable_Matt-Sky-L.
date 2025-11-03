from pyscript import display, document
import random

def general_weighted_average(e):
    for element in ['student_info', 'summary', 'output', 'quote']:
        document.getElementById(element).innerHTML = ''

    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    grades = []
    for sub in ['science', 'math', 'english', 'filipino', 'ict', 'pe']:
        try:
            g = float(document.getElementById(sub).value)
            grades.append(g)
        except:
            display("Please fill in all grades correctly!", target="output")
            return

    weights = [5, 4, 3, 2, 3, 1]
    weighted_sum = sum(g * w for g, w in zip(grades, weights))
    gwa = weighted_sum / sum(weights)

    info = f"Name: {first_name} {last_name}"
    summary = "\n".join([f"{sub}: {gr:.0f}" for sub, gr in zip(subjects, grades)])
    result = f"Your general weighted average is {gwa:.2f}"

    quotes = [
        "Keep aiming higher! 🌟",
        "Hard work pays off — stay consistent! 💪",
        "You're doing great — keep learning! 📘",
        "Success is built one grade at a time! 🏆"
    ]

    display(info, target="student_info")
    display(summary, target="summary")
    display(result, target="output")
    display(random.choice(quotes), target="quote")

def reset_form(e):
    for field in ['first_name', 'last_name', 'science', 'math', 'english', 'filipino', 'ict', 'pe']:
        document.getElementById(field).value = ''
    for element in ['student_info', 'summary', 'output', 'quote']:
        document.getElementById(element).innerHTML = ''