from tkinter import *

# Highlight Win
def H():
    if btn1['text']==btn4['text']==btn7['text']=='X' or btn1['text']==btn4['text']==btn7['text']=='O':
        btn1['bg']='tomato'
        btn4['bg']='tomato'
        btn7['bg']='tomato'
    if btn2['text']==btn5['text']==btn8['text']=='X' or btn2['text']==btn5['text']==btn8['text']=='O':
        btn2['bg']='tomato'
        btn5['bg']='tomato'
        btn8['bg']='tomato'
    if btn3['text']==btn6['text']==btn9['text']=='X' or btn3['text']==btn6['text']==btn9['text']=='O':
        btn3['bg']='tomato'
        btn6['bg']='tomato'
        btn9['bg']='tomato'
    if btn1['text']==btn2['text']==btn3['text']=='X' or btn1['text']==btn2['text']==btn3['text']=='O':
        btn1['bg']='tomato'
        btn2['bg']='tomato'
        btn3['bg']='tomato'
    if btn4['text']==btn5['text']==btn6['text']=='X' or btn4['text']==btn5['text']==btn6['text']=='O':
        btn4['bg']='tomato'
        btn5['bg']='tomato'
        btn6['bg']='tomato'
    if btn7['text']==btn8['text']==btn9['text']=='X' or btn7['text']==btn8['text']==btn9['text']=='O':
        btn7['bg']='tomato'
        btn8['bg']='tomato'
        btn9['bg']='tomato'
    if btn1['text']==btn5['text']==btn9['text']=='X' or btn1['text']==btn5['text']==btn9['text']=='O':
        btn1['bg']='tomato'
        btn5['bg']='tomato'
        btn9['bg']='tomato'
    if btn3['text']==btn5['text']==btn7['text']=='X' or btn3['text']==btn5['text']==btn7['text']=='O':
        btn3['bg']='tomato'
        btn5['bg']='tomato'
        btn7['bg']='tomato'
        
# Select Win wiith X
# Win X
def winxsx():
    global c, a, c3, flag, l1, l2
    f = 0
    if (btn1['text']==btn4['text']==btn7['text']=='X' or btn2['text']==btn5['text']==btn8['text']=='X' or btn3['text']==btn6['text']==btn9['text']=='X' or btn1['text']==btn2['text']==btn3['text']=='X' or btn4['text']==btn5['text']==btn6['text']=='X' or btn7['text']==btn8['text']==btn9['text']=='X' or btn1['text']==btn5['text']==btn9['text']=='X' or btn3['text']==btn5['text']==btn7['text']=='X'):
        a=Tk()
        bw=Button(a,text='{} WINS'.format(namep1),padx=10,pady=5,bd=5)
        bw.pack()
        c=10
        H()
        f = 1
    elif (btn1['text']==btn4['text']==btn7['text']=='O' or btn2['text']==btn5['text']==btn8['text']=='O' or btn3['text']==btn6['text']==btn9['text']=='O' or btn1['text']==btn2['text']==btn3['text']=='O' or btn4['text']==btn5['text']==btn6['text']=='O' or btn7['text']==btn8['text']==btn9['text']=='O' or btn1['text']==btn5['text']==btn9['text']=='O' or btn3['text']==btn5['text']==btn7['text']=='O'):
        a=Tk()
        bw=Button(a,text='{} WINS'.format(namep2),padx=10,pady=5,bd=5)
        bw.pack()
        c=10
        H()
        f = 1
    else:
        if c==9:
            a=Tk()
            bd=Button(a,text='Its a Draw',padx=10,pady=5,bd=5)
            bd.pack()
            f = 1
    if f == 1:
        l1 = [1,2,3,4,5,6,7,8,9]
        l2 = []
        flag = 0
        c3 = 0
        c = 0
    
# Select Win with O
# Win X
def winxso():
    global c, a, c3, flag, l1, l2
    f = 0
    if btn1['text']==btn4['text']==btn7['text']=='X' or btn2['text']==btn5['text']==btn8['text']=='X' or btn3['text']==btn6['text']==btn9['text']=='X' or btn1['text']==btn2['text']==btn3['text']=='X' or btn4['text']==btn5['text']==btn6['text']=='X' or btn7['text']==btn8['text']==btn9['text']=='X' or btn1['text']==btn5['text']==btn9['text']=='X' or btn3['text']==btn5['text']==btn7['text']=='X':
        a=Tk()
        bw=Button(a,text='{} WINS'.format(namep2),padx=10,pady=5,bd=5)
        bw.pack()
        c=10
        H()
        f = 1
    elif btn1['text']==btn4['text']==btn7['text']=='O' or btn2['text']==btn5['text']==btn8['text']=='O' or btn3['text']==btn6['text']==btn9['text']=='O' or btn1['text']==btn2['text']==btn3['text']=='O' or btn4['text']==btn5['text']==btn6['text']=='O' or btn7['text']==btn8['text']==btn9['text']=='O' or btn1['text']==btn5['text']==btn9['text']=='O' or btn3['text']==btn5['text']==btn7['text']=='O':
        a=Tk()
        bw=Button(a,text='{} WINS'.format(namep1),padx=10,pady=5,bd=5)
        bw.pack()
        c=10
        H()
        f = 1
    else:
        if c==9:
            a=Tk()
            bd=Button(a,text='Its a Draw',padx=10,pady=5,bd=5)
            bd.pack()
            f = 1
    if f == 1:
        l1 = [1,2,3,4,5,6,7,8,9]
        l2 = []
        flag = 0
        c3 = 0
        c = 0
    
