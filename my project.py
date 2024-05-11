import json
import os
import re
import winsound
import pygame
import tkinter as tk
from tkinter import font
from tkinter import simpledialog
from tkcode import CodeEditor
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import filedialog
from PIL import Image , ImageTk
from tkinter import *
from tkinter import messagebox
import subprocess
from datetime import datetime
import time
# colours #31363F(less dark), #222831(most dark) , #76ABAE(light blue) , #EEEEEE(off white)
# This error will produce a beep
time1 = datetime.now()

def play_applause():
    pygame.mixer.init()
    pygame.mixer.music.load("human_clapping_8_people.wav")  # Load the sound file
    pygame.mixer.music.play()

import tkinter.simpledialog as simpledialog
import winsound
import time
my_time1=20
my_time2=60
my_time3= 60
my_time4= 60
my_time5=60
my_time6=60
def taskbar():

    def play_sound():
        frequency = 440  
        duration = 1000 
        winsound.Beep(frequency, duration) 

    def app_header(window):
        label= Label(window, text= "YOU CODE" ,font= ("Georgia", 22),fg="white",bg="#222831", bd=5, relief= RAISED)
        label.place(x=550, y=5)
        label= Label(window,
                  text= 
"Empower your coding journey with our app, where every line you write brings your ideas to life" ,bd=5, relief= RAISED,font= ("Georgia", 17),fg="white",bg="#222831")
        label.place(x=150, y=50)

    def delete_input_lines(code):
        pattern = r".*input.*\n?"
        return re.sub(pattern, "", code)


    class CodeEditorApp:
      def __init__(self, window, q_text, file_name, code_terminal):
    
        
        self.window = window
        self.text= q_text
        self.code_editor= None
        self.file_name= file_name
        self.execute= False
        self.exists= True
        self.code_terminal= code_terminal
        self.timer_running= False


      def create_code_editor(self):
        self.code_editor = CodeEditor(
            self.window,
            width=94,
            height=12,
            language="python",
            background="black",
            highlighter="dracula",
            font="Consolas",
            autofocus=True,
            blockcursor=True,
            insertofftime=0
        )

        self.code_editor.pack()
        self.code_editor.bind("<KeyPress>", self.on_key_press)


        
        



      def create_question_label(self):
            ques= Label(self.window, text= self.text,font= ("Georgia", 15),fg="#EEEEEE",bg="#222831")
            ques.pack()
      def get_code_text(self):
        if self.code_editor:
            return self.code_editor.get("1.0", "end-1c")
        else:
            return "" 
          


      def terminal(self):
        if not self.execute:
              code= self.code_editor.get("1.0", "end-1c")
              print(code)
              pattern = r'(\w+)\s*=\s*(?:(int|float|list|tuple|set)\()?\s*input\("(.*)"\)'
              matches = re.findall(pattern, code)
              print(matches)
              for match in matches:
                    variable_name = match[0]   
                    input_prompt = match[2].strip('"')
                    print(match[0])
                    print(match[1])
                    modified_code= code
                    is_int_input = 'int'
                    is_float_input= 'float'
                    is_list_input= 'list'
                    is_tuple_input= 'tuple'
                    is_set_input= 'set'

                    if match[1]==is_int_input:
                         user_input = simpledialog.askinteger("Input", input_prompt)
                         code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                         print(type(user_input))
                    elif match[1]==is_float_input:
                         print('yes')
                         user_input = simpledialog.askfloat("Input", input_prompt)
                         code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                         print(type(user_input))
                    elif match[1]== is_list_input:
                          user_input_str = simpledialog.askstring("Input", input_prompt)
                          user_input = eval(user_input_str)
                          code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    elif match[1]== is_tuple_input:
                    
                          user_input_str = simpledialog.askstring("Input", input_prompt)
                          user_input = eval(user_input_str)
                          code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    elif match[1]== is_set_input:
                         user_input_str = simpledialog.askstring("Input", input_prompt)
                         user_input = set(user_input_str.split(","))
                         code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    else:
                          user_input = simpledialog.askstring("Input", input_prompt)
                          code = re.sub(rf'\b{variable_name}\b', f'"{user_input}"', modified_code)
        

              modified_code = delete_input_lines(code)
              with open("file.py", "w") as file:
                    file.write(modified_code)
              command = "python file.py"
              result = subprocess.run(command, shell=True, capture_output=True, text=True)
              self.code_terminal.delete("1.0", tk.END)
              if result.returncode == 0:
                  self.code_terminal.insert(tk.END, result.stdout)
              else:
                  self.code_terminal.insert(tk.END, result.stderr)
                  play_sound()
                  time.sleep(2)           
      def run_button(self):
            run_button= Button(self.code_editor,
                   text= "RUN",
                   bg= "#222831",
                   fg= "white",
                   command= self.terminal,
                   cursor='hand2')
            run_button.place(x=900,y=225)
      def on_key_press(self, event):
        
        if event.keysym == 'Return' and event.state & 0x1:
            self.terminal()


    def main():
        task_window= Tk()
        task_window.geometry("1200x700")
        task_window.title("YOUCODE... An app of innovation")
        notebook = ttk.Notebook(task_window)
        task_frame= Frame(task_window,bg= "#31363F",width= 1250, height= 600) 
        window1 = tk.Frame(notebook,bg="#76ABAE")
        window2 = tk.Frame(notebook,bg="#76ABAE")
        window3 = tk.Frame(notebook,bg="#76ABAE")
        window4 = tk.Frame(notebook,bg="#76ABAE")
        window5 = tk.Frame(notebook,bg="#76ABAE")
        window6 = tk.Frame(notebook,bg="#76ABAE")
        notebook.add(window1, text="Task1")
        notebook.add(window2, text="Task2")
        notebook.add(window3, text="Task3")
        notebook.add(window4, text="Task4") 
        notebook.add(window5, text="Task5") 
        notebook.add(window6, text="Task6") 
        notebook.pack(expand=True, fill="both")




        file1= "try1.json"
        timer1 = Label(window1, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer1.place(x=0,y=2)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 180) 
        terminal_subframe.place(x=100,y=440, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        task_frame= Frame(window1,bg= "#31363F",width= 1250, height= 600)
        task_frame.place(x=50,y=50, ) 
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 180) 
        terminal_subframe.place(x=100,y=440, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )


        code_editor1_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200)
        code_editor1_subframe.place(x=100,y=80, )
        code_editor_1 = CodeEditorApp(code_editor1_subframe, "Write a Python function to check if a number is prime or not.", file1,code_terminal)
        code_editor_1.create_question_label()
        code_editor_1.create_code_editor()
        # code_editor_1.submit_button() #it's something i changed
        def submit_code(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer1.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()

        def timer1_fun( button):
            global my_time1
            if my_time1 > 0:
                seconds = my_time1 % 60
                minutes = (my_time1 // 60) % 60
                hours = my_time1 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer1.config(text=timer_str)
                window1.after(1000, timer1_fun,button)
                my_time1 -= 1
            else:
                timer1.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")

              
        submit_button1 =Button(window1,
                        text= "Submit",
                        command= lambda: submit_code(submit_button1),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button1.place(x=1100,y=387)

        start_button1 = Button(window1,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer1_fun(submit_button1))
        start_button1.place(x= 1200,y=15 )
        
        code_editor_1.run_button()
      


# WINDOW 2
        task_frame= Frame(window2,bg= "#31363F",width= 1250, height= 600) #bd is adding border relief is type of the border
# frame.pack(side= BOTTOM)
        task_frame.place(x=50,y=50, )
        timer2 = Label(window2, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer2.place(x=0,y=2)
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 100) #bd is adding border relief is type of the border
# frame.pack(side= BOTTOM)
        terminal_subframe.place(x=100,y=440, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        code_editor2_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200) #bd is adding border relief is type of the border
# frame.pack(side= BOTTOM)
        code_editor2_subframe.place(x=100,y=80, )
        code_editor_2 = CodeEditorApp(code_editor2_subframe, " Write a Python function to find the factorial of a number", file1,code_terminal, )
        code_editor_2.create_question_label()
        code_editor_2.create_code_editor()
        # code_editor_1.submit_button()
        def submit_code2(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer2.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()
        def timer2_fun( button):
            global my_time2
            if my_time2 > 0:
                seconds = my_time2 % 60
                minutes = (my_time2 // 60) % 60
                hours = my_time2 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer2.config(text=timer_str)
                window2.after(1000, timer2_fun,button)
                my_time2 -= 1
            else:
                timer2.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")


        submit_button2 =Button(window2,
                        text= "Submit",
                        command= lambda: submit_code2(submit_button2),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button2.place(x=1100,y=387)
        start_button2 = Button(window2,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer2_fun(submit_button2))
        start_button2.place(x= 1200,y=15 )
        code_editor_2.run_button()
        code_editor2_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200)


        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, ) 

# WIDNOW3
        task_frame= Frame(window3,bg= "#31363F",width= 1250, height= 600) 
        task_frame.place(x=50,y=50, )
        timer3 = Label(window3, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer3.place(x=0,y=2)
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1180, height= 180)
        terminal_subframe.place(x=100,y=420, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        code_editor3_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200)
        code_editor3_subframe.place(x=100,y=80, )
        code_editor_3 = CodeEditorApp(code_editor3_subframe, " Write a Python program to find the sum of natural numbers up to n.", file1,code_terminal,)
        code_editor_3.create_question_label()
        code_editor_3.create_code_editor()
        # code_editor_1.submit_button()
        def submit_code3(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer3.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()
        def timer3_fun( button):
            global my_time3
            if my_time3 > 0:
                seconds = my_time3 % 60
                minutes = (my_time3 // 60) % 60
                hours = my_time3 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer3.config(text=timer_str)
                window3.after(1000, timer3_fun,button)
                my_time3 -= 1
            else:
                timer3.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")


        submit_button3 =Button(window3,
                        text= "Submit",
                        command= lambda: submit_code3(submit_button3),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button3.place(x=1100,y=387)

        start_button3 = Button(window3,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer3_fun(submit_button3))
        start_button3.place(x= 1200,y=15 )
        code_editor_3.run_button()

        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, ) 


   
# FOR WINDOW 4
        task_frame= Frame(window4,bg= "#31363F",width= 1250, height= 600)
        task_frame.place(x=50,y=50, )
        timer4 = Label(window4, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer4.place(x=0,y=2)
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1180, height= 180) 
        terminal_subframe.place(x=100,y=420, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        code_editor4_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200) 
        code_editor4_subframe.place(x=100,y=80, )
        code_editor_4 = CodeEditorApp(code_editor4_subframe, "Write a Python function to check if a string is a palindrome or not.", file1,code_terminal)
        code_editor_4.create_question_label()
        code_editor_4.create_code_editor()
        # code_editor_4.submit_button()
        def submit_code4(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer4.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()
        def timer4_fun( button):
            global my_time4
            if my_time4 > 0:
                seconds = my_time4 % 60
                minutes = (my_time4 // 60) % 60
                hours = my_time4 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer4.config(text=timer_str)
                window4.after(1000, timer4_fun,button)
                my_time4 -= 1
            else:
                timer4.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")


        submit_button4 =Button(window4,
                        text= "Submit",
                        command= lambda: submit_code4(submit_button4),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button4.place(x=1100,y=387)

        start_button4 = Button(window4,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer4_fun(submit_button4))
        start_button4.place(x= 1200,y=15 )
        code_editor_4.run_button()
        code_editor_4.run_button()
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, ) 

# FOR WINDOW 5
        task_frame= Frame(window5,bg= "#31363F",width= 1250, height= 600)
        task_frame.place(x=50,y=50, )
        timer5 = Label(window5, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer5.place(x=0,y=2)
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1180, height= 180) 
        terminal_subframe.place(x=100,y=420, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        code_editor5_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200) 
        code_editor5_subframe.place(x=100,y=80, )
        code_editor_5 = CodeEditorApp(code_editor5_subframe, "Write a Python function to find the Fibonacci series up to n terms.", file1,code_terminal,)
        code_editor_5.create_question_label()
        code_editor_5.create_code_editor()
        # code_editor_1.submit_button()
        def submit_code5(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer5.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()
        def timer5_fun( button):
            global my_time5
            if my_time5 > 0:
                seconds = my_time5 % 60
                minutes = (my_time5 // 60) % 60
                hours = my_time5 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer5.config(text=timer_str)
                window5.after(1000, timer5_fun,button)
                my_time5 -= 1
            else:
                timer5.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")


        submit_button5 =Button(window5,
                        text= "Submit",
                        command= lambda: submit_code5(submit_button5),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button5.place(x=1100,y=387)

        start_button5 = Button(window5,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer5_fun(submit_button5))
        start_button5.place(x= 1200,y=15 )
        code_editor_5.run_button()
        code_editor_5.run_button()
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, ) 






# FOR WINDOW6
        task_frame= Frame(window6,bg= "#31363F",width= 1250, height= 600)
        task_frame.place(x=50,y=50, )
        timer6 = Label(window6, text="", font=("Georgia", 22), fg="white", bg="#222831", bd=5, relief=tk.RAISED)
        timer6.place(x=0,y=2)
        app_header(task_frame)
        terminal_subframe=     Frame(task_frame,bg= "#31363F",width= 1180, height= 180)
        terminal_subframe.place(x=100,y=420, )
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, )
        code_editor6_subframe=     Frame(task_frame,bg= "#31363F",width= 1150, height= 200)
        code_editor6_subframe.place(x=100,y=80, )
        code_editor_6 = CodeEditorApp(code_editor6_subframe, " Write a Python program to count the number of vowels in a string", file1,code_terminal)
        code_editor_6.create_question_label()
        code_editor_6.create_code_editor()
        # code_editor_6.submit_button()
        def submit_code6(button):
            print("entry ho rai... check kro file")

            button.config(state=DISABLED)
            timer6.destroy()
            messagebox.showinfo("Congratulations","Congratulations.... You submitted your task in Time")
            play_applause()
        def timer6_fun( button):
            global my_time6
            if my_time6 > 0:
                seconds = my_time6 % 60
                minutes = (my_time6 // 60) % 60
                hours = my_time6 // 3600
                timer_str = f"{hours:02}:{minutes:02}:{seconds:02}"
                timer6.config(text=timer_str)
                window6.after(1000, timer6_fun,button)
                my_time6 -= 1
            else:
                timer6.config(text="Time's up")
                button.config(state="disabled")
                messagebox.showinfo("Time Alert","Time is up.You cannot submit the task after due time.")


        submit_button6 =Button(window6,
                        text= "Submit",
                        command= lambda: submit_code6(submit_button6),
                        font= ("Comic Sans", 12),
                        fg= "white",  
                        bg= "#222831",
                        activeforeground="white", 
                        activebackground="#222831",
                        state=ACTIVE, 
                        compound= 'left',
                        cursor="hand2")

        submit_button6.place(x=1100,y=387)

        start_button6 = Button(window6,
                              text="START",
                              font=("Comic Sans", 12),
                              fg="white",
                              bg="#222831",
                              activeforeground="white",
                              activebackground="#222831",
                              state=tk.ACTIVE,
                              compound='left',
                              cursor="hand2",
                              command=lambda: timer6_fun(submit_button6))
        start_button6.place(x= 1200,y=15 )
        code_editor_6.run_button()
        code_terminal= Text(terminal_subframe, height= 13, width= 130, bg= "#222831", fg= "white")
        code_terminal.pack(fill= BOTH, ) 
        task_window.mainloop()


    if __name__ == "__main__":
        main()

def error():
    frequency = 540  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("welcome voice.wav")  # Load the sound file
    pygame.mixer.music.play() 

def on_click(event1):
        if signin_entry1.get() == "Enter Username":
            signin_entry1.delete(0, "end")
            signin_entry1.config(fg='#31363F')
def on_click2(event2):
        if signin_entry2.get() == "Enter Password":
            signin_entry2.delete(0, "end")
            signin_entry2.config(fg='#31363F',show="*")

welcome_window = Tk()
welcome_window.geometry('1200x700')
welcome_window.title('Youcode')
welcome_window.config(background='#76ABAE')
bg_image = tk.PhotoImage(file="sign in.png")
style_main = ttk.Style()
style_main.theme_use('clam')
style_main.configure('TFrame',
                      borderwidth=5,
                      relief="raised",
                      bordercolor='black',
                      background='#31363F',
                      troughrelief='flat',
                      borderradius=32)
text_frame = ttk.Frame(welcome_window,
                   width=1080,
                   height=550)
text_frame.place(x=100,y=60)
frame1 = Frame(text_frame,bg="#31363F",width=700,height=300)
frame1.place(x=100,y=150)
label1 = Label(frame1,image=bg_image)
label1.pack()
welcome_label = Label(text_frame,
                      text="Welcome To YouCode",
                      fg="#EEEEEE",
                      font=("Roboto",29),
                      bg="#222831",
                      bd=2,
                      relief=RAISED,
                      padx=10,
                      pady=10)
welcome_label.place(x=74,y=50)

# hex value: #72cfc1
sign_inframe = Frame(text_frame,
                     bg="#EEEEEE",
                     padx=10,
                     pady=10,
                     width=350,
                     height=400)
sign_inframe.place(x=600,y=90)

signin_entry1 = Entry(sign_inframe,
                   font=('arial',20),
                   fg='grey',
                bg="white")
signin_entry1.insert(0,"Enter Username")
signin_entry1.bind("<FocusIn>", on_click)
signin_entry1.place(x=10,y=100)

signin_entry2 = Entry(sign_inframe,
                   font=('arial',20),
                   fg='grey',
                bg="white")
signin_entry2.insert(0, "Enter Password")
signin_entry2.bind("<FocusIn>", on_click2)
signin_entry2.place(x=10,y=170)
#ADD8E6
#87CEEB
#B0E0E6
symbol_font = font.Font(family="Roboto Condensed", size=24, weight="bold")
name = Label(sign_inframe,
             text="YOUCODE",
             font=symbol_font,
             fg="#87CEEB")
name.place(x=80,y=20)

import tkinter as tk
from PIL import Image , ImageTk
def sign_up():
    def on_entry_click(event):
        if entry1.get() == "Enter Username":
            entry1.delete(0, "end")
            entry1.config(fg='#222831')

    def on_entry_click2(event):
        if entry2.get() == "Enter Password":
            entry2.delete(0, "end")
            entry2.config(fg='#222831',show="*")

    def submit2():
        assert len(entry1.get()) != "",messagebox.showerror("Error","Username cannot be left blank.")
        assert len(entry1.get()) > 3,messagebox.showerror("Error","Invalid Username...Username must consist of more than 3 letters.")
        username = entry1.get()
        password = entry2.get()
        assert len(entry2.get()) != "",messagebox.showerror("Error","Password cannot be left blank.")
        assert len(entry2.get()) >= 5,messagebox.showwarning("Warning","A very weak password.Password must contain atleast 5 any characters")
        with open("code1.json","r") as file:
            prev = json.load(file)
        for i in range(len(prev)):
            if username == prev[i]["username"] and password == prev[i]["password"]:
                messagebox.showerror("Error","You already have an account on YouCode.")
                return
            if username == prev[i]["username"]:
                messagebox.showerror("Error","This username is already taken.")
                return
        if username != "" and password!="":
            submit_button.config(state=DISABLED,
                                 activebackground='grey',
                                 activeforeground='black')
            delete_button.config(state=DISABLED,
                                 activebackground='grey',
                                 activeforeground='black')
            backspace_butt.config(state=DISABLED,
                                 activebackground='grey',
                                 activeforeground='black')
            messagebox.showinfo("Welcome Aboard","You have successfully created an account on Youcode")
        elif username == "" or password == "":
            messagebox.showerror("Error","This is a required section.You cannot leave it blank.")
            error()
            return
 
        json_file_path = "code1.json"
        data_list = []
        try:
                if os.path.exists(json_file_path):
                    with open(json_file_path, 'r') as json_file:
                        data = json_file.read()
                        if data.strip():  # Check if the file is not empty
                            data_list = json.loads(data)
                new_data = {
                    "username": username,
                    "password": password,
                }
                data_list.append(new_data)

                with open(json_file_path, 'w') as new_file:
                    json.dump(data_list, new_file, indent=4)

        except json.JSONDecodeError:
                print(f"Error decoding JSON in {json_file_path}. Starting with a new list.")
                data_list = []
                new_data = {
                    "username": username,
                    "password": password,
                }
                data_list.append(new_data)
                with open(json_file_path, 'w') as json_file:
                    json.dump(data_list, json_file, indent=4)
                print(f"Data saved to {json_file_path}")
        except FileNotFoundError:
                print(f"JSON file '{json_file_path}' not found.")
        except PermissionError:
                print(f"Permission denied while accessing '{json_file_path}'.")

        signup_window.destroy()


        
    def delete():
            focused_box = signup_window.focus_get()
            if focused_box == entry1:
                entry1.delete(0,END)
            if focused_box == entry2:
                entry2.delete(0,END)
            return

    def backspace():
        focused_box = signup_window.focus_get()
        if focused_box == entry1:
            entry1.delete(len(entry1.get())-1,END)
        if focused_box == entry2:
            entry2.delete(len(entry2.get())-1,END)
        return

    welcome_window.lower()
    signup_window = tk.Toplevel(welcome_window)
    signup_window.geometry('1250x700')
    signup_window.title("Sign Up Window")
    signup_window.config(background="#76ABAE")
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TFrame', borderwidth=2, relief='raised',background='#31363F',bordercolor='black',borderradius=32)
    canvas = ttk.Frame(signup_window,
                   width=450,
                   height=500)
    canvas.place(x=320,y=300,anchor="center")
    pil_image = Image.open("new picture.png")
    image = ImageTk.PhotoImage(pil_image)
    person_label = Label(signup_window,
                      font=("Roboto",20),
                      image=image,
                      padx=20,
                      pady=20
                      )
    person_label.image = image
    person_label.place(x=800,y=170)
    
    # now we will add an entry box to the sign up window.
    entry1 = Entry(canvas,
                   font=('Roboto',19),
                   fg='grey',
                   bg="#EEEEEE")
    entry1.insert(0, "Enter Username")
    entry1.bind("<FocusIn>", on_entry_click)
    entry1.place(x=90,y=180)
    
    entry2 = Entry(canvas,
                   font=('Roboto',19),
                   fg='grey',
                   bg="#EEEEEE")
    entry2.insert(0,"Enter Password")
    entry2.bind("<FocusIn>", on_entry_click2)
    entry2.place(x=90,y=240)

    create_label = Label(canvas,
                         font=("roboto",24),
                         text="Create Your Account",
                            bg="#222831",
                            padx=10,
                            pady=10,
                            fg="#EEEEEE")
    create_label.place(x=60,y=40)
    create2_label = Label(signup_window,
                         font=("roboto",15),
                         text="Take only 60 seconds of your time with us !!!",
                            bg="#222831",
                            padx=10,
                            pady=10,
                            fg="#EEEEEE")
    create2_label.place(x=760,y=90)
    
    submit_button = Button(canvas,
                           text="Sign Up",
                           fg="#EEEEEE",
                           bg="#222831",
                           font=("roboto",17),
                           height=1,
                           width=20,
                           command=submit2)
    submit_button.place(x=90,y=330)
    delete_button = Button(canvas,
                       text="Delete",
                           fg="#EEEEEE",
                           bg="#222831",
                           width=10,
                           height=2,
                           command=delete)
    delete_button.place(x=100,y=400)
    backspace_butt = Button(canvas,
                           text="Backspace",
                           fg="#EEEEEE",
                           bg="#222831",
                           height=2,
                           width=10,
                           command=backspace)
    backspace_butt.place(x=266,y=400)


def submit():
        data_list = []
        enter = False
        username = signin_entry1.get()
        password = signin_entry2.get()
        with open("code1.json","r") as file:
            data = json.load(file)
        if not isinstance(data,list):
            data_list = [data]
        for user_data in data:
            if username== user_data["username"] and password == user_data["password"]:
                messagebox.showinfo("Welcome back!!","You have successfully signed in to your account.")
                play_alarm()
                enter = True
                sign_in_button.config(state=DISABLED)
                break

        if not enter:
            messagebox.showerror("Sign in error","You have failed to sign in either due to Unregistered user or Invalid input.")
            error()

        def delete_input_lines(code):
            pattern = r".*input.*\n?"
            return re.sub(pattern, "", code)
        
        def code_editor():
            import tkinter
            from tkinter import filedialog
            def Openfile():
                filepath = filedialog.askopenfilename(initialdir="D:\\Semester project\\file1.txt",
                                                      title="open file",
                                                      filetypes=(("text files","*.txt"),
                                                                 ("all files","*.*")))
                with open(filepath,'r') as file:
                    text = file.read()
                    code_editor1.delete("1.0",END)
                    code_editor1.insert("1.0",text)
            def submit():
                file= filedialog.asksaveasfile(initialdir="c:\\Users\\ATIF TRADERS\\PycharmProjects\\pythonProject2",
                                   defaultextension=".py",
                                   filetypes= [
                                       ("Text file", ".txt"),
                                       ("HTML",".html"),
                                       ("all files", ".*"),
                                       ("python file", ".py")
                                   ])
                if file:
                    content = code_editor1.get("1.0", "end-1c")  # Get all content
                    file.write(content + '\n')
                if file is None:
                    return #it will prevent error
# colours #31363F(less dark), #222831(most dark) , #76ABAE(light blue) , #EEEEEE(off white)
            root= tk.Toplevel()
            root.config(background='#76ABAE')
            root.title("YouCode: An app of innovation")
            
            app_header= tkinter.Label(root,
                          text= "YOU CODE: Code Editor",
                          bg="#222831",
                          fg="#EEEEEE",
                          bd=10,
                          relief=RAISED,
                          font= ("Georgia", 24))
            app_header.pack()
            ques= tkinter.Label(root,
                    text= "Edit any code, project or any task.",
                    font= ("Georgia", 24),
                    bd=10,
                    relief=RAISED,
                    fg="#EEEEEE",
                    bg="#222831")
            ques.pack()

            code_editor1 = CodeEditor(root,
                                     width=100,
                                     height=15,
                                     language="python",
                                     highlighter="dracula",
                                     font=("consolas"),
                                     background = "black",
                                     autofocus=True,
                                     blockcursor = True,
                                     insertofftime = 0,
                                     padx = 10,
                                     pady=10)
            code_editor1.pack(fill="both",expand = True)

            terminate_exec = Text(root,
                                  height=7,
                                  font=("consolas",19),
                                  bg="black",
                                  fg="white",
                                  width=99)
            terminate_exec.pack(side="bottom",fill="both")

            def terminal():
                        code= code_editor1.get("1.0", "end-1c")
                        print(code)
                        pattern = r'(\w+)\s*=\s*(?:(int|float|list|tuple|set)\()?\s*input\("(.*)"\)'
                        matches = re.findall(pattern, code)
                        print(matches)


                        for match in matches:
                                variable_name = match[0]   
                                input_prompt = match[2].strip('"')
                                print(match[0])
                                print(match[1])

                                modified_code= code
                                

                                is_int_input = 'int'
                                is_float_input= 'float'
                                is_list_input= 'list'
                                is_tuple_input= 'tuple'
                                is_set_input= 'set'

                                if match[1]==is_int_input:
                                    user_input = simpledialog.askinteger("Input", input_prompt)
                                    code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                                    print(type(user_input))
                                elif match[1]==is_float_input:
                                    print('yes')
                                    user_input = simpledialog.askfloat("Input", input_prompt)
                                    code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                                    print(type(user_input))
                                elif match[1]== is_list_input:
                                    user_input_str = simpledialog.askstring("Input", input_prompt)
                                    user_input = eval(user_input_str)
                                    code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                                elif match[1]== is_tuple_input:
                                
                                    user_input_str = simpledialog.askstring("Input", input_prompt)
                                    user_input = eval(user_input_str)
                                    code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                                elif match[1]== is_set_input:
                                    user_input_str = simpledialog.askstring("Input", input_prompt)
                                    user_input = set(user_input_str.split(","))
                                    code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                                else:
                                    user_input = simpledialog.askstring("Input", input_prompt)
                                    code = re.sub(rf'\b{variable_name}\b', f'"{user_input}"', modified_code)
                                
                        modified_code = delete_input_lines(code)
                        return modified_code

            def process_code():
                modified_code = terminal()
                with open("file.py", "w") as file:
                    file.write(modified_code)
                command = "python file.py"
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                terminate_exec.delete("1.0",END)
                if result.stdout:
                    terminate_exec.insert(END, result.stdout)
                if result.stderr:
                    terminate_exec.insert(END, result.stderr)
                    error()

            menu_bar2 = Menu(root)
            run_bar2 = Menu(menu_bar2,tearoff=0)
            file_bar2 = Menu(menu_bar2,tearoff=0)
            menu_bar2.add_cascade(label="Run",menu=run_bar2)
            menu_bar2.add_cascade(label="File",menu=file_bar2)
            file_bar2.add_command(label="Open File",command=Openfile)
            file_bar2.add_command(label="Save file",command=submit)
            run_bar2.add_command(label="Run code",command=process_code)
            root.config(menu=menu_bar2)
            root.mainloop()
        # This function stores the uploaded code into json file
        # colours #31363F(less dark), #222831(most dark) , #76ABAE(light blue) , #EEEEEE(off white)
        def code_upload():
            global time1
            timestr = str(time1)
            code = new_code.get("1.0",END)
            messagebox.showinfo("Update","Your code has been uploaded and saved successfully.")
            json_new_file_path = "code2.json"
            code_list = []
            if os.path.exists(json_new_file_path):
                with open(json_new_file_path,"r") as newfile:
                    code_list = json.load(newfile)
                    if not isinstance(code_list,list):
                        code_list = [code_list]
            code_data = {
                "username" : username,
                "code" : code,
                "date and time": timestr
            }
            code_list.append(code_data)
            with open(json_new_file_path,"w") as jsonfile2:
                json.dump(code_list,jsonfile2,indent=4)
            return
        def destroy():
            upload_label.destroy()
            new_code.destroy()
            code_list = []
            with open("code2.json","r") as codefile:
                data = json.load(codefile)
                for i in range(len(data)):
                    if data[i]["username"] == username:
                        extracted_data = data[i]["code"]
                        new_time = data[i]["date and time"]
                        code_list.append(new_time)
                        code_list.append(extracted_data)
                        continue
                    
                    else:
                        extracted_data = "You have not uploaded anything yet."
            print(code_list)
            saved_code = scrolledtext.ScrolledText(account_win,
                               height=15,
                               width=85,
                               bg="#222831",
                               font=("consolas",15),
                               fg="#EEEEEE",
                               padx=5,
                               pady=5,
                               bd=10,
                               relief=RAISED)
            saved_code.place(x=180,y=110)
            for code_parts in code_list:
                saved_code.insert(END,code_parts)
                # saved_code.insert(END,"This is the next uploaded code:")
                saved_code.insert(END,'\n')
            saved_code.delete("end-2l", "end")

            
    
        if enter == True:
            account_win = tk.Toplevel(welcome_window)
        account_win.geometry('1250x700')
        account_win.config(background="#76ABAE")
        account_win.title("User Account")
        pil_image2 = Image.open("profile.png")
        resized_image = pil_image2.resize((100,100))
        image2 = ImageTk.PhotoImage(resized_image)

        def select_image():
            image_file_path = filedialog.askopenfilename()
            if image_file_path:
                pic1 = Image.open(image_file_path)
                resize = pic1.resize((100,100))
                global pic
                pic = ImageTk.PhotoImage(resize)
                image_label.config(image=pic)
                messagebox.showinfo("Update","Profile picture has been updated!")
            else:
                messagebox.showerror("Error","Such a file does not exist!")
                error()
        # creating a button of selecting the profile picture.
        select_pic = Button(account_win,
                            fg="#EEEEEE",
                            bg="#222831",
                            text="Select Profile picture",
                            font=("robotos",10),
                            command=select_image)
        select_pic.place(x=1130,y=30)

        image_label = Label(account_win,
                            fg="#EEEEEE",
                            bg="#222831",
                            padx=10,
                            pady=10,
                            bd=10,
                            relief=RAISED,
                            image=image2)
        image_label.image = image2
        image_label.place(x=4,y=9)
        
        acc_name_label = Label(account_win,
                               text=f"{username}'s Account",
                               font=("robotos",12),
                               fg="#EEEEEE",
                               bg="#222831")
        acc_name_label.place(x=1130,y=5)
        # creating a label of homepage in account_window
        acc_label = Label(account_win,
                          text="Account Homepage",
                          font=("robotos",28),
                          bg="#222831",
                          fg="#EEEEEE",
                          padx=10,
                          pady=10,
                          bd=10,
                          relief=RAISED)
        acc_label.pack()

        def delete_input_lines2(code):
            pattern = r".*input.*\n?"
            return re.sub(pattern, "", code)

        def terminal2():
            code=new_code.get("1.0", "end-1c")
            print(code)
            pattern = r'(\w+)\s*=\s*(?:(int|float|list|tuple|set)\()?\s*input\("(.*)"\)'
            matches = re.findall(pattern, code)
            print(matches)
            for match in matches:
                    variable_name = match[0]   
                    input_prompt = match[2].strip('"')
                    print(match[0])
                    print(match[1])
                    modified_code= code
                    is_int_input = 'int'
                    is_float_input= 'float'
                    is_list_input= 'list'
                    is_tuple_input= 'tuple'
                    is_set_input= 'set'

                    if match[1]==is_int_input:
                        user_input = simpledialog.askinteger("Input", input_prompt)
                        if user_input is None:
                            return
                        code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                        print(type(user_input))
                    elif match[1]==is_float_input:
                        print('yes')
                        user_input = simpledialog.askfloat("Input", input_prompt)
                        if user_input is None:
                            return
                        code = re.sub(rf'\b{variable_name}\b', str(user_input), modified_code)
                        print(type(user_input))
                    elif match[1]== is_list_input:
                        user_input_str = simpledialog.askstring("Input", input_prompt)
                        user_input = eval(user_input_str)
                        code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    elif match[1]== is_tuple_input:
                                
                        user_input_str = simpledialog.askstring("Input", input_prompt)
                        user_input = eval(user_input_str)
                        code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    elif match[1]== is_set_input:
                        user_input_str = simpledialog.askstring("Input", input_prompt)
                        user_input = set(user_input_str.split(","))
                        code = re.sub(rf'\b{variable_name}\b', repr(user_input), code)
                    else:
                        user_input = simpledialog.askstring("Input", input_prompt)
                        code = re.sub(rf'\b{variable_name}\b', f'"{user_input}"', modified_code)
                                
            modified_code = delete_input_lines2(code)
            with open("file2.py", "w") as file:
                file.write(modified_code)
            command = "python file2.py"
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            code_terminal.delete("1.0",END)
            if result.stdout:
                code_terminal.insert(END, result.stdout)
            if result.stderr:
                code_terminal.insert(END, result.stderr)
                error()

        def Openfile2():
                filepath = filedialog.askopenfilename(initialdir="D:\\Semester project\\file1.txt",
                                                      title="open file",
                                                      filetypes=(("text files","*.txt"),
                                                                 ("all files","*.*")))
                with open(filepath,'r') as file:
                    text = file.read()
                    new_code.delete("1.0",END)
                    new_code.insert("1.0",text)
        def saveasfile():
                file= filedialog.asksaveasfile(initialdir="c:\\Users\\ATIF TRADERS\\PycharmProjects\\pythonProject2",
                                   defaultextension=".py",
                                   filetypes= [
                                       ("Text file", ".txt"),
                                       ("HTML",".html"),
                                       ("all files", ".*"),
                                       ("python file", ".py")
                                   ])
                if file:
                    content = new_code.get("1.0", "end-1c")  # Get all content
                    file.write(content + '\n')
                if file is None:
                    return

        # creating a menubar to hold button options:
        menu_bar = Menu(account_win)
        run_bar = Menu(menu_bar,tearoff=0)
        code_bar = Menu(menu_bar,tearoff=0)
        file_bar = Menu(menu_bar,tearoff=0)

        file_bar.add_command(label="Open File",command=Openfile2)
        file_bar.add_command(label="Save",command=saveasfile)
        file_bar.add_command(label="Exit",command=exit)
        menu_bar.add_cascade(label="File",menu=file_bar)
        code_bar.add_command(label="View uploaded code",command=destroy)
        menu_bar.add_cascade(label="Code",menu=code_bar)
        menu_bar.add_command(label="open code editor",command=code_editor)
        menu_bar.add_command(label="Open Task Window",command=taskbar)
        menu_bar.add_command(label="Upload code",command=code_upload)

        # we are adding the runbar to the menubar on top.
        run_bar.add_command(label="Run",command=terminal2)
        # this is the function to add the label run to runbar.
        menu_bar.add_cascade(label="Run",menu=run_bar)
        # it is to add a menu to a given menubar(a menu of run shows up in the run option of the menubar.)
        account_win.config(menu=menu_bar)
        # creating a label to place frame within.Reason for using the label was to be able to use place function,so we can place editor wherever we want.
        frame_label= Label(account_win)
        frame_label.place(x=1,y=130)

        # creating a text box for user to upload any random code or project.
        tab1 = ttk.Frame(frame_label)
        tab1.pack()
        new_code = CodeEditor(tab1,
                              language="python",
                              highlighter="dracula",
                              width=138,
                              height=18,
                              background = "black",
                              font=("consolas",12),
                              insertofftime = 0,
                              blockcursor = True,
                              autofocus=True,
                              padx=10,
                              pady=10)
        # we can't use pack and place within the same window.so we use place for both here.
        new_code.pack()
        account_win.update_idletasks()
        account_win.minsize(account_win.winfo_height(),account_win.winfo_width())

        code_terminal = Text(account_win,
                                 width=200,
                                 height=7,
                                 fg="#EEEEEE",
                                 bg="black",
                                 font=("consolas",15))
        code_terminal.pack(side=BOTTOM)
        code_terminal_label = Label(account_win,
                                    font=("arial",12),
                                    text="Terminal:",
                                    fg="white",
                                    bg="black")
        code_terminal_label.place(x=1,y=445)

        # we will now create a label for the upload text widget.
        upload_label = Label(account_win,
                             text="Enter any project or code snippets that you want to share on your account.",
                             fg="#EEEEEE",
                             bg="#222831",
                             font=("roboto",17))
        upload_label.place(x=270,y=100)
        
        account_win.mainloop()
        return
    
# Making the two buttons on the first interface.
sign_up_button = Button(sign_inframe,
                 text='Sign up',
                 bg='#EEEEEE',
                 fg='#31363F',
                 font=('Roboto',12),
                 width=10,
                 command=sign_up)
sign_up_button.place(x=100,y=350)
sign_in_button = Button(sign_inframe,
                  text='Log In',
                  fg='#EEEEEE',
                  bg='#222831',
                  font=('Roboto',17),
                  width=21,
                  height=1,
                  command=submit)
sign_in_button.place(x=20,y=250)

welcome_window.mainloop()