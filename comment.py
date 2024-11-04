import pyautogui
import time

# Positions
x1, y1 = 100, 200  # Position Input Field
x2, y2 = 150, 250  # Position Send-Button


text = "Your text could be placed here"
repetitions = int(input("How often should the text be sent? "))

# Time to choose correct Window
time.sleep(3)

# Sending Text
for _ in range(repetitions):
    
    pyautogui.click(x1, y1)
    time.sleep(0.5)
  
    pyautogui.write(text, interval=0.1)

    time.sleep(0.5)
    pyautogui.click(x2, y2)

    # Adjust waiting time between messages, if desired
    time.sleep(1)  # Wait 1 second before the next message
#Optional
#print("Text was sent the desired number.")
