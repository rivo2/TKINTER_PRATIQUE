from tkinter import*
import math

# def age():


#premiere fenetre
main=Tk()

#creer une frame(boite)
frame=Frame(main,bg="#41B77F")
frame2=Frame(main,bg="white")

main.title("Mon Application")
main.geometry("700x40")#.....taille de la fenetre
main.minsize(400,360)#........taille minimale
main.maxsize(800,600)#........taille maximale
# main.resizable(width=False,height=True)...atao egale true ilay parametre raha toa ka avela azo kitiana ny dimension...izay manandrify azy
# main.sizefrom("user")
# main.iconbitmap("couleur.jpeg")
main.config(background='#41B77F')
label_title=Label(frame,text="Bienvenue ",font=("Courrier",40),bg="#41B77F",fg="white")
label_subtitle=Label(frame,text="Bonjour tout le monde ",font=("Courrier",30),bg="#41B77F",fg="white")
bouton=Button(frame,text="SUBMIT",font=("Courrier",20),bg="white",fg="#41B77F")
age =Entry(frame,font=("Courrier",25))

label_title.pack()#etendre=lui donner toute la
frame.pack(expand=YES)
label_subtitle.pack()
age.pack()
bouton.pack(pady=20,fill=X)
frame2.pack(expand=YES)

main.tk.mainloop()