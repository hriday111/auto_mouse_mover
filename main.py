import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
try:
    from pynput.mouse import Button, Controller
except:
    install("pynput")
import time
mouse = Controller()
pixels_to_move=20
if len(sys.argv)>1:
    try:
        pixels_to_move=int(sys.argv[1])
    except:
        print("you seemedto have enter a value that is not a number")



while True:
    try:
        mouse.move(0,pixels_to_move)
        time.sleep(2)
        mouse.move(0,-pixels_to_move)
        time.sleep(2)
    
    except KeyboardInterrupt:
        print("You seemed to have pressed CTRL+c, good bye :) ")
        exit()
    except Exception as e:
        print("An unexpected error occurred.")
        print(e)
