from tkinter import *
from tkinter.messagebox import showinfo
from pyshorteners import *

 #create tkinter object to hold GUI
window=Tk()
window.title('URL shortener')
window.geometry('400x400')

#method to shortener
def short():
	url=entry.get()
	shortened_url=Shortener()
	showinfo('Shortened URL',f"{shortened_url.tinyurl.short(url)}")
#create a label
label1=Label(window,text='Enter your URL: ')
label1.grid(row=0,column=0)

#create a textbox where user will input the string
entry=Entry(window,width=30,bg='#69BEF6',bd=2)
entry.grid(row=0,column=1,padx=5,pady=5)


#create a button 
button=Button(window,text='Short',command=short)
button.grid(row=1,column=0,columnspan=2)

#show the window
window.mainloop()
