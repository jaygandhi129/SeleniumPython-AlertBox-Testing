import time
import threading
import tkinter
from tkinter import *
from tkinter.ttk import Progressbar

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common import alert
from selenium.webdriver.common.by import By


def update_progressbar(p):
    progress['value'] = p
    window.update_idletasks()


def start_test():
    global text_widget, window
    text_widget.insert(END, "Testing Started...\n")
    driver = webdriver.Chrome()
    text_widget.insert(END, "Chrome opened successfully.\n")
    update_progressbar(20)
    time.sleep(1)
    driver.maximize_window()
    text_widget.insert(END, "Window Maximized.\n")
    update_progressbar(30)
    time.sleep(1)
    driver.get("http://demo.automationtesting.in/Alerts.html")
    text_widget.insert(END, "URL Opened\n")
    update_progressbar(40)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, value="btn-danger").send_keys(Keys.ENTER)
    text_widget.insert(END, "Button pressed.\n")
    update_progressbar(50)
    time.sleep(2)
    text = driver.switch_to.alert.text
    text_widget.insert(END, f"Alert Box Says:{text}\n")
    update_progressbar(70)
    time.sleep(1)
    driver.switch_to.alert.accept()
    text_widget.insert(END, "Alert Accepted Successfully.\nClosing window...\n")
    update_progressbar(90)
    time.sleep(2)
    driver.close()
    text_widget.insert(END, "Window Closed.\nTest Successful! \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    update_progressbar(100)
    text_widget.config(state=DISABLED)


window = Tk()
window.title("Alert Box Handling")
window.geometry("500x400")
text_widget = Text(window, height=15, width=50)
text_widget.config(bg="black", fg="white", font=('PT Sans', 12, "normal"))
text_widget.pack(side=BOTTOM)
window.config(padx=80, pady=10)
button = Button(window, text="Start Test", bg="lightgreen", font=('Helvetica', 15, "bold"),
                command=threading.Thread(target=start_test).start)
button.place(x=120, y=20)
progress = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate')
progress.place(x=20, y=80)
window.mainloop()
