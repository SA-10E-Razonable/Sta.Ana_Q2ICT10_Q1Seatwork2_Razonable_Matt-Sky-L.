from pyscript import display, document
import random, asyncio

async def general_weighted_average(e):
    eq = document.getElementById("equalizer")
    eq.style.display = "flex"

    for el in ['student_info', 'summary', 'output', 'quote']:
        document.getElementById(el).innerHTML = ''

    await asyncio.sleep(1.5) 

    first_name = document.getElementById('first_name').value.strip()
    last_name = document.getElementById('last_name').value.strip()

    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    ids = ['science', 'math', 'english', 'filipino', 'ict', 'pe']
    grades = []

    for sub in ids:
        try:
            g = float(document.getElementById(sub).value)
            grades.append(g)
        except:
            display("⚠️ Please fill in all grades correctly!", target="output")
            eq.style.display = "none"
            return

    weights = [5, 4, 3, 2, 3, 1]
    gwa = sum(g * w for g, w in zip(grades, weights)) / sum(weights)

    info = f"🎤 Student: {first_name} {last_name}"
    summary = "\n".join([f"{s}: {g:.0f}" for s, g in zip(subjects, grades)])
    result = f"🎶 Your GWA is {gwa:.2f} 🎵"

    quotes = [
        "You're hitting all the right notes! 🎼",
        "Keep your rhythm steady — success is in tune! 🎷",
        "Encore! You’re doing great! 🎺",
        "Your hard work is pure harmony. 🎻"
    ]

    display(info, target="student_info")
    display(summary, target="summary")
    display(result, target="output")
    display(random.choice(quotes), target="quote")

    await asyncio.sleep(2)
    eq.style.display = "none"

def reset_form(e):
    for field in ['first_name', 'last_name', 'science', 'math', 'english', 'filipino', 'ict', 'pe']:
        document.getElementById(field).value = ''
    for el in ['student_info', 'summary', 'output', 'quote']:
        document.getElementById(el).innerHTML = ''
    document.getElementById("equalizer").style.display = "none"
