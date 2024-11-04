import pyautogui
import time
#You need one Position for Input Field and one Position for send Button.
print("Move Mouse to Position and press CTRL + C, to show Position.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Position: X={x}, Y={y}", end="\r")
        time.sleep(0.1) 
except KeyboardInterrupt:
    print("\nProgramme completed.")
