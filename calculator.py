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

class image:
	def __init__(self,filename,r,c,op,e_h=0):
		abg="dark blue"
		b="orange"
		self.height=40+e_h
		self.width=80+(e_h*2)
		self.filename=location+filename+".png"
		self.one=PhotoImage(file=self.filename)
		button=Button(image=self.one,bg=b,activebackground=abg,
					command=lambda: press(op),height=self.height,width=self.width).grid(row=r,column=c)

gui=Tk() 
gui.configure(background="orange") 
gui.title("Calculator") 
gui.geometry("430x255")
gui.wm_iconbitmap('images\\menu_icon.ico') 
equation = StringVar() 
expression_field = Entry(gui, textvariable=equation,font=('CityBlueprint','14')) 
expression_field.grid(columnspan=4, ipadx=70) 
equation.set(' ') 

one=image("one",3,0,1)
two=image("two",3,1,2)
three=image("three",3,2,3)
four=image("four",4,0,4)
five=image("five",4,1,5)
six=image("six",4,2,6)
seven=image("seven",5,0,7)
eight=image("eight",5,1,8)
nine=image("nine",5,2,9)
zero=image("zero",6,0,0)
	
plus=image("add",3,3,'+',e_h=10)
minus=image("minus",4,3,'-',e_h=10)
multiply=image('mult',5,3,'*',e_h=10)
divide=image('div',6,3,'/',e_h=10)
photo_eqto=PhotoImage(file="symbols\\eq_to.png")
equal = Button(gui, image=photo_eqto,bg="orange",activebackground="dark blue" ,
			command=equalpress,height=50,width=100) 
equal.grid(row=6, column=2) 
photo_clear=PhotoImage(file="symbols\\clear.png")
clear = Button(gui, image=photo_clear, 
			command=clear,height=50,width=100) 
clear.grid(row=6, column=1) 

gui.mainloop() 
