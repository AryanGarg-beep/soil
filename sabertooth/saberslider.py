import tkinter as tk
import serial
import time

# try:
#     ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
#     print(f"Connected to {ser.portstr}")
# except serial.SerialException as e:
#     print(f"Error: {e}")
#     exit(1)


current_direction = "stop"

def send_command(command, direction):
    try:
        command = int(command)
        if direction == "forward":
            command1 = command + 64
            command2 = command + 192
        elif direction == "backward":
            command1 = 64 - command
            command2 = 192 - command
        elif direction == "left":
            command1 = command + 64
            command2 = 192 - command
        elif direction == "right":
            command1 = 64 - command
            command2 = command + 192
        else:  #i will make this as emergency command
            command1 = 0
            command2 = 0


        # ser.write(command_byte)
        print(f"Command sent: {direction} | slider={command} (0x{command:02X}) | motor1={command1} | motor2={command2}")

    except Exception as e:
        print(f"Failed to send command: {e}")

# Functions to update direction
def update_direction(direction):
    global current_direction
    current_direction = direction
    send_command(slider.get(), current_direction)

def forward():
    update_direction("forward")

def backward():
    update_direction("backward")

def left():
    update_direction("left")

def right():
    update_direction("right")

def stop():
    update_direction("stop")


def update_speed(value):
    global current_direction
    send_command(value, current_direction)


app = tk.Tk()
app.title("Motor Control")

app.configure(bg="#0F0F0F")
#STYLR:D
button_style = {
    "bg": "#00FF00",
    "fg": "#0F0F0F",
    "activebackground": "#00CC00",
    "activeforeground": "#FFFFFF",
    "font": ("Courier New", 14, "bold"),
    "bd": 5,
    "relief": "ridge",
}


hello_button = tk.Button(app, text="^", command=forward, **button_style)
second_button = tk.Button(app, text="\/", command=backward, **button_style)
third_button = tk.Button(app, text="<", command=left, **button_style)
forth_button = tk.Button(app, text=">", command=right, **button_style)
stop_button = tk.Button(app, text="stop", command=stop, **button_style)


slider = tk.Scale(app, from_=0, to=63, orient=tk.HORIZONTAL, command=update_speed)
slider.set(0)

# Layout for buttons and slider
hello_button.grid(row=0, column=2, padx=15, pady=10)
second_button.grid(row=2, column=2, padx=15, pady=10)
third_button.grid(row=1, column=1, padx=15, pady=10)
forth_button.grid(row=1, column=3, padx=15, pady=10)
stop_button.grid(row=1, column=2, padx=15, pady=10)
slider.grid(row=3, column=0, columnspan=5, padx=10, pady=20)

# Set window size
app.geometry("395x250")
app.mainloop()

# ser.close()  

