import tkinter as tk
from tkinter import scrolledtext

class NewspaperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Newspaper App")

        # Create a list of sample news articles
        self.news_articles = [
            "Headline 1: This is the first news article.",
            "Headline 2: Another interesting news piece.",
            "Headline 3: More news to keep you informed.",
            "Headline 1: This is the first news article.",
            "Headline 2: Another interesting news piece.",
            "Headline 3: More news to keep you informed.",
            "Headline 1: This is the first news article.",
            "Headline 2: Another interesting news piece.",
            "Headline 3: More news to keep you informed.",
            # Add more articles as needed
        ]

        # Create and configure the UI elements
        self.label = tk.Label(root, text="Newspaper Headlines", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, font=("Helvetica", 12))
        self.text_widget.pack(pady=10)

        self.show_news_button = tk.Button(root, text="Show News", command=self.show_news)
        self.show_news_button.pack(pady=10)

        # Display the UI
        self.root.mainloop()

    def show_news(self):
        # Clear previous text
        self.text_widget.delete(1.0, tk.END)

        # Display each news article in the scrolled text widget
        for article in self.news_articles:
            self.text_widget.insert(tk.END, article + "\n\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = NewspaperApp(root)
