import psutil
import ttkbootstrap as tb
from batteryinfo import Battery
import threading
import time

root = tb.Window(themename="minty")
root.title("Battery Widget")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.wm_attributes('-transparentcolor', 'gray')
root.config(bg='gray')

def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = root.winfo_x() - root.x + event.x
    y = root.winfo_y() - root.y + event.y
    root.geometry(f"+{x}+{y}")

root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

widget_label = tb.Label(
    root, text="", font=('Segoe UI', 11), bootstyle="secondary", background='gray'
)
widget_label.pack(padx=12, pady=6)

def get_battery_details():
    try:
        bat = Battery()
        full = bat.energy_full.value if bat.energy_full else None
        design = bat.energy_full_design.value if bat.energy_full_design else None
        temp = bat.temperature.value if bat.temperature else None
        cycles = bat.cycle_count if bat.cycle_count else None
        health = (full / design) * 100 if full and design else None
        return health, temp, cycles, design, full
    except Exception:
        return None, None, None, None, None

def update_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = battery.power_plugged
            health, temp, cycles, design, full = get_battery_details()
            health_text = f"{health:.1f}%" if health else "N/A"
            temp_text = f"{temp}°C" if temp else "N/A"
            cycles_text = str(cycles) if cycles else "N/A"
            design_text = f"{design}mWh" if design else "N/A"
            full_text = f"{full}mWh" if full else "N/A"
            status = "Charging" if plugged else "On Battery"

            widget_label.config(
                text=f"{percent}% | {status} | Health: {health_text} | Temp: {temp_text} | Cycles: {cycles_text} | Design: {design_text} | Full: {full_text}"
            )
        time.sleep(5)

threading.Thread(target=update_battery, daemon=True).start()
root.mainloop()
