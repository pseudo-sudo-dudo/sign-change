import customtkinter as ctk
from collections import Counter

class SignChangerApp:
    def __init__(self, root):
        ctk.set_appearance_mode("System")  # Dark/Light mode based on system settings
        ctk.set_default_color_theme("blue")
        
        self.root = root
        self.root.title("Church Sign Changer")
        self.root.geometry("800x600")
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        
        font_size = 20
        
        # Labels
        ctk.CTkLabel(root, text="Original Sign Message:", font=("Verdana", font_size, "bold")).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        ctk.CTkLabel(root, text="New Sign Message:", font=("Verdana", font_size, "bold")).grid(row=1, column=0, padx=10, pady=5, sticky="w")
        
        # Entry Fields
        self.original_entry = ctk.CTkEntry(root, font=("Arial", font_size))
        self.original_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
        
        self.new_entry = ctk.CTkEntry(root, font=("Arial", font_size))
        self.new_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        
        # Button
        self.compare_button = ctk.CTkButton(root, text="Compare", font=("Arial", font_size), command=self.compare_signs)
        self.compare_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Result Display
        self.result_text = ctk.CTkTextbox(root, font=("Arial", font_size))
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")
        
    def compare_signs(self):
        original_sign = self.original_entry.get().replace("\n", " ").replace("\r", " ").strip()
        new_sign = self.new_entry.get().replace("\n", " ").replace("\r", " ").strip()
        
        diff_letters, useless_letters = self.find_differences(original_sign, new_sign)
        
        result_output = ""
        if diff_letters:
            result_output += "Letters to grab:\n"
            for char, count in sorted(diff_letters.items()):
                result_output += f"{char} - {count}\n"
        else:
            result_output += "There is no differences!\n"
        
        if useless_letters:
            result_output += "\nLetters you no longer need from the original:\n"
            for char, count in sorted(useless_letters.items()):
                result_output += f"{char} - {count}\n"
        
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", result_output)
    
    def find_differences(self, ogSign, newSign):
        ogSign = ogSign.replace(" ", "").upper()
        newSign = newSign.replace(" ", "").upper()
        
        ogCount = Counter(ogSign)
        newCount = Counter(newSign)
        
        differences = Counter(newCount) - Counter(ogCount)
        notNeededLetters = Counter(ogCount) - Counter(newCount)
        
        return dict(differences), dict(notNeededLetters)

if __name__ == "__main__":
    root = ctk.CTk()
    app = SignChangerApp(root)
    root.mainloop()
