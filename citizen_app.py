
import smtplib, re
from tkinter import *
import tkinter as tk
from tkinter import BitmapImage, Button, Canvas, Entry, Frame, Image, Label, PhotoImage, Place, mainloop, ttk
from tkinter import messagebox
import tkinter
import PIL
from PIL import ImageTk
from PIL import Image


#Defining Canvas and Frame
def canvas_and_frame():
	global frame 
	global canvas

	canvas = tk.Canvas(root,height=720,width=1280,bg="#90EE90")
	canvas.pack()
	main_heading=Label(canvas,text="CITIZEN GRIEVANCE",font=('Playfair Display',45,'bold'),bg='#90EE90',fg='#FF8C00').place(x=325,y=0)

	############# LOGO ###########

	image1=Image.open("/home/kali/Downloads/logo-g.png")
	image1=image1.resize((100,100),Image.LANCZOS)
	photo=ImageTk.PhotoImage(image1)
	label3=tkinter.Label(image=photo)
	label3.image=photo
	label3.place(x=125,y=10)

	############# LOGO ###########

	#creating frame
	frame = tk.Frame(canvas,bg='white')
	frame.place(x=250,y=175,height=450,width=800)

############################ SECTION-1 ###########################

########################### LOGIN PAGE ##########################

#CHECK VALID EMAIL
def check_email(email, password):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	
	try:
		if server.login(email,password):
			return True
	
	except smtplib.SMTPAuthenticationError:
		return False
			
def clear_frame():
	for widgets in frame.winfo_children():
   		widgets.destroy()

#CHANGE
def onclick_Login():

	if email.get() and password.get() and check_email(email.get(),password.get()):
		clear_frame()
		return problem_statement()

	return messagebox.showerror("error","Login fail!!!")


def login_page():
	global email
	global password

	mylabel1 = Label(frame,text="Login",font=('Segoi Ui',30,'bold'),bg='white',fg="green").place(x=360,y=25)
	
	#entry email 
	l_email = Label(frame,text="Gmail Id",font=('Segoi Ui',16,),bg='white',fg='#FF8C00').place(x=310,y=100) 	#LABLE
	email = StringVar()
	e_email = Entry(frame, textvariable=email,font=('Segoi Ui',15)).place(x=310,y=145)		#ENTRY

	#entry pass
	l_pass = Label(frame, text=" Password",font=('Segoi Ui',16,),bg='white',fg='#FF8C00').place(x=310,y=180)		#LABLE
	password = StringVar()
	e_pass=Entry(frame, textvariable=password,borderwidth=1,show = "*",font=('Segoi Ui',15)).place(x=310,y=220)				#ENTRY
	button = Button( frame , text = "Login", command =lambda : onclick_Login(),relief='raised',font=('Segoi Ui',16,),bd=0,bg='#FF8C00',fg='white').place(x=390,y=300)

############################################################# END OF FIRST SECTION #################################

############################################################# SECTION 2 ########################################	

def check_num_name():
	try:
		if len(name.get())<3:
			messagebox.showerror("error", "Enter correct name")
		elif not int(number.get()) or len(number.get()) != 10:
			messagebox.showerror("error", "re-enter your mobile_no previous was incorrect")
			return False
		else:
			return True

	except ValueError:
		messagebox.showerror("error", "re-enter your mobile_no previous was incorrect")

def st_prob():
	# Adding Subject and content of mail
	global mail_sub_st
	subject = ""
	count = 0

	# verifing check box are selected or not 
	# if they are adding them to subject of email
	for op in option_list:
		count+=options[op].get()
		if options[op].get():
			subject+=op+"\n"
	if count==0:
		messagebox.showerror("error", "please select your problem")

	# checking if in optios others is selected then statement is there or not
	elif options["Can't find your issue? Please Mention Below:"].get() and len(statement.get(1.0,"end-1c"))<1:
		messagebox.showerror("Statement_error", "you have selected others please discribe your issue")
		return False
	dash = "\n"+"-"*50
	mail_sub_st = """\nProblems:\n%s%s\n\nProblem Discription:\n%s%s\n\n%s\n%s\nAddress:"""\
	%(subject, dash, statement.get(1.0,"end-1c"), dash , name.get(), str(number.get()))
	return True

def onclick_proceed():
	if check_num_name() and st_prob():
		clear_frame()
		return add_location()
	return

# def scroll():
	#global new_frame

	#wrapper = tk.Frame(frame)
	#canvas2 = Canvas(wrapper)
	#canvas2.pack(side=LEFT)
	#yscrollbar = ttk.Scrollbar(wrapper, orient = "vertical" , command=canvas2.yview)
	#yscrollbar.pack(side=RIGHT, fill="y")
	#wrapper.pack()
	
