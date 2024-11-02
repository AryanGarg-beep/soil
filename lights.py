import RPi.GPIO as GPIO
import time

# GPIO pin assignments for each relay channel
UV_LIGHT_1 = 17  # Relay Channel 1
UV_LIGHT_2 = 27  # Relay Channel 2
ALWAYS_ON_LED = 22  # Relay Channel 3
SPECTRO_LED = 23  # Relay Channel 4

# Setup GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up each relay channel as output
GPIO.setup(UV_LIGHT_1, GPIO.OUT)
GPIO.setup(UV_LIGHT_2, GPIO.OUT)
GPIO.setup(ALWAYS_ON_LED, GPIO.OUT)
GPIO.setup(SPECTRO_LED, GPIO.OUT)

# Initialize relay states (assuming LOW is ON and HIGH is OFF)
GPIO.output(UV_LIGHT_1, GPIO.HIGH)
GPIO.output(UV_LIGHT_2, GPIO.HIGH)
GPIO.output(ALWAYS_ON_LED, GPIO.LOW)  # Always-on LED is ON by default
GPIO.output(SPECTRO_LED, GPIO.HIGH)

def uv_lights_on():
    GPIO.output(UV_LIGHT_1, GPIO.LOW)
    GPIO.output(UV_LIGHT_2, GPIO.LOW)
    print("UV Lights ON for 2 minutes")
    time.sleep(120)  # Keep UV lights on for 2 minutes
    GPIO.output(UV_LIGHT_1, GPIO.HIGH)
    GPIO.output(UV_LIGHT_2, GPIO.HIGH)
    print("UV Lights OFF")

def spectroscopy_light_on():
    # Turn off all other lights
    GPIO.output(UV_LIGHT_1, GPIO.HIGH)
    GPIO.output(UV_LIGHT_2, GPIO.HIGH)
    GPIO.output(ALWAYS_ON_LED, GPIO.HIGH)
    
    # Turn on spectroscopy LED
    GPIO.output(SPECTRO_LED, GPIO.LOW)
    print("Spectroscopy LED ON")
    
def spectroscopy_light_off():
    # Turn off spectroscopy LED and restore other lights' states
    GPIO.output(SPECTRO_LED, GPIO.HIGH)
    GPIO.output(ALWAYS_ON_LED, GPIO.LOW)
    print("Spectroscopy LED OFF")

try:
    # Run the UV lights for 2 minutes initially
    uv_lights_on()
    
    # Spectroscopy process (example of turning on and off)
    spectroscopy_light_on()
    time.sleep(5)  # Replace with actual spectroscopy process duration
    spectroscopy_light_off()
    
    # Keep the always-on LED running (Loop to prevent code from ending)
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO settings on exit
    GPIO.cleanup()
    print("Program exited and GPIO cleaned up")

