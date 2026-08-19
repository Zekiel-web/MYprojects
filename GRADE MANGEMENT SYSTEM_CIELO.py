
import tkinter as tk
from tkinter import messagebox


def getStudentInfo():
    return name_entry.get()

def getQuizScores():
    try:
        q1 = float(q1_entry.get())
        q2 = float(q2_entry.get())
        q3 = float(q3_entry.get())
        return [q1, q2, q3]
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid quiz scores.")
        return None

def computeAverage(scores):
    return sum(scores) / len(scores)

def clampAverage(avg):
    if avg < 65:
        return 65
    elif avg > 100:
        return 100
    return avg

def determineGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def processResult(event=None):
    name = getStudentInfo()
    scores = getQuizScores()

    if scores:
        raw_average = computeAverage(scores)
        average = clampAverage(raw_average)  
        grade = determineGrade(average)

        result_text.config(
            text=(
                f"Student Name: {name}\n"
                f"Quiz Scores: {scores}\n"
                f"Average Score: {average:.2f}\n"
                f"Letter Grade: {grade}"
            )
        )

root = tk.Tk()
root.title("Student Grade Management System")
root.geometry("520x560")
root.configure(bg="#555555")
root.resizable(False, False)

tk.Label(
    root,
    text="Student grade mangement system",
    font=("Arial", 18, "bold"),
    bg="#555555",
    fg="white"
).pack(pady=15)

top_frame = tk.Frame(root, bg="#555555")
top_frame.pack(pady=20)

left_frame = tk.Frame(top_frame, bg="#555555")
left_frame.grid(row=0, column=0, padx=30)

tk.Label(
    left_frame,
    text="ENTER STUDENT NAME:",
    font=("Arial", 11),
    bg="#555555",
    fg="white"
).pack(anchor="w", pady=5)

name_entry = tk.Entry(left_frame, font=("Arial", 12), width=20)
name_entry.pack()
name_entry.focus()

right_frame = tk.Frame(top_frame, bg="#555555")
right_frame.grid(row=0, column=1, padx=30)

tk.Label(right_frame, text="Quiz 1 Score", font=("Arial", 11), bg="#555555", fg="white").pack(anchor="w")
q1_entry = tk.Entry(right_frame, font=("Arial", 12), width=20)
q1_entry.pack(pady=5)

tk.Label(right_frame, text="Quiz 2 Score", font=("Arial", 11), bg="#555555", fg="white").pack(anchor="w")
q2_entry = tk.Entry(right_frame, font=("Arial", 12), width=20)
q2_entry.pack(pady=5)

tk.Label(right_frame, text="Quiz 3 Score", font=("Arial", 11), bg="#555555", fg="white").pack(anchor="w")
q3_entry = tk.Entry(right_frame, font=("Arial", 12), width=20)
q3_entry.pack(pady=5)

tk.Button(
    root,
    text="Compute Result",
    font=("Arial", 13, "bold"),
    bg="#3498db",
    fg="white",
    width=18,
    command=processResult
).pack(pady=15)

result_text = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#f3ede4",
    width=46,
    height=8,
    justify="left",
    anchor="nw",
    relief="solid"
)
result_text.pack(pady=15)

root.bind("<Return>", processResult)

root.mainloop()
