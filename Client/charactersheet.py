import tkinter as tk
from tkinter import messagebox

class CharacterSheetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("キャラシ")

        self.create_label_entry("キャラクター名", 0)
        self.create_label_entry("種族", 1)
        self.create_label_entry("クラス", 2)
        self.create_label_entry("レベル", 3)

        # 能力値
        self.stats = ["筋力", "生命", "敏捷", "知力", "精神", "魅力"]
        self.stat_entries = {}
        for i, stat in enumerate(self.stats):
            label = tk.Label(self.root, text=stat)
            label.grid(row=i+4, column=1, padx=5, pady=2, sticky="e")
            entry = tk.Entry(self.root)
            entry.grid(row=i+4, column=1, padx=5, pady=2)
            self.stat_entries[stat] = entry

        # メモ欄
        memo_label = tk.Label(self.root, text="memo")
        memo_label.grid(row=10, column=0, padx=5, pady=5, sticky="ne")
        self.memo_text = tk.Text(self.root, height=5, width=30)
        self.memo_text.grid(row=10, column=1, padx=5, pady=5)

        # 保存ボタン
        save_button = tk.Button(self.root, text="保存", command=self.save_character)
        save_button.grid(row=11, column=1, pady=10)

    def create_label_entry(self, label_text, row):
        label = tk.Label(self.root, text=label_text)
        label.grid(row=row, column=0, padx=5, pady=2, sticky="e")
        entry = tk.Entry(self.root)
        entry.grid(row=row, column=1, padx=5, pady=2)
        setattr(self, f"entry_{label_text}", entry)

    def save_character(self):
        data = {
            "キャラクター名": self.entry_キャラクター名.get(),
            "種族": self.entry_種族.get(),
            "クラス": self.entry_クラス.get(),
            "レベル": self.entry_レベル.get(),
            "能力値": {stat: self.stat_entries[stat].get() for stat in self.stats},
            "メモ": self.memo_text.get("1.0", tk.END).strip()
        }

        # 保存
        print("キャラクター情報:")
        for key, value in data.items():
            print(f"{key}: {value}")
        messagebox.showinfo("保存完了", "キャラクター情報を保存しました")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterSheetApp(root)
    root.mainloop()
        