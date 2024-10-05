import time
import matplotlib.pyplot as plt

# PID controller class
class PID:
    def __init__(self, kp, ki, kd, setpoint=0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0
        self.previous_error = 0

    def compute(self, input_value, dt):
        # Calculate error
        error = self.setpoint - input_value

        # Proportional term
        P = self.kp * error

        # Integral term
        self.integral += error * dt
        I = self.ki * self.integral

        # Derivative term
        derivative = (error - self.previous_error) / dt
        D = self.kd * derivative

        # Remember for next iteration
        self.previous_error = error

        # Output
        return P + I + D

# Simulate a virtual servo motor (simplified model)
class VirtualServo:
    def __init__(self, initial_position=0):
        self.position = initial_position
        self.speed = 0

    def update(self, control_signal, dt):
        # Update the position based on the control signal (simplified dynamics)
        self.speed = control_signal  # Control signal acts like a speed
        self.position += self.speed * dt

        # Constrain position to typical servo limits (0 to 180 degrees)
        if self.position > 180:
            self.position = 180
        elif self.position < 0:
            self.position = 0

        return self.position

# Simulation parameters
setpoint = 90  # Target position for the servo motor
kp = 1.2       # Proportional gain
ki = 0.02      # Integral gain
kd = 0.01      # Derivative gain
simulation_time = 10  # seconds
dt = 0.01  # Time step (100 Hz control loop)

# Create PID controller and virtual servo
pid = PID(kp, ki, kd, setpoint=setpoint)
servo = VirtualServo()

# Store data for plotting
time_data = []
position_data = []
setpoint_data = []

# Run simulation
current_time = 0
while current_time < simulation_time:
    # Get the current servo position
    current_position = servo.position

    # Compute the control signal from the PID controller
    control_signal = pid.compute(current_position, dt)

    # Update the virtual servo position based on the control signal
    new_position = servo.update(control_signal, dt)

    # Save data for plotting
    time_data.append(current_time)
    position_data.append(new_position)
    setpoint_data.append(setpoint)

    # Wait for the next time step
    time.sleep(dt)
    current_time += dt

# Plot the results
plt.plot(time_data, position_data, label='Servo Position')
plt.plot(time_data, setpoint_data, label='Setpoint', linestyle='--')
plt.xlabel('Time (s)')
plt.ylabel('Position (degrees)')
plt.title('PID Control of Virtual Servo Motor')
plt.legend()
plt.grid(True)
plt.show()

