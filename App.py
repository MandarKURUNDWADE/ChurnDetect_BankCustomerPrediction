from tkinter import *
import joblib

def show_entry_fields():
    p1=int(e1.get())
    p2=int(e2.get())
    p3=int(e3.get())
    p4=float(e4.get())
    p5=int(e5.get())
    p6=int(e6.get())
    p7=int(e7.get())
    p8=float(e8.get())
    p9=int(e9.get())
    
    p10=0
    p11=sel()
    
    model = joblib.load('churn_predict_model')
    # result = model.predict([[619, 42, 2, 0.0, 0, 0, 0, 101348.88, 0, 0, 0]])
    result = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11]])

    if result == 0:
        Label(master, text="No Exit",bg='#333333',fg="#ffffff",font=("Arial", 13)).grid(row=14)
    else:
        Label(master, text="Exit",bg='#333333',fg="#ffffff",font=("Arial", 13)).grid(row=14)

master = Tk()
master.title("KMandar...😃")
master.geometry('420x500')
master.configure(bg='#333333')

# label = Label(master, text = "Customers Churn Prediction Using ML"
#                           , bg = "black", fg = "white"). \
#                                grid(row=0,columnspan=2)

label = Label(master, text = "Bank Customers Churn Prediction Using ML", 
              bg='#333333',fg="#FF3399",font=("Arial", 16)). \
                               grid(row=0,columnspan=3, pady=10)
                               
Label(master, text="CreditScore:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=1, sticky="e")
Label(master, text="Age:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=2, sticky="e")
Label(master, text="Tenure:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=3, sticky="e")
Label(master, text="Balance:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=4, sticky="e")
Label(master, text="Num Of Products:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=5, sticky="e")
Label(master, text="HasCrCard:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=6, sticky="e")
Label(master, text="Is Active Member:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=7, sticky="e")
Label(master, text="Estimated Salary:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=8, sticky="e")
Label(master, text="Geography:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=9, sticky="e")
Label(master,text="Gender:",bg='#333333',fg="#ffffff",font=("Arial", 10)).grid(row=10, sticky="e")

def sel():
   selection = int(var.get())
   Label(master, text="Gender: " + str(var.get())).grid(row=14)
   return selection
   
var = IntVar()
Radiobutton(master, text="Male    ",bg='#333333',fg="#ffffff",font=("Arial", 10), variable=var, value=0,command=sel).grid(row=10, column=1)
Radiobutton(master, text="Female",bg='#333333',fg="#ffffff",font=("Arial", 10), variable=var, value=1,command=sel).grid(row=11, column=1)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
e7 = Entry(master)
e8 = Entry(master)
e9 = Entry(master)
# e10 = Entry(master)

e1.grid(row=0, column=0, pady=5)
e1.grid(row=1, column=1, pady=5)
e2.grid(row=2, column=1, pady=5)
e3.grid(row=3, column=1, pady=5)
e4.grid(row=4, column=1, pady=5)
e5.grid(row=5, column=1, pady=5)
e6.grid(row=6, column=1, pady=5)
e7.grid(row=7, column=1, pady=5)
e8.grid(row=8, column=1, pady=5)
e9.grid(row=9, column=1, pady=5)
# e10.grid(row=10,column=1, pady=5)


Button(master, text='Predict', font=("Arial", 10), 
       bg='green', fg='white', command=show_entry_fields).grid(row=13, column=1, columnspan=1, pady=10, sticky='e')


mainloop()