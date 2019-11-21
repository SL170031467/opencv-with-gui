import tkinter as tk

from tkinter import messagebox as msb

HEIGHT=500
WIDTH=500

root = tk.Tk()
root.title("face recognisation")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

def gh(name_of_user):
    import numpy as np
    import cv2
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi=img[y:y+h,x:x+h]
            cv2.putText(img,name_of_user,(x-1,y-1),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1,cv2.LINE_AA)
            cv2.imshow("ROI",roi)
        cv2.imshow('img',img)
    
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()    



def mod1():
    name_of_user=entry.get()
    gh(name_of_user)
      
background_image = tk.PhotoImage(file='insta.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#0000b3', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.12, anchor='n')

label=tk.Label(frame,text="enter your name:", bg='#e62e00')
label.grid(row=0,column=0)
entry = tk.Entry(frame, font=40,bd=7)
entry.grid(row=1,column=2)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

background_image1 = tk.PhotoImage(file='dheeraj.png')
background_label1 = tk.Label(lower_frame, image=background_image1)
background_label1.place(relwidth=1, relheight=1)

button = tk.Button(root, text="Check",activebackground="green",bd=7,font=40,command=mod1)
button.pack()

root.mainloop()



