import tkinter as tk
from tkinter import messagebox

def calculate_and_show():
    try:
        num_resumes = int(resume_entry.get())
        num_reviewers = int(reviewer_entry.get())
        if num_reviewers == 0:
            messagebox.showerror("Error", "Number of people reviewing cannot be zero!")
            return
        resumes_per_person = num_resumes // num_reviewers
        remainder = num_resumes % num_reviewers
        if remainder == 0:
            message = f"Each person should review {resumes_per_person} resumes."
        else:
            message = (f"Each person should review at least {resumes_per_person} resumes.\n"
                       f"{remainder} person(s) should review one more resume.")
        messagebox.showinfo("Resume Divider Result", message)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integer values!")

root = tk.Tk()
root.title("Resume Divider")

tk.Label(root, text="Number of resumes to review:").grid(row=0, column=0, padx=10, pady=10)
resume_entry = tk.Entry(root)
resume_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Number of people reviewing:").grid(row=1, column=0, padx=10, pady=10)
reviewer_entry = tk.Entry(root)
reviewer_entry.grid(row=1, column=1, padx=10, pady=10)

submit_btn = tk.Button(root, text="Submit", command=calculate_and_show)
submit_btn.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()