def problem_statement():
	global name
	global number
	global statement 
	global options
	global option_list

	option_list = ["Improper Collection of Waste"\
	,"Blocked Drainage System","Garbage Collector Did Not Come"\
	,"Dumpster is Damaged","Can't find your issue? Please Mention Below:"]
	options = {}
	for op in option_list:
		options[op] = IntVar()

	# attach Scrollbar to root window on
    # the side
	
	#add
	# scroll()
	mylabel1 = Label(frame, text="Welcome to Citizen Grievance",font=('Segoi Ui',16,'bold'),bg='white',fg="green") #LABEL
	mylabel2 = Label(frame, text="Please Choose/Mention your Problem",font=('Segoi Ui',16,'bold'),bg='white',fg="green") #LABEL
	mylabel1.pack()
	mylabel2.pack()

	#ENTER NAME
	l_name = Label(frame, text="NAME: ",font=('Segoi Ui',14,),bg='white',fg='#FF8C00').place(x=80,y=80) #LABEL
	name = StringVar()
	e_name = Entry(frame, textvariable=name,borderwidth= 2,width=30).place(x=180,y=85) #ENTRY
	#l_name.pack()
	#e_name.pack()

	#ENTER NUMBER
	l_number = Label(frame, text="CONTACT: ",font=('Segoi Ui',14,),bg='white',fg='#FF8C00').place(x=400,y=80) #LABEL
	number = StringVar()
	e_number = Entry(frame, textvariable=number,borderwidth= 2,width=30).place(x=535,y=85) #ENTRY
	#l_number.pack()
	#e_number.pack()

	pls_choose=Label(frame,text="Please Choose From Below:",font=('Segoi Ui',14,),bg='white',fg='green').place(x=80,y=130)

	#CheckBoxes

	op1 = Checkbutton(frame,text="Improper Collection of Waste",variable = options[option_list[0]],onvalue=1,offvalue=0,font=('Segoi Ui',12,),bg='white',fg='#FF8C00').place(x=80,y=160)
	op2 = Checkbutton(frame,text="Blocked Drainage System",variable = options[option_list[1]],onvalue=1,offvalue=0,font=('Segoi Ui',12,),bg='white',fg='#FF8C00').place(x=80,y=190)
	op3 = Checkbutton(frame,text="Can't find your issue? Please Mention Below:",variable = options[option_list[2]],onvalue=1,offvalue=0,font=('Segoi Ui',12,),bg='white',fg='#FF8C00').place(x=80,y=220)
	op4 = Checkbutton(frame,text="Garbage Collector Did Not Come",variable = options[option_list[3]],onvalue=1,offvalue=0,font=('Segoi Ui',12,),bg='white',fg='#FF8C00').place(x=420,y=160)
	op5 = Checkbutton(frame,text="Dumpster is Damaged",variable = options[option_list[4]],onvalue=1,offvalue=0,font=('Segoi Ui',12,),bg='white',fg='#FF8C00').place(x=420,y=190)

	#txt_box=Text(frame,height=6,width=70,bd=2,font=('Segoi Ui',12,)).place(x=80,y=265)

	# ENTER STATEMENT
	st_frame = Frame(frame)
	st_frame.place(x=80,y=265)
	scroll = Scrollbar(st_frame)
	scroll.pack(side=RIGHT, fill=Y)
	# statement = Text(st_frame, height=3, width=30, wrap=NONE, yscrollcommand=scroll.set)
	statement = Text(st_frame, height=6, width=78, wrap=NONE, yscrollcommand=scroll.set) #ENTRY
	statement.pack()
	scroll.config(command=statement.yview)

	#button
	button1 = Button( frame , text = "Proceed", command=lambda: onclick_proceed(),relief='raised',font=('Segoi Ui',16,),bd=0,bg='#FF8C00',fg='white').place(x=350,y=395)

############################################################# END OF SECTION 2 ####################################

######################### Add_Location and POC ###########################
# proof of concept
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from tkinter import filedialog

from PIL import ImageTk, Image 
import exifread
from datetime import datetime

def poc():
	if len(imagelist)>=1:
		return True
	else:
		messagebox.showerror("upload photo","please upload proof of concept")
		return False

def upload_image():
	if len(imagelist)<3:	
		
		photo_frame.filename = filedialog.askopenfilename(title = "select an image", filetypes=(("png files", "*.png"),("all files", "*.*")))
		try:
			with open(str(photo_frame.filename), 'rb') as fh:
			    tags = exifread.process_file(fh, stop_tag="EXIF DateTimeOriginal")
			    dateTaken = tags["EXIF DateTimeOriginal"]
			    print(dateTaken) 
		except KeyError:
			dateTaken = str(datetime.now()).split()

		imagelist[photo_frame.filename]= "date : " +dateTaken[0]+"\t time : " +dateTaken[1]

		for widgets in photo_frame.winfo_children():
	   		widgets.destroy()
		i=1	
		for image_p, t_s in imagelist.items():
			path = Label(photo_frame, text = image_p)
			path.grid(row=i)
			button = Button( photo_frame , text = "delete_image", command=lambda: del_img(image_p),relief='raised',font=('Segoi Ui',16,),bd=0,bg='#FF8C00',fg='white')
			button.grid(row=i ,column =2 )
			i+=1
	else:
		return messagebox.showerror("upload error","Can't upload_image\n more than 3")

