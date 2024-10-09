import tkinter as tk
import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    print(f"Connected to {ser.portstr}")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command}(0x{command:02X})")
    except Exception as e:
        print(f"Failed to send command: {e}")


def forward():
    print("moving forward")
    send_command(64+32)
    send_command(192+32)

def backward():
    print("moving backward")
    send_command(64-32)
    send_command(192-32)

def left():
    print("turning left")
    send_command(64+32)
    send_command(192-32)

def right():
    print("turning right")
    send_command(64-32)
    send_command(192+32)

def stop():
    print("stopping")
    send_command(0)

app = tk.Tk()
app.title("ROVER")

app.configure(bg="#0F0F0F")  # Dark background

# Style options
button_style = {
    "bg": "#00FF00",  # Neon green background for the button
    "fg": "#0F0F0F",  # Dark text color for contrast
    "activebackground": "#00CC00",  # Darker green when clicked
    "activeforeground": "#FFFFFF",  # White text when active
    "font": ("Courier New", 14, "bold"),  # Futuristic font
    "bd": 5,  # Border width
    "relief": "ridge",  # Button style
}



# Button with command
hello_button = tk.Button(app, text="^", command=forward, **button_style)
second_button = tk.Button(app, text="\/", command=backward, **button_style)
third_button = tk.Button(app, text="<", command=left, **button_style)
forth_button = tk.Button(app, text=">",command=right, **button_style)
stop_button = tk.Button(app, text="stop", command=stop, **button_style)
deco_button = tk.Button(app, text="Rover control")

hello_button.grid(row=0, column=2, padx=15, pady=10)  # Position in grid
second_button.grid(row=2, column=2, padx=15, pady=10)
third_button.grid(row=1, column=3, padx=15, pady=10)
forth_button.grid(row=1,column=4,padx=15, pady=10)
stop_button.grid(row=1,column=2,padx=15,pady=10)
#deco_button.grid(row=0, column=3,padx=20,pady=15)

app.geometry("260x200")
app.mainloop()

ser.close()

