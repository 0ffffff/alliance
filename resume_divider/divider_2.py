import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import StringVar, IntVar, messagebox

class ResumeDividerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Divider")
        self.num_resumes = IntVar()
        self.num_reviewers = IntVar()
        self._setup_widgets()

    def _setup_widgets(self):
        ttk.Label(self.root, text="Number of resumes to review:").grid(row=0, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.num_resumes).grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Number of people reviewing:").grid(row=1, column=0, padx=10, pady=10)
        ttk.Entry(self.root, textvariable=self.num_reviewers).grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(self.root, text="Submit", bootstyle=SUCCESS, command=self.on_submit).grid(row=2, column=0, columnspan=2, pady=20)

    def on_submit(self):
        try:
            n_resumes = self.num_resumes.get()
            n_reviewers = self.num_reviewers.get()
            if n_reviewers == 0:
                messagebox.showerror("Error", "Number of people reviewing cannot be zero!")
                return
            resumes_per = n_resumes // n_reviewers
            remainder = n_resumes % n_reviewers
            if remainder == 0:
                message = f"Each person should review {resumes_per} resumes."
            else:
                message = (f"Each person should review at least {resumes_per} resumes.\n"
                           f"{remainder} person(s) should review one more resume.")
            messagebox.showinfo("Resume Division Result", message)
        except Exception as e:
            messagebox.showerror("Error", f"Input error: {str(e)}")

if __name__ == "__main__":
    app = ttk.Window(themename="flatly")  # Choose a modern theme
    ResumeDividerApp(app)
    app.mainloop()