def del_img(image_p):
	del imagelist[image_p]

	for widgets in photo_frame.winfo_children():
   		widgets.destroy()
	i=1	
	
	for image_p, t_s in imagelist.items():
		path = Label(photo_frame, text = image_p)
		path.grid(row=i)
		button = Button( photo_frame , text = "delete_image", command=lambda: del_img(image_p),relief='raised',font=('Segoi Ui',16,),bd=0,bg='#FF8C00',fg='white')
		button.grid(row=i,column= 2)
		i+=1	
	return

def open_img():
	top = Toplevel()

	topcanvas = Canvas(top,width = 400,height = 400)
	topcanvas.pack()
	img = tkinter.PhotoImage(file="/home/kali/Downloads/project/environment-earth-day-hands-trees-growing-seedlings-bokeh-green-background-female-hand-holding-tree-nature-field-gra-130247647.jpg")
	topcanvas.create_image(0,0,image =img,anchor=NW)
	topcanvas.image =img

	close_btn = Button(top, text = "close_image" ,command=top.destroy).pack()
	d_img = Button(top, text = "delete_image",command= lambda :del_img(image_p)).pack()	


def location(address_op):
	for ad in address_ls:
		if len(address_op[ad].get())<2:
			messagebox.showerror("fill address", "please fill the "+ad)
			return False 
	return True

def send_mail(address_op):

	content = mail_sub_st
	ad = ""
	for key, val in address_op.items():
		ad += "\n"+key +": "+str(address_op[key].get())
	content +=ad

	img_data = {}
	ts = ""
	i=0
	for ImgFileName , st  in imagelist.items(): 
		i+=1
		with open(ImgFileName, 'rb') as f:
		    img_data[ImgFileName]=f.read()
		    ts+="\n"+ImgFileName.split('/')[-1]+str(i)+":: "+st

	content+="\n\nTime Stamp:"+ts
	msg = MIMEMultipart()
	msg['Subject'] = 'CITIZEN GRIEVANCE'
	msg['From'] = email.get()
	msg['To'] = "srivastavanuj21@gmail.com"

	text = MIMEText(content)
	msg.attach(text)
	for i_p, i_d in img_data.items():
		image = MIMEImage(i_d, name=os.path.basename(i_p))
		msg.attach(image)

	s = smtplib.SMTP("smtp.gmail.com", 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(msg['From'],password.get() )
	s.sendmail(msg['From'],msg['To'] , msg.as_string())
	s.quit()


def onclick_submit(address_op):
	if poc() and location(address_op):
		send_mail(address_op)
		clear_frame()

		return response()
	else:
		return 

def add_location():
	global photo_frame
	global imagelist
	global address_ls
	imagelist = {}

	mylabel1 = Label(frame, text="LOCATION & PROOF OF CONCEPT",font=('Segoi Ui',16,'bold'),bg='white',fg="green") #LABEL
	mylabel1.pack()

	mylabel2 = Label(frame,text="Location Details:",font=('Segoi Ui',14,),bg='white',fg='green')
	mylabel2.place(x=80,y=80)

	#this is for preview type like which file is uploaded
	photo_frame = Frame(frame)
	photo_frame.pack()

	# button = Button( frame , text = "ADD_POC", command=lambda: live_campture_image())
	# button.pack()

	upload_button = Button( frame , text = "Upload Image", command=lambda: upload_image())
	upload_button.place(x=575,y=280)
	

	address_ls = ["Problem_Location","Area/Colony","Landmark","Town/City","State"]
	address_op = {}
	for add_details in address_ls:
		address_op[add_details] = StringVar()
	
	x=80
	i=0
	for ls in address_ls:
		loc_label = Label(frame,text=ls,font=('Segoi Ui',12,),bg='white',fg='#FF8C00')
		loc_label.place(x=x,y=x+40+(40*i))
		loc_entry = Entry(frame,textvariable=address_op[ls],borderwidth=2,width=30)
		loc_entry.place(x=x*3+20,y=x+40+(40*i))
		if ls == "Town/City":
			loc_entry.insert(0,"Bokaro")
		elif ls == "State":
			loc_entry.insert(0,"Jharkhand")
		i+=1

	
	button = Button( frame , text = "Submit", command=lambda: onclick_submit(address_op),relief='raised',font=('Segoi Ui',16,),bd=0,bg='#FF8C00',fg='white')
	button.place(x=370,y=395)

##################################################################

def response():
	mylabel1 = Label(frame, text="Response is recorded!!!\n We will try to resolve it soon \n check your email for complaint no.",font=('Segoi Ui',16,'bold'),bg='white',fg="green") #LABEL
	mylabel1.place(x=250,y=175)



root= tk.Tk()
root.geometry("1280x720") 
root.title("CITIZEN GRIEVANCE")
#root.iconbitmap('logo-icon.png')
root.resizable(width=FALSE,height=FALSE)
#creating canvas and frame
canvas_and_frame()
login_page()
root.mainloop()