# Cheat
def cheat():
    global c
    c=c-1
    a=Tk()
    cb=Button(a,text='Dont Cheat',padx=10,pady=5,bd=5)
    cb.pack()

#Buttons
def b11():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=1
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a1=Frame(a)
                a1.pack()
                btn1['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn1['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b12():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=2
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a1=Frame(a)
                a1.pack()
                btn2['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn2['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b13():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=3
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a1=Frame(a)
                a1.pack()
                btn3['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn3['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b21():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=4
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a2=Frame(a)
                a2.pack()
                btn4['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn4['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b22():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=5
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a2=Frame(a)
                a2.pack()
                btn5['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn5['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b23():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=6
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a2=Frame(a)
                a2.pack()
                btn6['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn6['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b31():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=7
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a3=Frame(a)
                a3.pack()
                btn7['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn7['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b32():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2=8
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p==1:
                a3=Frame(a)
                a3.pack()
                btn8['text'] = sxo1
                p=0
            elif p==0:
                a1=Frame(a)
                a1.pack()
                btn8['text'] = sxo2
                p=1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
def b33():
    global p, l1, c, l2, sxo1, sxo2
    c=c+1
    c2 = 9
    if c2 in l2:
        cheat()
    else:
        if c in l1:
            l2.append(c2)
            if p == 1:
                a3 = Frame(a)
                a3.pack()
                btn9['text'] = sxo1
                p = 0
            elif p == 0:
                a1 = Frame(a)
                a1.pack()
                btn9['text'] = sxo2
                p = 1
        if sxo1 == 'O':
            winxso()
        else:
            winxsx()
            
# Printing Who Selects What
def XO(s1, s2):
    global flag, a, p
    p=1
    flag=flag+1
    if flag==1:
        a=Tk()
        a.title('TIC TAC TOE')
        lx=Label(a,text='{} Selects {}      and      {} Selects {}\n'.format(namep1,s1,namep2,s2))
        lx.pack()

# Select X
def startXO(s1, s2):
    global a, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, sxo1, sxo2
    XO(s1, s2)
    sxo1 = s1
    sxo2 = s2
    a1=Frame(a)
    a2=Frame(a)
    a3=Frame(a)
    a1.pack()
    a2.pack()
    a3.pack()
    btn1=Button(a1,padx=33,pady=26,bd=10, text = ' ', fg='Black',command=b11)
    btn2=Button(a1,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b12)
    btn3=Button(a1,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b13)
    btn4=Button(a2,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b21)
    btn5=Button(a2,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b22)
    btn6=Button(a2,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b23)
    btn7=Button(a3,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b31)
    btn8=Button(a3,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b32)
    btn9=Button(a3,padx=33,pady=26,bd=10, text = ' ',fg='Black',command=b33)
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)
    btn6.pack(side=LEFT)
    btn7.pack(side=LEFT)
    btn8.pack(side=LEFT)
    btn9.pack(side=LEFT)

# Select X
def startX():
    global s1, s2, a, a1, p, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, namep1, namep2,c3
    if c3==0:
        startXO('X','O')
        c3=1
    else:
        pass

# Select O
def startO():
    global s1, s2, a, a1, p, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, namep1, namep2, c3
    if c3==0:
        startXO('O','X')
        c3=1
    else:
        pass

# Boar

global l1, l2, c, c3, s1, s2
s1 = ''
s2 = ''
l1 = [1,2,3,4,5,6,7,8,9]
l2 = []
c3 = 0
c = 0
flag = 0

# Select button
def select():
    global namep1
    l = Label( root, text = '{} Is Requested To Select'.format( namep1)).grid( row = 5, columnspan = 3, padx = 20, pady = 20)
    btnX = Button( root, padx=23, pady=16, text='X', bd=10, fg='Black', command = startX).grid( row=6, column=0, padx = 20, pady = 20)
    btnO = Button( root, padx=23, pady=16, text='O', bd=10, fg='Black', command = startO).grid( row=6, column=2, padx = 20, pady = 20)

#Checking Name columns
def check():
    global namep1, namep2
    namep1, namep2 = p1v.get(), p2v.get()
    namep1, namep2 = namep1.upper(), namep2.upper()
    if namep1.strip() != '' or namep2.strip() != '':
        select()

root=Tk()
root.title('TIC TAC TOE')
heading_label = Label(root, padx= 20, pady = 20, text='TIC TAC TOE', font=("Helvetica", 15), fg='black') 
heading_label.grid(rowspan=1, row=1, columnspan=3)
p1 = Label(root,text='NAME OF PLAYER 1', padx= 20, pady = 20, font=("Helvetica", 10), fg='black').grid(row=2,column=0, columnspan=2)
p1v = StringVar()
p1n = Entry(root,textvariable=p1v).grid(row=2,column=2, columnspan=1, padx=20, pady = 20)
p2 = Label(root,text='NAME OF PLAYER 2', padx= 20, pady = 20, font=("Helvetica", 10), fg='black').grid(row=3,column=0, columnspan=2)
p2v = StringVar()
p2n = Entry(root,textvariable=p2v).grid(row=3,column=2, columnspan=1, padx = 20, pady = 20)
btnok = Button(root,padx=35,pady=5,text='SELECT',bd=10,fg='Black',command=check).grid(row=4, columnspan=3, pady = 20)
mainloop()
