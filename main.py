from tkinter import *
#addition
def add():
    N1=int(entern1.get())
    N2=int(entern2.get())
    R=N1+N2
    result.insert(0,R)

def mince():
    N1 = int(entern1.get())
    N2 = int(entern2.get())
    R = N1 - N2
    result.insert(0, R)

def mul():
    N1 = int(entern1.get())
    N2 = int(entern2.get())
    R = N1 * N2
    result.insert(0, R)

def div():
    N1 = int(entern1.get())
    N2 = int(entern2.get())
    R = N1 / N2
    result.insert(0, R)

def init():
    entern2.delete(0,END)
    entern1.delete(0,END)
    result.delete(0,END)
def close():
    window.destroy()



#creer une fenetre
window=Tk()

window.title("calculatrice")
window.geometry("500x500")
window.iconbitmap("cal.ico")
window.config(background='#F7F4FF')

label_title=Label(window, text="Calculatrice", font=("Times New Roman",50,"italic"), bg='#F7F4FF', fg='#FF004F')
label_title.pack()

#frame=Frame(window, bg="white" )
n1=Label(window, text="N1:", font=("Courrier",20,"bold") , bg="#F7F4FF" , fg="#4800F3")
n1.place(x=50 , y=200)

n2=Label(window, text="N2:", font=('Courrier',20,"bold"), bg="#F7F4FF", fg="#4800F3")
n2.place(x=50 , y=250)


#champs de saisie de n1
entern1=Entry(window,bg="#DED1FF")
entern1.place(x=200,y=210)
#champs de saisie de n2
entern2=Entry(window,bg="#DED1FF")
entern2.place(x=200, y=260)



button1=Button(window, text="Initialiser", font=("Courrier",10,"italic"), bg="#DED1FF", fg='black', command=init)
#button1.pack(pady=10, fill=X)
button1.place(x=400,y=205)
button2=Button(window,text="Fermer",font=("Courrier",10,"italic"),bg="#DED1FF",fg="black", command=close)
button2.place(x=400,y=255)

#boutton des operations
buttonplus=Button(window,text="+",font=("Courrier",15,"bold"),bg="#DED1FF",fg="black", command=add)
buttonplus.place(x=80,y=340)
#
buttonplus=Button(window,text="-",font=("Courrier",15,"bold"),bg="#DED1FF",fg="black",command=mince)
buttonplus.place(x=150,y=340)
#
buttonplus=Button(window,text="*",font=("Courrier",15,"bold"),bg="#DED1FF",fg="black",command=mul)
buttonplus.place(x=220,y=340)
#
buttonplus=Button(window,text="/",font=("Courrier",15,"bold"),bg="#DED1FF",fg="black", command=div)
buttonplus.place(x=290,y=340)
#Afficher le resultat
result=Entry(window,bg="#DED1FF")
result.place(x=200,y=410)
label_result=Label(window, text="Résultat:", font=("Courrier",20,"bold"), bg="#F7F4FF", fg='#4800F3')
label_result.place(x=50,y=400)





#afficher
window.mainloop()
