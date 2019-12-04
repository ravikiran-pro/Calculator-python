from tkinter import *
expression = "" 
location="symbols\\"
def press(num): 
	global expression 
	expression = expression + str(num) 
	equation.set(expression) 
def equalpress(): 
	try: 

		global expression 
		total = str(eval(expression)) 
		equation.set(total)  
		expression = total
	except: 
		equation.set(" error ")  
		expression=""
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

class Button1:
	def __init__(self,filename,row,column,op,e_h=0):
		self.op=op
		self.row=row
		self.column=column
		self.activebackground="dark blue"
		self.bg="orange"
		self.height=40+e_h
		self.width=80+(e_h*2)
		self.filename=location+filename+".png"
		self.one=PhotoImage(file=self.filename)
	def __button__(self):
		button=Button(image=self.one,bg=self.bg,activebackground=self.activebackground,command=lambda: press(self.op),
					height=self.height,width=self.width).grid(row=self.row,column=self.column)

gui=Tk() 
gui.configure(background="orange") 
gui.title("Calculator") 
gui.geometry("430x255")
gui.wm_iconbitmap('images\\menu_icon.ico') 
equation = StringVar() 
expression_field = Entry(gui, textvariable=equation,font=('CityBlueprint','14')) 
expression_field.grid(columnspan=4, ipadx=70) 
equation.set(' ') 

filename=["one","two","three","add","four","five","six","minus","seven","eight","nine","mult","zero","div"]
list_row=[3,3,3,3,4,4,4,4,5,5,5,5,6,6]
list_column=[0,1,2,3,0,1,2,3,0,1,2,3,0,3]
list_op=[1,2,3,'+',4,5,6,'-',7,8,9,'*',0,'/']
list_eh=[0,0,0,10,0,0,0,10,0,0,0,10,0,10]

for i in range(len(filename)):
	one=Button1(filename[i],list_row[i],list_column[i],list_op[i],list_eh[i])
	one.__button__()

photo_clear=PhotoImage(file="symbols\\clear.png")
clear = Button(gui, image=photo_clear, 
			command=clear,height=50,width=100) .grid(row=6, column=1) 


photo_eqto=PhotoImage(file="symbols\\eq_to.png")
equal = Button(gui, image=photo_eqto,bg="orange",activebackground="dark blue" ,
			command=equalpress,height=50,width=100) .grid(row=6, column=2) 

gui.mainloop() 
