from tkinter import *
import ast

root = Tk()
root['bg'] = 'black'
i=0

def get_num(num):
    global i
    result.insert(i,num)
    i+=1

def get_operator(operator):
    global i
    length = len(operator)
    result.insert(i,operator)
    i=i+length

def clear_all():
    result.delete(0,END)

def calculate():
    try:
        string = result.get()
        node = ast.parse(string,mode="eval")
        output = eval(compile(node,'<string>',"eval"))
        clear_all()
        result.insert(0,output)
    except Exception:
        clear_all()
        result.insert(0,"Error")

def convert_to_USD():
    string = int(result.get())
    output = string/83.4
    clear_all()
    result.insert(1, output)
    result.insert(0,"$")

def convert_to_INR():
    string = int(result.get())
    output = string*83.4
    clear_all()
    result.insert(0, output)
    length = len(str(output))
    result.insert(length,"/-")

frame = LabelFrame(root, text="Result",background="thistle2")
frame.grid(row=0,columnspan=10,padx=10,pady=10,sticky="ew")

result = Entry(frame,background="ivory2")
result.grid(row=0,columnspan=20,padx=10,pady=10)

numbers = [1,2,3,4,5,6,7,8,9]
count = 0
for x in range(3):
    for y in range(3):
        value = numbers[count]
        if value%2==0:
            button = Button(root,text=value,height=2,width=4,background="yellow2",command=lambda num = value: get_num(num))
        else:
            button = Button(root, text=value, height=2, width=4, background="RoyalBlue2",
                            command=lambda num=value: get_num(num))
        button.grid(row=x+1,column=y)
        count = count+1

operators = ["+","-","*","/"]
counter = 0
for x in range(4):
        if counter<len(operators):
            value = operators[counter]
            button = Button(root,text=value,height=2,width=4,background="coral", command=lambda operator = value: get_operator(operator))
            button.grid(row=x+1,column=3)
            counter+=1

button = Button(root,text="0",height=2,width=4,background="RoyalBlue2", command=lambda: get_num(0))
button.grid(row=4,column=1)

button = Button(root,text=".",height=2,width=4,background="SlateBlue2", command=lambda: get_num("."))
button.grid(row=1,column=4)

button = Button(root,text="AC",height=2,width=4,background="firebrick2",command=lambda: clear_all())
button.grid(row=4,column=0)

button = Button(root,text="=",height=2,width=4,background="green2",command=lambda: calculate())
button.grid(row=4,column=2)

button = Button(root,text="USD",height=2,width=4,background="violet", command=lambda num = value: convert_to_USD())
button.grid(row=2,column=4)

button = Button(root,text="INR",height=2,width=4,background="deep sky blue", command=lambda num = value: convert_to_INR())
button.grid(row=3,column=4)

frame = Frame(root,background="seashell2")
frame.grid(row=5,columnspan=20)
label = Label(frame,text="My Calculator",background="LightBlue3")
label.grid(row=0,column=0,padx=5,pady=5,sticky="ew")

root.mainloop()
