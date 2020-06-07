from tkinter import *
from googletrans import Translator
from tkinter.messagebox import showinfo

#create tkinter object to hold GUI
window=Tk()
window.title('Translator')
window.geometry('200x100')

#create a translator object
translator=Translator()

#method to translate
def dotranslation():
	word=entry.get()
	result=translator.translate(word).text
	showinfo('Translator',result)

#create a label
label1=Label(window,text='Enter your string: ')
label1.grid(row=0,column=0)

#create a textbox where user will input the string
entry=Entry(window)
entry.grid(row=1,column=0)

#create a button 
button=Button(window,text='Translate',command=dotranslation)
button.grid(row=2,column=0)

#show the window
window.mainloop()