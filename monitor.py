import psutil
import tkinter as tk
from tkinter import ttk

running = False  # monitoring state

def get_cpu():
    return psutil.cpu_percent(interval=1)

def get_ram():
    return psutil.virtual_memory().percent

def get_disk():
    return psutil.disk_usage('/').percent

def get_color(value):
    if value < 50:
        return "green"
    elif value < 80:
        return "orange"
    else:
        return "red"

def toggle_monitoring():
    global running
    running = not running
    if running:
        status_label.config(text="Status: RUNNING", fg="green")
        toggle_btn.config(text="STOP")
        update()
    else:
        status_label.config(text="Status: STOPPED", fg="red")
        toggle_btn.config(text="START")

def update():
    if not running:
        return

    cpu = get_cpu()
    ram = get_ram()
    disk = get_disk()

    cpu_bar['value'] = cpu
    ram_bar['value'] = ram
    disk_bar['value'] = disk

    cpu_label.config(text=f"CPU: {cpu}%", fg=get_color(cpu))
    ram_label.config(text=f"RAM: {ram}%", fg=get_color(ram))
    disk_label.config(text=f"Disk: {disk}%", fg=get_color(disk))

    if cpu > 80:
        alert_label.config(text="⚠ HIGH CPU USAGE!", fg="red")
    else:
        alert_label.config(text="")

    window.after(1000, update)

# Window
window = tk.Tk()
window.title("Smart System Monitor")
window.geometry("450x420")
window.configure(bg="#121212")

# Title
tk.Label(
    window,
    text="SMART SYSTEM MONITOR",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="white"
).pack(pady=10)

# Status
status_label = tk.Label(
    window,
    text="Status: STOPPED",
    font=("Arial", 12, "bold"),
    bg="#121212",
    fg="red"
)
status_label.pack(pady=5)

# CPU
cpu_label = tk.Label(window, font=("Arial", 12), bg="#121212")
cpu_label.pack()
cpu_bar = ttk.Progressbar(window, length=320, maximum=100)
cpu_bar.pack(pady=5)

# RAM
ram_label = tk.Label(window, font=("Arial", 12), bg="#121212")
ram_label.pack()
ram_bar = ttk.Progressbar(window, length=320, maximum=100)
ram_bar.pack(pady=5)

# Disk
disk_label = tk.Label(window, font=("Arial", 12), bg="#121212")
disk_label.pack()
disk_bar = ttk.Progressbar(window, length=320, maximum=100)
disk_bar.pack(pady=5)

# Alert
alert_label = tk.Label(
    window,
    font=("Arial", 14, "bold"),
    bg="#121212"
)
alert_label.pack(pady=10)

# Button
toggle_btn = tk.Button(
    window,
    text="START",
    font=("Arial", 12, "bold"),
    width=15,
    command=toggle_monitoring
)
toggle_btn.pack(pady=15)

window.mainloop()


