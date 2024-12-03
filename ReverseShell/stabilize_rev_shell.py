import pyautogui
import time
import pty


def dumb_to_smart():
    lines = input("No. of lines your terminal has: ") #Command to determine number of lines = tput lines
    columns = input("No. of columns your terminal has: ") #Command to determine number of columns = tput cols

    print("[!] Take your cursor to the terminal in which the nc session is running")

    time.sleep(3)

    print("Initializing Script...")

    # Define the command string
    command1 = "python3 -c 'import pty; pty.spawn"
    command2 = "bin"
    command3 = "bash"
    command4 = "'"

    # Write the command with pyautogui
    pyautogui.press("p")
    pyautogui.press("y")
    pyautogui.press("t")
    pyautogui.press("h")
    pyautogui.press("o")
    pyautogui.press("n")
    pyautogui.press("3")
    pyautogui.press("space")    
    pyautogui.press("-")  
    pyautogui.press("c")
    pyautogui.press("space")   
    pyautogui.press("'")
    pyautogui.press("i")
    pyautogui.press("m")
    pyautogui.press("p")
    pyautogui.press("o")
    pyautogui.press("r")
    pyautogui.press("t")
    pyautogui.press("space")
    pyautogui.press("p")
    pyautogui.press("t")
    pyautogui.press("y")
    with pyautogui.hold("shift"):
        pyautogui.press(";")
    pyautogui.press("space")
    pyautogui.press("p")
    pyautogui.press("t")
    pyautogui.press("y")
    pyautogui.press(".")
    pyautogui.press("s")
    pyautogui.press("p")
    pyautogui.press("a")
    pyautogui.press("w")
    pyautogui.press("n")
    with pyautogui.hold("shift"):
        pyautogui.press("8") 
    with pyautogui.hold("shift"):
        pyautogui.press("2")  
    with pyautogui.hold("shift"):
        pyautogui.press("7")
    pyautogui.press("b")
    pyautogui.press("i")
    pyautogui.press("n")
    #pyautogui.write(command2)
    with pyautogui.hold("shift"):
        pyautogui.press("7")
    #pyautogui.write(command3)
    pyautogui.press("b")
    pyautogui.press("a")
    pyautogui.press("s")
    pyautogui.press("h")
    with pyautogui.hold("shift"):
        pyautogui.press("2")
    with pyautogui.hold("shift"):
        pyautogui.press("9") 
    pyautogui.press("'")
    #pyautogui.write(command4)    
    
    pyautogui.press("enter")
    time.sleep(1)

    with pyautogui.hold("ctrl"):
        pyautogui.press("z")

    pyautogui.write("stty raw -echo")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write("fg")
    pyautogui.press("enter")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write("export TERM=xterm")
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.write(f"stty cols {columns} rows {lines}")
    pyautogui.press("enter")
    
    print("\nShell Successfully Stabilized!")
    exit()

dumb_to_smart()
