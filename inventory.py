Código completo de la aplicación de gestión de inventarios con tkinter

import tkinter as tk
import json

Función para agregar un elemento al inventario

def add_item():
name = name_entry.get()
quantity = int(quantity_entry.get())
inventory[name] = quantity
name_entry.delete(0, tk.END)
quantity_entry.delete(0, tk.END)
update_inventory()

Función para actualizar la cantidad de un elemento existente en el inventario

def update_quantity():
index = name_listbox.curselection()[0]
name = name_listbox.get(index)
quantity = int(quantity_entry_2.get())
inventory[name] = quantity
quantity_entry_2.delete(0, tk.END)
update_inventory()

Función para eliminar un elemento del inventario

def delete_item():
index = name_listbox.curselection()[0]
name = name_listbox.get(index)
del inventory[name]
update_inventory()

Función para actualizar el listbox y el text widget del inventario

def update_inventory():
name_listbox.delete(0, tk.END)
inventory_text.delete("1.0", tk.END)
for name, quantity in inventory.items():
name_listbox.insert(tk.END, name)
inventory_text.insert(tk.END, f"{name}: {quantity}\n")
status_label.config(text="Inventario actualizado", fg="green")

Función para guardar el inventario en un archivo

def save_inventory():
with open("inventory.json", "w") as f:
json.dump(inventory, f)
status_label.config(text="Inventario guardado en archivo", fg="green")

Función para cargar el inventario desde un archivo

def load_inventory():
try:
with open("inventory.json", "r") as f:
inventory.update(json.load(f))
update_inventory()
status_label.config(text="Inventario cargado desde archivo", fg="green")
except FileNotFoundError:
status_label.config(text="Archivo de inventario no encontrado", fg="red")

Crear la ventana principal de la GUI

window = tk.Tk()
window.title("Gestión de inventarios")

Crear el diccionario del inventario

inventory = {}

Crear los widgets de la GUI

name_label = tk.Label(window, text="Nombre del elemento:")
name_label.grid(column=0, row=0, padx=10, pady=10)
name_entry = tk.Entry(window)
name_entry.grid(column=1, row=0, padx=10, pady=10)

quantity_label = tk.Label(window, text="Cantidad del elemento:")
quantity_label.grid(column=0, row=1, padx=10, pady=10)
quantity_entry = tk.Entry(window)
quantity_entry.grid(column=1, row=1, padx=10, pady=10)

add_button = tk.Button(window, text="Agregar elemento", command=add_item)
add_button.grid(column=1, row=2, padx=10, pady=10)

inventory_label = tk.Label(window, text="Inventario:")
inventory_label.grid(column=2, row=0, padx=10, pady=10)
inventory_text = tk.Text(window, width=30, height=10)
inventory_text.grid(column=2, row=1, rowspan=3, padx=10, pady=10)

name_listbox_label = tk.Label(window, text="Seleccionar elemento:")
name_listbox_label.grid(column=0, row=3, padx=10, pady=10)
name_listbox = tk.Listbox(window)
name_listbox.grid(column=1, row=3, padx=10, pady=10)

quantity_label
quantity_label_2 = tk.Label(window, text="Nueva cantidad:")
quantity_label_2.grid(column=0, row=4, padx=10, pady=10)
quantity_entry_2 = tk.Entry(window)
quantity_entry_2.grid(column=1, row=4, padx=10, pady=10)

update_button = tk.Button(window, text="Actualizar cantidad", command=update_quantity)
update_button.grid(column=1, row=5, padx=10, pady=10)

delete_button = tk.Button(window, text="Eliminar elemento", command=delete_item)
delete_button.grid(column=1, row=6, padx=10, pady=10)

save_button = tk.Button(window, text="Guardar inventario", command=save_inventory)
save_button.grid(column=2, row=4, padx=10, pady=10)

load_button = tk.Button(window, text="Cargar inventario", command=load_inventory)
load_button.grid(column=2, row=5, padx=10, pady=10)

status_label = tk.Label(window, text="Bienvenido", fg="blue")
status_label.grid(column=0, row=7, columnspan=3, padx=10, pady=10)

Cargar el inventario desde un archivo al inicio de la aplicación

load_inventory()

Ejecutar el loop principal de la GUI

window.mainloop()