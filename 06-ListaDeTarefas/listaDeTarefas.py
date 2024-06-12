import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista de Tarefas")

        self.tasks = []

        self.label = tk.Label(master, text="Digite a tarefa:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.add_button = tk.Button(master, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.remove_button = tk.Button(master, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa!")

    def remove_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa!")

    def update_tasks_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()