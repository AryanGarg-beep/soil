import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# PID controller class (as in previous examples)
class PID:
    def __init__(self, kp, ki, kd, setpoint=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.previous_error = 0

    def compute(self, input_value, dt):
        error = self.setpoint - input_value
        P = self.kp * error
        self.integral += error * dt
        I = self.ki * self.integral
        derivative = (error - self.previous_error) / dt
        D = self.kd * derivative
        self.previous_error = error
        return P + I + D

# Virtual servo motor class (as in previous examples)
class VirtualServo:
    def __init__(self, initial_position=0):
        self.position = initial_position

    def update(self, control_signal, dt):
        self.position += control_signal * dt
        self.position = np.clip(self.position, 0, 180)
        return self.position

# Simulation parameters
setpoint = 90
kp = 1.2
ki = 0.1
kd = 0.05
dt = 0.1

pid = PID(kp, ki, kd, setpoint=setpoint)
servo = VirtualServo()

time_data = []
position_data = []
setpoint_data = []

fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Servo Position', color='blue')
line2, = ax.plot([], [], label='Setpoint', linestyle='--', color='orange')
ax.set_ylim(0, 180)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position (degrees)')
ax.set_title('Real-Time PID Control of Virtual Servo Motor with Dynamic Setpoint')
ax.legend()
ax.grid()

manual_noise = 0

# Function to set noise from user input
def set_manual_noise():
    global manual_noise, pid
    try:
        noise_input = input("Enter noise or type 'set 100' to move to 100 degrees (negative to subtract, '0' to reset, 'exit' to stop): ")
        if noise_input.lower() == 'exit':
            plt.close()
            return
        elif noise_input.lower().startswith('set'):
            new_setpoint = float(noise_input.split()[1])
            pid.setpoint = new_setpoint
            print(f"Setpoint changed to {new_setpoint} degrees")
        else:
            manual_noise = float(noise_input)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Animation function
def animate(i):
    global time_data, position_data, setpoint_data
    
    # Get current time
    current_time = i * dt
    
    # Compute control signal
    current_position = servo.position
    noisy_position = current_position + manual_noise
    control_signal = pid.compute(noisy_position, dt)
    new_position = servo.update(control_signal, dt)
    
    # Save data for plotting
    time_data.append(current_time)
    position_data.append(new_position)
    setpoint_data.append(pid.setpoint)
    
    # Adjust the x-axis to show the most recent 20 seconds
    if current_time > 20:
        ax.set_xlim(current_time - 20, current_time)
    else:
        ax.set_xlim(0, 20)
    
    # Update plot data
    line1.set_data(time_data, position_data)
    line2.set_data(time_data, setpoint_data)
    
    # Redraw the canvas to update the axis limits
    ax.figure.canvas.draw()
    
    return line1, line2

# Start a thread to allow for manual noise and setpoint input
import threading

def input_thread():
    while True:
        set_manual_noise()

# Run the input thread
threading.Thread(target=input_thread, daemon=True).start()

# Run the animation with a slower interval to observe changes
ani = animation.FuncAnimation(fig, animate, frames=200, interval=100, blit=False)
plt.show()

