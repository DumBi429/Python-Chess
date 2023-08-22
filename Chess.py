import tkinter as tk
from tkinter import ttk
from tkinter import *
#p r kn b q k
# 
# def redtiles(a0):
##############################################################################################################################################
#The current issues are that
#   1. The game doesn't know when the king is in check (and at the same time, the game should know when it is over / have a 'play again' button)
#   2. Game doesnt know about promoting, en passant, and castling
#   3. The window needs more info (line numbers/letters, maybe how many pieces up, taken pieces list)
##############################################################################################################################################
rb=[7,15,23,31,39,47,55,63]
tb=[0,1,2,3,4,5,6,7]
bb=[56,57,58,59,60,61,62,63]
lb=[0,8,16,24,32,40,48,56]
stage="red"
wincheck=False
bincheck=False
lastnum= -1
sndlastnum=-1
turn= "w"
clist=['b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w','w']
blist=[]
hiddenchecks=[]
oldplist=[]
oldclist=[]
temppieces=[]
whiddencheckes=[]
bhiddencheckes=[]
enpass=False
enpassgiven=False
temppiecesbool=False
#maybe make a variable that makes sure that tempplieces doesnt change more than one time pe
#maybe make two fuctions, one that sets temppieces and one that tracks if it was recently changes
plist=['r','kn','b','q','k','b','kn','r','p','p','p','p','p','p','p','p','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','p','p','p','p','p','p','p','p','r','kn','b','q','k','b','kn','r']
imglist=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
falselist=[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
#I am just testing out my new setup with this one :)
def checkerclist():
    color_setup=[]
    i=0
    j=0
    yn=0        
    while i <8:
        if i%2==1:
            yn=1
        else:
            yn=0
        while j <8:
            if yn==0:
                color_setup.append('blue')
                yn=1
            elif yn==1:
                color_setup.append('green')
                yn=0

            j=j+1
        j=0
        i=i+1
    return color_setup
colors= checkerclist()

def boardarray(x,y):
    barray=[]
    st=0
    while st<(x*y):
        barray.append(Tile(st,"",[],''))
        st=st+1
    return barray

#CURRENTLY I AM TRYING TO FIGURE OUT THE EXAMPLE CALL IN REFRESH SO I KNOW WHAT TO MAKE THE MAINLOOP AT THE END
class Example(tk.Frame):
    def __init__(self,parent):
        global imglist
        tk.Frame.__init__(self,parent)
        self.parent = parent
    
        b0= tk.Button(parent,text=plist[0],image =imglist[0],command=lambda:refresh(0),height=90,width=90, bg=colors[0]).grid(row=int((0-(0%8))/8),column= int(0%8))
        b1= tk.Button(parent,text=plist[1],image =imglist[1],command=lambda:refresh(1),height=90,width=90, bg=colors[1]).grid(row=int((1-(1%8))/8),column= int(1%8))
        b2= tk.Button(parent,text=plist[2],image =imglist[2],command=lambda:refresh(2),height=90,width=90, bg=colors[2]).grid(row=int((2-(2%8))/8),column= int(2%8))
        b3= tk.Button(parent,text=plist[3],image =imglist[3],command=lambda:refresh(3),height=90,width=90, bg=colors[3]).grid(row=int((3-(3%8))/8),column= int(3%8))
        b4= tk.Button(parent,text=plist[4],image =imglist[4],command=lambda:refresh(4),height=90,width=90, bg=colors[4]).grid(row=int((4-(4%8))/8),column= int(4%8))
        b5= tk.Button(parent,text=plist[5],image =imglist[5],command=lambda:refresh(5),height=90,width=90, bg=colors[5]).grid(row=int((5-(5%8))/8),column= int(5%8))
        b6= tk.Button(parent,text=plist[6],image =imglist[6],command=lambda:refresh(6),height=90,width=90, bg=colors[6]).grid(row=int((6-(6%8))/8),column= int(6%8))
        b7= tk.Button(parent,text=plist[7],image =imglist[7],command=lambda:refresh(7),height=90,width=90, bg=colors[7]).grid(row=int((7-(7%8))/8),column= int(7%8))
        b8= tk.Button(parent,text=plist[8],image =imglist[8],command=lambda:refresh(8),height=90,width=90, bg=colors[8]).grid(row=int((8-(8%8))/8),column= int(8%8))
        b9= tk.Button(parent,text=plist[9],image =imglist[9],command=lambda:refresh(9),height=90,width=90, bg=colors[9]).grid(row=int((9-(9%8))/8),column= int(9%8))
        b10= tk.Button(parent,text=plist[10],image =imglist[10],command=lambda:refresh(10),height=90,width=90, bg=colors[10]).grid(row=int((10-(10%8))/8),column= int(10%8))
        b11= tk.Button(parent,text=plist[11],image =imglist[11],command=lambda:refresh(11),height=90,width=90, bg=colors[11]).grid(row=int((11-(11%8))/8),column= int(11%8))
        b12= tk.Button(parent,text=plist[12],image =imglist[12],command=lambda:refresh(12),height=90,width=90, bg=colors[12]).grid(row=int((12-(12%8))/8),column= int(12%8))
        b13= tk.Button(parent,text=plist[13],image =imglist[13],command=lambda:refresh(13),height=90,width=90, bg=colors[13]).grid(row=int((13-(13%8))/8),column= int(13%8))
        b14= tk.Button(parent,text=plist[14],image =imglist[14],command=lambda:refresh(14),height=90,width=90, bg=colors[14]).grid(row=int((14-(14%8))/8),column= int(14%8))
        b15= tk.Button(parent,text=plist[15],image =imglist[15],command=lambda:refresh(15),height=90,width=90, bg=colors[15]).grid(row=int((15-(15%8))/8),column= int(15%8))
        b16= tk.Button(parent,text=plist[16],image =imglist[16],command=lambda:refresh(16),height=90,width=90, bg=colors[16]).grid(row=int((16-(16%8))/8),column= int(16%8))
        b17= tk.Button(parent,text=plist[17],image =imglist[17],command=lambda:refresh(17),height=90,width=90, bg=colors[17]).grid(row=int((17-(17%8))/8),column= int(17%8))
        b18= tk.Button(parent,text=plist[18],image =imglist[18],command=lambda:refresh(18),height=90,width=90, bg=colors[18]).grid(row=int((18-(18%8))/8),column= int(18%8))
        b19= tk.Button(parent,text=plist[19],image =imglist[19],command=lambda:refresh(19),height=90,width=90, bg=colors[19]).grid(row=int((19-(19%8))/8),column= int(19%8))
        b20= tk.Button(parent,text=plist[20],image =imglist[20],command=lambda:refresh(20),height=90,width=90, bg=colors[20]).grid(row=int((20-(20%8))/8),column= int(20%8))
        b21= tk.Button(parent,text=plist[21],image =imglist[21],command=lambda:refresh(21),height=90,width=90, bg=colors[21]).grid(row=int((21-(21%8))/8),column= int(21%8))
        b22= tk.Button(parent,text=plist[22],image =imglist[22],command=lambda:refresh(22),height=90,width=90, bg=colors[22]).grid(row=int((22-(22%8))/8),column= int(22%8))
        b23= tk.Button(parent,text=plist[23],image =imglist[23],command=lambda:refresh(23),height=90,width=90, bg=colors[23]).grid(row=int((23-(23%8))/8),column= int(23%8))
        b24= tk.Button(parent,text=plist[24],image =imglist[24],command=lambda:refresh(24),height=90,width=90, bg=colors[24]).grid(row=int((24-(24%8))/8),column= int(24%8))
        b25= tk.Button(parent,text=plist[25],image =imglist[25],command=lambda:refresh(25),height=90,width=90, bg=colors[25]).grid(row=int((25-(25%8))/8),column= int(25%8))
        b26= tk.Button(parent,text=plist[26],image =imglist[26],command=lambda:refresh(26),height=90,width=90, bg=colors[26]).grid(row=int((26-(26%8))/8),column= int(26%8))
        b27= tk.Button(parent,text=plist[27],image =imglist[27],command=lambda:refresh(27),height=90,width=90, bg=colors[27]).grid(row=int((27-(27%8))/8),column= int(27%8))
        b28= tk.Button(parent,text=plist[28],image =imglist[28],command=lambda:refresh(28),height=90,width=90, bg=colors[28]).grid(row=int((28-(28%8))/8),column= int(28%8))
        b29= tk.Button(parent,text=plist[29],image =imglist[29],command=lambda:refresh(29),height=90,width=90, bg=colors[29]).grid(row=int((29-(29%8))/8),column= int(29%8))
        b30= tk.Button(parent,text=plist[30],image =imglist[30],command=lambda:refresh(30),height=90,width=90, bg=colors[30]).grid(row=int((30-(30%8))/8),column= int(30%8))
        b31= tk.Button(parent,text=plist[31],image =imglist[31],command=lambda:refresh(31),height=90,width=90, bg=colors[31]).grid(row=int((31-(31%8))/8),column= int(31%8))
        b32= tk.Button(parent,text=plist[32],image =imglist[32],command=lambda:refresh(32),height=90,width=90, bg=colors[32]).grid(row=int((32-(32%8))/8),column= int(32%8))
        b33= tk.Button(parent,text=plist[33],image =imglist[33],command=lambda:refresh(33),height=90,width=90, bg=colors[33]).grid(row=int((33-(33%8))/8),column= int(33%8))
        b34= tk.Button(parent,text=plist[34],image =imglist[34],command=lambda:refresh(34),height=90,width=90, bg=colors[34]).grid(row=int((34-(34%8))/8),column= int(34%8))
        b35= tk.Button(parent,text=plist[35],image =imglist[35],command=lambda:refresh(35),height=90,width=90, bg=colors[35]).grid(row=int((35-(35%8))/8),column= int(35%8))
        b36= tk.Button(parent,text=plist[36],image =imglist[36],command=lambda:refresh(36),height=90,width=90, bg=colors[36]).grid(row=int((36-(36%8))/8),column= int(36%8))
        b37= tk.Button(parent,text=plist[37],image =imglist[37],command=lambda:refresh(37),height=90,width=90, bg=colors[37]).grid(row=int((37-(37%8))/8),column= int(37%8))
        b38= tk.Button(parent,text=plist[38],image =imglist[38],command=lambda:refresh(38),height=90,width=90, bg=colors[38]).grid(row=int((38-(38%8))/8),column= int(38%8))
        b39= tk.Button(parent,text=plist[39],image =imglist[39],command=lambda:refresh(39),height=90,width=90, bg=colors[39]).grid(row=int((39-(39%8))/8),column= int(39%8))
        b40= tk.Button(parent,text=plist[40],image =imglist[40],command=lambda:refresh(40),height=90,width=90, bg=colors[40]).grid(row=int((40-(40%8))/8),column= int(40%8))
        b41= tk.Button(parent,text=plist[41],image =imglist[41],command=lambda:refresh(41),height=90,width=90, bg=colors[41]).grid(row=int((41-(41%8))/8),column= int(41%8))
        b42= tk.Button(parent,text=plist[42],image =imglist[42],command=lambda:refresh(42),height=90,width=90, bg=colors[42]).grid(row=int((42-(42%8))/8),column= int(42%8))
        b43= tk.Button(parent,text=plist[43],image =imglist[43],command=lambda:refresh(43),height=90,width=90, bg=colors[43]).grid(row=int((43-(43%8))/8),column= int(43%8))
        b44= tk.Button(parent,text=plist[44],image =imglist[44],command=lambda:refresh(44),height=90,width=90, bg=colors[44]).grid(row=int((44-(44%8))/8),column= int(44%8))
        b45= tk.Button(parent,text=plist[45],image =imglist[45],command=lambda:refresh(45),height=90,width=90, bg=colors[45]).grid(row=int((45-(45%8))/8),column= int(45%8))
        b46= tk.Button(parent,text=plist[46],image =imglist[46],command=lambda:refresh(46),height=90,width=90, bg=colors[46]).grid(row=int((46-(46%8))/8),column= int(46%8))
        b47= tk.Button(parent,text=plist[47],image =imglist[47],command=lambda:refresh(47),height=90,width=90, bg=colors[47]).grid(row=int((47-(47%8))/8),column= int(47%8))
        b48= tk.Button(parent,text=plist[48],image =imglist[48],command=lambda:refresh(48),height=90,width=90, bg=colors[48]).grid(row=int((48-(48%8))/8),column= int(48%8))
        b49= tk.Button(parent,text=plist[49],image =imglist[49],command=lambda:refresh(49),height=90,width=90, bg=colors[49]).grid(row=int((49-(49%8))/8),column= int(49%8))
        b50= tk.Button(parent,text=plist[50],image =imglist[50],command=lambda:refresh(50),height=90,width=90, bg=colors[50]).grid(row=int((50-(50%8))/8),column= int(50%8))
        b51= tk.Button(parent,text=plist[51],image =imglist[51],command=lambda:refresh(51),height=90,width=90, bg=colors[51]).grid(row=int((51-(51%8))/8),column= int(51%8))
        b52= tk.Button(parent,text=plist[52],image =imglist[52],command=lambda:refresh(52),height=90,width=90, bg=colors[52]).grid(row=int((52-(52%8))/8),column= int(52%8))
        b53= tk.Button(parent,text=plist[53],image =imglist[53],command=lambda:refresh(53),height=90,width=90, bg=colors[53]).grid(row=int((53-(53%8))/8),column= int(53%8))
        b54= tk.Button(parent,text=plist[54],image =imglist[54],command=lambda:refresh(54),height=90,width=90, bg=colors[54]).grid(row=int((54-(54%8))/8),column= int(54%8))
        b55= tk.Button(parent,text=plist[55],image =imglist[55],command=lambda:refresh(55),height=90,width=90, bg=colors[55]).grid(row=int((55-(55%8))/8),column= int(55%8))
        b56= tk.Button(parent,text=plist[56],image =imglist[56],command=lambda:refresh(56),height=90,width=90, bg=colors[56]).grid(row=int((56-(56%8))/8),column= int(56%8))
        b57= tk.Button(parent,text=plist[57],image =imglist[57],command=lambda:refresh(57),height=90,width=90, bg=colors[57]).grid(row=int((57-(57%8))/8),column= int(57%8))
        b58= tk.Button(parent,text=plist[58],image =imglist[58],command=lambda:refresh(58),height=90,width=90, bg=colors[58]).grid(row=int((58-(58%8))/8),column= int(58%8))
        b59= tk.Button(parent,text=plist[59],image =imglist[59],command=lambda:refresh(59),height=90,width=90, bg=colors[59]).grid(row=int((59-(59%8))/8),column= int(59%8))
        b60= tk.Button(parent,text=plist[60],image =imglist[60],command=lambda:refresh(60),height=90,width=90, bg=colors[60]).grid(row=int((60-(60%8))/8),column= int(60%8))
        b61= tk.Button(parent,text=plist[61],image =imglist[61],command=lambda:refresh(61),height=90,width=90, bg=colors[61]).grid(row=int((61-(61%8))/8),column= int(61%8))
        b62= tk.Button(parent,text=plist[62],image =imglist[62],command=lambda:refresh(62),height=90,width=90, bg=colors[62]).grid(row=int((62-(62%8))/8),column= int(62%8))
        b63= tk.Button(parent,text=plist[63],image =imglist[63],command=lambda:refresh(63),height=90,width=90, bg=colors[63]).grid(row=int((63-(63%8))/8),column= int(63%8))





class Frames():
    def __init__(self):
        self.root=tk.Tk()
        self.frame= None
        self.startup()
        self.refresh(-1)
        self.pieces=plist
        self.colors=clist
        self.stage=stage
        
    def startup(self):
        global imglist
        if imglist==falselist:
            i=0
            while i < len(plist):
                if plist[i]=='p' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WP.png"))
                
                elif plist[i]=='b' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WB.png"))
                elif plist[i]=='k' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WK.png"))
                elif plist[i]=='kn' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WKN.png"))
                elif plist[i]=='q' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WQ.png"))
                elif plist[i]=='r' and clist[i]=='w':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WR.png"))
                elif plist[i]=='p' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BP.png"))
                elif plist[i]=='b' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BB.png"))
                elif plist[i]=='k' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BK.png"))
                elif plist[i]=='kn' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BKN.png"))
                elif plist[i]=='q' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BQ.png"))
                elif plist[i]=='r' and clist[i]=='b':
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\BR.png"))
                else:
                    imglist[i]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\empty.png"))
                i=i+1
    def getroot():
        return self.root
    def create_tiles():
        st=0
        while st<(64):
            arr1.append(Tile(st,"",[],''))
            st=st+1
    def set_up_chess():
        if stage == 'ChessSU':
            chess_setup=['r','kn','b','q','k','b','kn','r','p','p','p','p','p','p','p','p','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','p','p','p','p','p','p','p','p','r','kn','b','q','k','b','kn','r']
            color_setup=checkerclist()
            count=0
        for pos in chess_setup:
            arr1[count].piece = pos
            arr1[count].color = color_setup[count]
            count=count+1
        # some code
    def changestage(self,nextstage):
        self.stage= nextstage
    def get_stage(self):
        return self.stage
    def buttons(self,stage):
        i=0
        while i < 63:
            arr1[i].createbutton(self.root)
            blist.append(arr1[i].getbutton())
            i=i+1
    def choosepiece(self,choice,num):
        print("MADE IT INTO THE CHOOSEPIECE")
        plist[lastnum]=''
        plist[num]=choice
        cou=clist[lastnum]
        clist[lastnum]=''
        clist[num]=cou
        imglist[lastnum]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\empty.png"))
        if choice=='q':
            imglist[num]= (tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WQ.png"))
        elif choice=='b':
            imglist[num]= (tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WB.png"))
        elif choice=='r':
            imglist[num]= (tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WR.png"))
        elif choice=='kn':
            imglist[num]= (tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\WKN.png"))
        
    def refresh(self,num):
        if self.frame is None:
            self.frame = Example(self.root)
        else:    
            global stage
            global arr1
            global clist
            global blist
            global colors
            global lastnum
            global sndlastnum
            global wincheck
            global oldplist
            global oldclist
            global enpass
            if stage=='red':
                if clist[num] is not turn:
                    stage='red'
                    moves=[]
                else:
                    stage ='move'
                    sndlastnum= lastnum
                    lastnum=num
                    moves=getmoves(num)   
                    colors = movestoredclist(moves)
                    
                if moves!=[]:
                    oldplist=plist
                    oldclist=clist
                    self.frame.destroy()
                    self.frame = Example(self.root)
                else:
                    stage='red'
            elif stage =='move':
                    if plist[lastnum]=='p' and (num == lastnum+16 or num== lastnum-16):
                        enpass= True
                    else:
                        enpass=False
                    stage ='red'
                    movepiece(num,False,-1,-1)
                    colors= checkerclist()
                    oldplist=plist
                    oldclist=clist
                    self.frame.destroy()
                    self.frame = Example(self.root)
                    
                    updatechecks()
                    print("After updating checks (L:258), wincheck is {0} and bincheck is {1}".format(wincheck,bincheck))
                

class Tile(Frames):
    def __init__(self,pos,piece,moves,color):
        self.pos=pos
        self.piece=piece
        self.moves=moves
        self.xpos= pos %8
        self.ypos= int((pos-(pos%8))/8) #relistically 8 is arbetrary here
        self.color= color
    def createbutton(self,tile):
        self.button= tk.Button(root,text=self.piece,command=super().refresh(self.pos),height=4,width=10).grid(row=self.ypos,column=self.xpos)
    def getbutton(self):
        return self.button
    def __str__(self):
        return f"pos:{self.pos}, piece:{self.piece}, moves:{self.moves}"
    def id(self):
        return self.pos
    def set_piece(new):
        self.piece=new
    def set_moves(new):
        self.moves=new
   
f1=Frames()

def refresh(num):
    f1.refresh(num)
def settemppieces(l):
    global temppiecesbool
    global temppieces
    temppieces=[]
    if temppiecesbool== False:
        i=0
        while i<len(l):
            temppieces.append(l[i])
            i=i+1
                
    
        temppiecesboo(True,True)
        
def temppiecesboo(change, changeto):
    if change==True:
        global temppiecesbool
        temppeicesbool=changeto
temppiecesbool=False
def movepiece(num,temp,fro,onto):

    global turn
    if temp==False:
        if colors[num]=='red':
            if turn=='w':
                turn='b'
            else:
                turn='w'
            if enpassgiven==True:
                print('Enpassgiven is true at this point')
                if plist[lastnum]=='p':
                    
                    if num==lastnum+9:
                        plist[lastnum-1]=''
                        clist[lastnum-1]=''
                        imglist[lastnum-1]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\empty.png"))
                    elif num==lastnum+7:
                        plist[lastnum+1]=''
                        clist[lastnum+1]=''
                        imglist[lastnum+1]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\empty.png"))
            piece=plist[lastnum]
            plist[lastnum]=''
            plist[num]=piece
            cou=clist[lastnum]
            clist[lastnum]=''
            clist[num]=cou
            imm= imglist[lastnum]
            imglist[lastnum]=(tk.PhotoImage(file = r"C:\Users\gtmot\Desktop\CHess\pieces\empty.png"))
            imglist[num]=imm
    else:
        piece=plist[fro]
        plist[fro]=''
        plist[onto]=piece
        cou=clist[fro]
        clist[fro]=''
        clist[onto]=cou



def findpieces():
    ret=[]
    ind=0
    for x in(plist):
        if not(x=='' or x==""):
            ret.append(ind)
        ind=ind+1
    
    return ret
def getkings():
    ret=[]
    i =0
    while i<len(plist):
        
       
        if plist[i] == 'k':
            if clist[i]=='w':
                ret.append([i,'w'])
            elif clist[i]=='b':
                ret.append([i,'b'])
        i=i+1
    return ret
#What i need to do is just brute force the calculations and check to see if in check.
#then separately, I need to use brute force each time a xmoves() is called so that it checks for hidden checks            
def currentopposingpieces(c):
    #this should only be called inside of incheck so you can just call currentopposingpieces(c)
    outputlist=[]
    ourcolor= c
    if ourcolor=='w':
        oppcolor='b'
    elif ourcolor=='b':
        oppcolor='w'
    else:
        print('ERROR: invalid color in currentopposingpieces')
    #set ourcolor and oppcolor
    #now find our color in clist and add the piece and index to outputlist
    n=0
    while n < 64:
        curcol= clist[n]
        if curcol==oppcolor:
            outputlist.append([plist[n],n])
        n=n+1
    return outputlist
def incheck(c):
    global stage
    global arr1
    global clist
    global blist
    global plist
    global colors
    global lastnum
    global sndlastnum
    global wincheck
    global bincheck

#alrighty now, what i have to do is brute force this checking code 
    # I would first make a list of the pieces on the opposing team (make sure the code is not team specific)
    #Then i can see if those pieces' moves set contain the index of the opposing team's king and cycle
        #one thing to think about is if you need any information out of this code in later code (like hidden check)
            #and if so, have the inckeck function take in a variable that is checked before going through the shit
    retcheck=False
    opps=currentopposingpieces(c)
    
    kings=getkings()
    if kings[0][1]=='b':
        wking=kings[1][0]
        bking=kings[0][0]
    else:
        bking=kings[1][0]
        wking=kings[0][0]
    if c =='w':
        ourking=wking
        theirking=bking
    elif c=='b':
        ourking=bking
        theirking=wking
    else:
        print('oopsie woopsie line 413')
    for anopp in opps:
        
        
        #anopp[0] is the piece -- anopp[1] is the index
        if anopp[0]=='k':
            tempmoves= kmoves(anopp[1],False)
        elif anopp[0]=='kn':
            tempmoves= knmoves(anopp[1],False)
        elif anopp[0]=='q':
            tempmoves= qmoves(anopp[1],False)
        elif anopp[0]=='b':
            tempmoves= bmoves(anopp[1],False)
        elif anopp[0]=='p':
            tempmoves= pmoves(anopp[1],False)
        elif anopp[0]=='r':
            tempmoves=rmoves(anopp[1],False)
        else:
            print('oopsie woopsie line 416')
            tempmoves=[]
    
        for index in tempmoves:
            if index==ourking:
                checkingpiece=anopp[0]
                retcheck=True
                print('CHECK DETECTED BY:')
                print(checkingpiece)

    return retcheck








    #     #check each of the moves types on the kings place and if the piece that the move comes from is able to be taken by the king,the king is in check from that piece
    # if c=='w' or c=="w":
    #     kn=knmoves(wking,True)
    #     print('NEXT 5 LISTS ARE (366) CHECK MOVES')
    #     print(kn) 
        
    #     q=qmoves(wking,True)
    #     print(q)
    #     b=bmoves(wking,True)
    #     print(b)
    #     p=pmoves(wking,True)
    #     print(p)
    #     r=rmoves(wking,True)4
    #     print(r)
    #     i=-1 
    #     for pi in kn:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='kn':
    #                 if clist[kn[i][0]]=='b':
    #                     print("line344")
    #                     wincheck=True
                        
    #     i=-1
        
                        
    #     i=-1
    #     for pi in q:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='q':
    #                 if clist[q[i][0]]=='b':
    #                     print("line369")
    #                     wincheck=True
                        
    #     i=-1
    #     for pi in b:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='b':
    #                 if clist[b[i][0]]=='b':
    #                     print("line380")
    #                     wincheck=True
                        
    #     i=-1
    #     for pi in p:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='p':
    #                 if clist[p[i][0]]=='b':
    #                     print("Line392")
    #                     wincheck=True
                        
    #     i=-1
    #     for pi in r:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='r':
    #                 if clist[r[i][0]]=='b':
    #                     print("line402")
    #                     wincheck=True
                        
    #     if wincheck==True:
    #         return True
        
    # if c=='b' or c=="b":
    #     kn=knmoves(bking,True)
    #     print('THE NEXT....................................(450)')
    #     print(kn)
        
    #     q=qmoves(bking,True)
    #     print(q)
    #     b=bmoves(bking,True)
    #     print(b)
    #     p=pmoves(bking,True)
    #     print(p)
    #     r=rmoves(bking,True)
    #     print(r)
    #     i=-1
        
    #     for pi in kn:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='kn':
    #                 if clist[kn[i][0]]=='w':
    #                     print("line424")
    #                     bincheck=True
                        
        
                        
    #     i=-1
    #     for pi in q:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='q':
    #                 if clist[q[i][0]]=='w':i
    #                     print("line3asdasd")
    #                     bincheck=True
                        
    #     i=-1
    #     for pi in b:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='b':
    #                 if clist[b[i][0]]=='w':
    #                     print("line344werwer")
    #                     bincheck=True
                        
    #     i=-1
    #     for pi in p:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='p':
    #                 if clist[p[i][0]]=='w':
    #                     print("line344bing casinap")
    #                     bincheck=True
                        
    #     i=-1
    #     for pi in r:
    #         i=i+1
    #         j=-1
    #         for pie in pi:
    #             j=j+1
    #             if pie=='r':
    #                 if clist[r[i][0]]=='w':
    #                     print("line344qweqwfzxvzxs")
    #                     bincheck=True
    #     if bincheck==True:
    #         return True
    #     return False
    
def updatechecks():
    w1=incheck('w')
    b1=incheck('b')
    global wincheck
    global bincheck
    if w1==True:
        wincheck=True
    else:
        wincheck=False
    if b1==True:
        bincheck=True
    else:
        bincheck=False
        
def updatehiddenchecks(c):
    global stage
    global arr1
    global clist
    global blist
    global plist
    global colors
    global lastnum
    global sndlastnum
    global wincheck
    global bincheck
    global hiddenchecks
    global oldplist
    global bhiddencheckes
    global whiddencheckes

    ntc=[]
    mc=[]
    hcp=[]
    co=c
    kings=getkings()
    if kings[0][1]=='b':
        wking=kings[1][0]
        bking=kings[0][0]
    else:
        bking=kings[1][0]
        wking=kings[0][0]
        #check each of the moves types on the kings place and if the piece that the move comes from is able to be taken by the king,the king is in check from that piece 
    
    if co=='w':
        
        i=0
        if plist==oldplist:
            settemppieces(plist)
            
            
            while i<len(plist):
                piece=plist[i]
                if clist[i]=='w':
                    if piece!='k':
                        plist[i]=''
                i=i+1
            #fromt the time i
            q=qmoves(wking,True)
            
            b=bmoves(wking,True)
            
            r=rmoves(wking,True)
            
            tempvar=0
            plist=[]
            while tempvar<len(temppieces):
                
                plist.append(temppieces[tempvar])
                tempvar=tempvar+1
            
            i=-1
            j=-1
            for pi in q:
                i=i+1
                for thing in pi:
                    j=j+1
                    if thing=='q':
                        ntc.append([q[i][0],q[i][2]])
            i=-1
            j=-1
            for pi in b:
                i=i+1
                for pie in pi:
                    j=j+1
                    if pie=='b':
                        ntc.append([b[i][0],b[i][2]])
            i=-1
            j=-1
            for pi in r:
                i=i+1
                for pie in pi:
                    j=j+1
                    if pie=='r':
                        ntc.append([r[i][0],r[i][2]])
            #it crashes every time there is a piece in front of the piece that is checking
           
        q=qmoves(wking,True)
        b=bmoves(wking,True)
        r=rmoves(wking,True)
        i=-1
        j=-1
        for pi in q:
            i=i+1
            for thing in pi:
                j=j+1
                if thing=='q':
                    mc.append([q[i][0],q[i][2]])
        i=-1
        j=-1
        for pi in b:
            i=i+1
            for pie in pi:
                j=j+1
                if pie=='b':
                    mc.append([b[i][0],b[i][2]])
        i=-1
        j=-1
        for pi in r:
            i=i+1
            for pie in pi:
                j=j+1
                if pie=='r':
                    mc.append([r[i][0],r[i][2]])
        i=0
        while i<len(ntc):
            num=ntc[i][0]
            direc=ntc[i][1]
            badegg=False
            j=0
            
            while j<len(mc):
                if mc[j][0]==num:
                    badegg=True
                    break
                j=j+1
            if badegg==True:
                i=i-1
                ntc.pop(i+1)
            i=i+1
        i=0
        while i<len(ntc):
            direc=ntc[i][1]
            num=ntc[i][0]
            count=-1
            first=-1
            if direc=="-8":   
                if num not in tb:
                    n=0
                    while n<8:
                        n=n+1
                        if num-8*n in tb:
                            if clist[num-8*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num-8*n
                            break
                        if clist[num-8*n]=='w':
                            count=count+1
                            if count==0:
                                first=num-8*n
                        if count>1:
                            break
                    if count==1:
                        whiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=="+8":   
                if num not in bb:
                    n=0
                    while n<8:
                        n=n+1
                        if num+8*n in bb:
                            if clist[num+8*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num+8*n
                            break
                        if clist[num+8*n]=='w':
                            count=count+1
                            if count==0:
                                first=num+8*n
                        
                        if count>1:
                            break
                    if count==1:
                        whiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            
            elif direc=="-1":   
                if num not in lb:
                    n=0
                    while n<8:
                        n=n+1
                        if num-1*n in lb:
                            if clist[num-1*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num-1*n
                            break
                        if clist[num-1*n]=='w':
                            count=count+1
                            if count==0:
                                first=num-1*n
                        
                        if count>1:
                            break
                    if count==1:
                        whiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=="+1":   
                if num not in rb:
                    n=0
                    while n<8:
                        n=n+1
                        if num+1*n in rb:
                            if clist[num+1*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num+1*n
                            break
                        if clist[num+1*n]=='w':
                            count=count+1
                            if count==0:
                                first=num+1*n
                
                        if count>1:
                            break
                    if count==1:
                        whiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=="+7":   
                if num not in bb:
                    if num not in lb:
                        n=0
                        while n<8:
                            n=n+1
                            if num+7*n in lb or num+7*n in bb:
                                if clist[num+7*n]=='w':
                                    count=count+1
                                    if count==0:
                                        first=num+7*n
                                break
                            if clist[num+7*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num+7*n
                            
                            if count>1:
                                break
                        if count==1:
                            whiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=="+9":   
                if num not in bb:
                    if num not in rb:
                        n=0
                        while n<8:
                            n=n+1
                            if num+9*n in rb or num+9*n in bb:
                                if clist[num+9*n]=='w':
                                    count=count+1
                                    if count==0:
                                        first=num+9*n
                                break
                            if clist[num+9*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num+9*n
                            
                            if count>1:
                                break
                        if count==1:
                            whiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=="-7":   
                if num not in tb:
                    if num not in rb:
                        n=0
                        while n<8:
                            n=n+1
                            if num-7*n in rb or num-7*n in tb:
                                if clist[num-7*n]=='w':
                                    count=count+1
                                    if count==0:
                                        first=num+7*n
                                break
                            if clist[num-7*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num-7*n
                            
                            if count>1:
                                break
                        if count==1:
                            whiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=="-9":   
                if num not in tb:
                    if num not in lb:
                        n=0
                        while n<8:
                            n=n+1
                            if num-9*n in lb or num-9*n in tb:
                                if clist[num-9*n]=='w':
                                    count=count+1
                                    if count==0:
                                        first=num-9*n
                                break
                            if clist[num-9*n]=='w':
                                count=count+1
                                if count==0:
                                    first=num-9*n
                            
                            if count>1:
                                break
                        if count==1:
                            whiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            i=i+1
    else:
        oldplist= plist
        
        if plist==oldplist:
            settemppieces(plist)
            i=0
            while i<len(plist):
                piece=plist[i]
                if clist[i]=='b':
                    if piece!='k':
                        plist[i]=''
                i=i+1
            q=qmoves(bking,True)
            
           
            b=bmoves(bking,True)
            
            r=rmoves(bking,True)
            
            tempvar=0
            plist=[]
            while tempvar<len(temppieces):
                plist.append(temppieces[tempvar])
                tempvar=tempvar+1
            
            i=-1
            j=-1
            
            for pi in q:
                i=i+1
                for thing in pi:
                    j=j+1
                    if thing=='q':
                        ntc.append([q[i][0],q[i][2]])
            i=-1
            j=-1
            for pi in b:
                i=i+1
                for pie in pi:
                    j=j+1
                    if pie=='b':
                        ntc.append([b[i][0],b[i][2]])
            i=-1
            j=-1
            for pi in r:
                i=i+1
                for pie in pi:
                    j=j+1
                    if pie=='r':
                        ntc.append([r[i][0],r[i][2]])
        
                    
            
        q=qmoves(bking,True)
        b=bmoves(bking,True)
        r=rmoves(bking,True)
        i=-1
        j=-1
        for pi in q:
            i=i+1
            for thing in pi:
                j=j+1
                if thing=='q':
                    
                    mc.append([q[i][0],q[i][2]])
        i=-1
        j=-1
        for pi in b:
            i=i+1
            for pie in pi:
                j=j+1
                if pie=='b':
                    mc.append([b[i][0],b[i][2]])
        i=-1
        j=-1
        for pi in r:
            i=i+1
            for pie in pi:
                j=j+1
                if pie=='r':
                    mc.append([r[i][0],r[i][2]])
        i=0
    
         
        while i<len(ntc):
            num=ntc[i][0]
            direc=ntc[i][1]
            badegg=False
            j=0
            while j<len(mc):
                if mc[j][0]==num:
                    
                    badegg=True
                    break
                j=j+1
            if badegg==True:
                i=i-1
                ntc.pop(i+1)
            i=i+1
        i=0
        while i<len(ntc):
            direc=ntc[i][1]
            num=ntc[i][0]
            count=-1
            first=-1
            if direc=='+8':   
                if num not in tb:
                    n=0
                    while n<8:
                        n=n+1
                        if num-8*n in tb:
                            if clist[num-8*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num-8*n
                            break
                        if clist[num-8*n]=='b':
                            count=count+1
                            if count==0:
                                first=num-8*n
                        if count>1:
                            break
                    if count==1:
                        bhiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=='-8':   
                if num not in bb:
                    n=0
                    while n<8:
                        n=n+1
                        if num+8*n in bb:
                            if clist[num+8*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num+8*n
                            break
                        if clist[num+8*n]=='b':
                            count=count+1
                            if count==0:
                                first=num+8*n
                        
                        if count>1:
                            break
                    if count==1:
                        bhiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            
            elif direc=='+1':   
                if num not in lb:
                    n=0
                    while n<8:
                        n=n+1
                        if num-1*n in lb:
                            if clist[num-1*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num-1*n
                            break
                        if clist[num-1*n]=='b':
                            count=count+1
                            if count==0:
                                first=num-1*n
                        
                        if count>1:
                            break
                    if count==1:
                        bhiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=='-1':   
                if num not in rb:
                    n=0
                    while n<8:
                        n=n+1
                        if num+1*n in rb:
                            if clist[num+1*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num+1*n
                            break
                        if clist[num+1*n]=='b':
                            count=count+1
                            if count==0:
                                first=num+1*n
                
                        if count>1:
                            break
                    if count==1:
                        bhiddencheckes.append(first)
                    if count>1:
                        ntc.pop(i)
                        i=i-1
            elif direc=='-7':   
                if num not in bb:
                    if num not in lb:
                        n=0
                        while n<8:
                            n=n+1
                            if num+7*n in lb or num+7*n in bb:
                                if clist[num+7*n]=='b':
                                    count=count+1
                                    if count==0:
                                        first=num+7*n
                                break
                            if clist[num+7*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num+7*n
                            
                            if count>1:
                                break
                        if count==1:
                            bhiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=='-9':   
                if num not in bb:
                    if num not in rb:
                        n=0
                        while n<8:
                            n=n+1
                            if num+9*n in rb or num+9*n in bb:
                                if clist[num+9*n]=='b':
                                    count=count+1
                                    if count==0:
                                        first=num+9*n
                                break
                            if clist[num+9*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num+9*n
                            
                            if count>1:
                                break
                        if count==1:
                            bhiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=='+7':   
                if num not in tb:
                    if num not in rb:
                        n=0
                        while n<8:
                            n=n+1
                            if num-7*n in rb or num-7*n in tb:
                                if clist[num-7*n]=='b':
                                    count=count+1
                                    if count==0:
                                        first=num+7*n
                                break
                            if clist[num-7*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num-7*n
                            
                            if count>1:
                                break
                        if count==1:
                            bhiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            elif direc=='+9':   
                if num not in tb:
                    if num not in lb:
                        n=0

                        while n<8:
                            n=n+1
                            
                            if num-9*n in lb or num-9*n in tb:
                                if clist[num-9*n]=='b':
                                    count=count+1
                                    if count==0:
                                        first=num-9*n
                                break
                            if clist[num-9*n]=='b':
                                count=count+1
                                if count==0:
                                    first=num-9*n
                            
                            if count>1:
                                break
                        if count==1:
                            bhiddencheckes.append(first)
                        if count>1:
                            ntc.pop(i)
                            i=i-1
            
            i=i+1   

def getmoves(num):
    global arr1
    global plist
    global clist
    ourcolor=clist[num]
    ml=[]
    piece=plist[num]
    if plist[num]=="kn":
       ml= knmoves(num,False)
    elif plist[num]=="q":
        ml= qmoves(num,False)
    elif plist[num]=="p":
        ml= pmoves(num,False)
    elif plist[num]== "r":
        ml= rmoves(num,False)
    elif plist[num] =="k":
        ml= kmoves(num,False)
    elif plist[num] == "b":
        ml= bmoves(num,False)
    i=0
    while i<len(ml):
        if ml[i]>63 or ml[i]<0:
            ml.pop(i)
            i=i-1
        i=i+1
    tforplist=[]
    tforclist=[]
    n=0
    while n<64:
        tforplist.append(plist[n])
        tforclist.append(clist[n])
        n=n+1
    print("temp plist:\n{0}\ntemp clist:\n{1}".format(tforplist,tforclist))
    n=0
    while n < len(ml):
        
        movepiece(-1,True,num,ml[n])
        if incheck(ourcolor)==True:
            plist=[]
            clist=[]
            no=0
            while no<64:
                plist.append(tforplist[no])
                clist.append(tforclist[no])
                no=no+1
            print("our plist is:\n{0}\nour clist is:\n{1}".format(plist,clist))
            ml.pop(n)
            n=n-1
        else:
            plist=[]
            clist=[]
            no=0
            while no<64:
                plist.append(tforplist[no])
                clist.append(tforclist[no])
                no=no+1
            print
            # plist[num]=piece
            # clist[num]=ourcolor
        n=n+1

    if ml==[]:
        stage='red'
        return ml
    else:
        return ml
def knmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    bsr=[48,49,50,51,52,53,54,55]
    tsr=[8,9,10,11,12,13,14,15]
    lsr=[1,9,17,25,33,41,49,57]
    rsr=[6,14,22,30,38,46,54,62]
    rfr=[7,15,23,31,39,47,55,63]
    tfr=[0,1,2,3,4,5,6,7]
    bfr=[56,57,58,59,60,61,62,63]
    lfr=[0,8,16,24,32,40,48,56]
    piece=findpieces()
    ourcolor=clist[num]
    opmoves=[num-15,num-17,num-6,num+10,num+17,num+15,num+6,num-10]
    phit=[[]]
    if num in bsr:
        i=0
        while i <len(opmoves):
            if opmoves[i]== num+17 or opmoves[i]== num+15:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in bfr:
        i=0
        ban=[num+17,num+15,num+10,num+6]
        while i <len(opmoves):
            if opmoves[i] in ban:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in tsr:
        i=0
        while i <len(opmoves):
            if opmoves[i]== num-15 or opmoves[i]== num-17:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in tfr:
        i=0
        ban=[num-17,num-15,num-10,num-6]
        while i <len(opmoves):
            if opmoves[i] in ban:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in lsr:
        i=0
        while i <len(opmoves):
            if opmoves[i]== num-10 or opmoves[i]== num+6:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in lfr:
        i=0
        ban=[num-17,num+15,num-10,num+6]
        while i <len(opmoves):
            if opmoves[i] in ban:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in rsr:
        i=0
        while i <len(opmoves):
            if opmoves[i]== num-6 or opmoves[i]== num+10:
                opmoves.pop(i)
                i=i-1
            i=i+1
    if num in rfr:
        i=0
        ban=[num+17,num-15,num+10,num-6]
        while i <len(opmoves):
            if opmoves[i] in ban:
                opmoves.pop(i)
                i=i-1
            i=i+1
    i=0
    while i <len(opmoves):
        if opmoves[i]in piece:
            if forcheck==True:
                phit.append([i,plist[i]])
            if clist[opmoves[i]]==ourcolor:
                if forcheck==True:
                    phit.pop(len(phit)-1)
                opmoves.pop(i)
                i=i-1
                
        i=i+1
    if forcheck==True:
        return phit
    
    if num in hiddenchecks:
        if ourcolor=='w':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('w')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
            
                
                
        if ourcolor=='b':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('b')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
    
    return opmoves
def qmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    opmoves=[]
    sub=num
    ourcolor=clist[num]
    n=1
    piece= findpieces()
    #pieces works for when it is reduced to just one colors pieces
    phit=[]
    #Up down -8
    if num not in tb:
        while n<7:
            if sub-(8*n) in piece:
                if clist[sub-8*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub-8*n,plist[sub-8*n],'-8'])
                    opmoves.append(sub-(8*n))
                    break
                break
            if sub-(8*n) in tb:
                opmoves.append(sub-(8*n))
                break
            
            opmoves.append(sub-(8*n))
            n=n+1
    sub=num
    n=1
    if num not in bb:
        while n<7:
            if sub+(8*n) in piece:
                if clist[sub+8*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub+8*n,plist[sub+8*n],'+8'])
                    opmoves.append(sub+(8*n))
                    break
                break
            if sub+(8*n) in bb:
                opmoves.append(sub+(8*n))
                break
            
            opmoves.append(sub+(8*n))
            n=n+1
    #left right -1
    sub=num
    n=1
    if num not in lb:
        while n<7:
            if sub-(1*n) in piece:
                if clist[sub-1*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub-1*n,plist[sub-1*n],'-1'])
                    opmoves.append(sub-(1*n))
                    break
                break
            if sub-(1*n) in lb:
                opmoves.append(sub-(1*n))
                break
            
            opmoves.append(sub-(1*n))
            n=n+1
    sub=num
    n=1
    if num not in rb:
        while n<7:
            if sub+(1*n) in piece:
                if clist[sub+1*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub+1*n,plist[sub+1*n],'+1'])
                    opmoves.append(sub+(1*n))
                    break
                break
            if sub+(1*n) in rb:
                opmoves.append(sub+(1*n))
                break
            
            opmoves.append(sub+(1*n))
            n=n+1
    #Up/right Down/left -7
    n=1
    sub=num
    if num not in tb:
        if num not in rb:
            while n < 7:
                if sub-(7*n) in piece:
                    if clist[sub-7*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub-7*n,plist[sub-7*n],'-7'])
                        opmoves.append(sub-(7*n))
                        break
                    else:
                        break
                elif sub-(7*n) in tb:
                    opmoves.append(sub-(7*n))
                    break
                elif sub-(7*n) in rb:
                    opmoves.append(sub-(7*n))
                    break
                opmoves.append(sub-(7*n))
                n=n+1
    sub=num
    n=1
    if num not in lb:
        if num not in bb:
            while n < 7:
                if sub+(7*n) in piece:
                    if clist[sub+7*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub+7*n,plist[sub+7*n],'+7'])
                    
                        opmoves.append(sub+(7*n))
                        break
                    else:
                        break
                elif sub+(7*n) in lb:
                    opmoves.append(sub+(7*n))
                    break
                elif sub+(7*n) in bb:
                    opmoves.append(sub+(7*n))
                    break
                    
                opmoves.append(sub+(7*n))
                n=n+1
    #Up/left Down/right -9
    sub=num
    n=1
    if num not in tb:
        if num not in lb:
            while n < 7:
                if sub-(9*n) in piece:
                    if clist[sub-9*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub-9*n,plist[sub-9*n],'-9'])
                    
                        opmoves.append(sub-(9*n))
                        break
                    else:
                        break
                elif sub-(9*n) in tb:
                    opmoves.append(sub-(9*n))
                    break
                elif sub-(9*n) in lb:
                    opmoves.append(sub-(9*n))
                    break
                
                opmoves.append(sub-(9*n))
                n=n+1
    sub=num
    n=1
    if num not in rb:
        if num not in bb:
            while n < 7:
                if sub+(9*n) in piece:
                    if clist[sub+9*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub+9*n,plist[sub+9*n],'+9'])
                    
                        opmoves.append(sub+(9*n))
                        break
                    else:
                        break
                elif sub+(9*n) in rb:
                    opmoves.append(sub+(9*n))
                    break
                elif sub+(9*n) in bb:
                    opmoves.append(sub+(9*n))
                    break
                opmoves.append(sub+(9*n))
                n=n+1
    if forcheck==True:
        
        return phit
    
    if num in hiddenchecks:
        if ourcolor=='w':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('w')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
            
                
                
        if ourcolor=='b':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('b')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
                    
    return opmoves
def pmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    global enpassgiven
    sub=num
    ourcolor=clist[num]
    piece= findpieces()
    mooooo=[]
    wdm=[48,49,50,51,52,53,54,55]
    bdm=[8,9,10,11,12,13,14,15]
    phit=[[]]
    if ourcolor=='w':
        if (sub-8) not in piece:
            mooooo.append(num-8)
            if sub in wdm and (sub-16) not in piece:
                mooooo.append(num-16)
        if (sub-9) in piece and  clist[sub-9]!=ourcolor:
            if forcheck==True:
                phit.append([sub-9,plist[sub-9]])
            mooooo.append(num-9)
        if (sub-7) in piece and  clist[sub-7]!=ourcolor:
            if forcheck==True:
                phit.append([sub-7,plist[sub-7]])
            mooooo.append(num-7)
    if ourcolor=='b':
        if (sub+8) not in piece:
            mooooo.append(num+8)
            if sub in bdm and (sub+16) not in piece:
                mooooo.append(num+16)
        if (sub+9) in piece and  clist[sub+9]!=ourcolor:
            if forcheck==True:
                phit.append([sub+9,plist[sub+9]])
            mooooo.append(num+9)
        if (sub+7) in piece and  clist[sub+7]!=ourcolor:
            if forcheck==True:
                phit.append([sub+7,plist[sub+7]])
            mooooo.append(num+7)
     
    if enpass==True:
        enpassgiven=False
        if sndlastnum in bdm:
            if num==sndlastnum+17 or num==sndlastnum+15:
                enpassgiven=True
                mooooo.append(sndlastnum+8)
        elif sndlastnum in wdm:
            if num==sndlastnum-17 or num==sndlastnum-15:
                enpassgiven=True
                mooooo.append(sndlastnum-8)
        
    if num in bhiddencheckes or num in whiddencheckes:
        
        if ourcolor=='w':
            tplst=[]
            tclst=[]
            tempvar=0
            while tempvar<len(temppieces):
                tclst.append(clist[tempvar])
                tplst.append(plist[tempvar])
                tempvar=tempvar+1
            
            i=0
           
            while i<len(mooooo):
                plist[num]='p'
                clist[num]=ourcolor
                piece=plist[num]
                cou=clist[num]
                plist[mooooo[i]]=piece
                plist[num]=''
                clist[mooooo[i]]=cou
                clist[num]=''
                if incheck('w')==True:
                    mooooo.pop(i)
                    i=i-1
                i=i+1
            plist=[]
            clist=[]
            tempvar=0
            while tempvar<len(temppieces):
                clist.append(tclst[tempvar])
                plist.append(tplst[tempvar])
                tempvar=tempvar+1
            
                
                
        if ourcolor=='b':
            tplst=[]
            tclst=[]
            tempvar=0
            while tempvar<len(temppieces):
                tclst.append(clist[tempvar])
                tplst.append(plist[tempvar])
                tempvar=tempvar+1
            
            i=0
            while i<len(mooooo):
             
                pindhold=mooooo[i]
                cindhold=mooooo[i]
                pholder=plist[pindhold]
                cholder=clist[cindhold]
                plist[num]='p'
                clist[num]=ourcolor
                piece=plist[num]
                cou=clist[num]
                plist[mooooo[i]]=piece
                plist[num]=''
                clist[mooooo[i]]=cou
                clist[num]=''
                if incheck('b')==True:
                    updatechecks()
                   
                    mooooo.pop(i)
                    i=i-1
                
                plist[pindhold]=pholder
                clist[cindhold]=cholder
                
                i=i+1
                
            while tempvar<len(temppieces):
                clist.append(tclst[tempvar])
                plist.append(tplst[tempvar])
                tempvar=tempvar+1
    if forcheck==True:
        return phit

    return mooooo
def rmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    opmoves=[]
    sub=num
    ourcolor=clist[num]
    n=1
    piece= findpieces()
    phit=[[]]
    #Up down -8
    if num not in tb:
        while n<7:
            if sub-(8*n) in tb:
                opmoves.append(sub-(8*n))
                break
            if sub-(8*n) in piece:
                if clist[sub-8*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub-8*n,plist[sub-8*n],'-8'])
                    opmoves.append(sub-(8*n))
                    break
                break
            opmoves.append(sub-(8*n))
            n=n+1
    sub=num
    n=1
    if num not in bb:
        while n<7:
            if sub+(8*n) in bb:
                opmoves.append(sub+(8*n))
                break
            if sub+(8*n) in piece:
                if clist[sub+8*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub+8*n,plist[sub+8*n],'+8'])
                    opmoves.append(sub+(8*n))
                    break
                break
            opmoves.append(sub+(8*n))
            n=n+1
    #left right -1
    sub=num
    n=1
    if num not in lb:
        while n<7:
            if sub-(1*n) in lb:
                opmoves.append(sub-(1*n))
                break
            if sub-(1*n) in piece:
                if clist[sub-1*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub-1*n,plist[sub-1*n],'-1'])
                    opmoves.append(sub-(1*n))
                    break
                break
            opmoves.append(sub-(1*n))
            n=n+1
    sub=num
    n=1
    if num not in rb:
        while n<7:
            if sub+(1*n) in rb:
                opmoves.append(sub+(1*n))
                break
            if sub+(1*n) in piece:
                if clist[sub+1*n]!=ourcolor:
                    if forcheck==True:
                        phit.append([sub+1*n,plist[sub+1*n],'+1'])
                    opmoves.append(sub+(1*n))
                    break
                break
            opmoves.append(sub+(1*n))
            n=n+1
    if forcheck==True:
        return phit
   
    if num in hiddenchecks:
        if ourcolor=='w':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('w')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
            
                
                
        if ourcolor=='b':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('b')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst

    return opmoves
def kmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    bsr=[48,49,50,51,52,53,54,55]
    tsr=[8,9,10,11,12,13,14,15]
    lsr=[1,9,17,25,33,41,49,57]
    rsr=[6,14,22,30,38,46,54,62]
    rfr=[7,15,23,31,39,47,55,63]
    tfr=[0,1,2,3,4,5,6,7]
    bfr=[56,57,58,59,60,61,62,63]
    lfr=[0,8,16,24,32,40,48,56]
    piece=findpieces()
    
    ourcolor=clist[num]
    opmoves=[num+8,num -8,num+9,num-9,num +7, num-7,num+1,num-1]
    i=0
    phit=[[]]
    while i <len(opmoves):
        if forcheck==True:
            phit.append([i,plist[i]])
        if opmoves[i] in piece:
            if forcheck==True:
                phit.pop(len(phit)-1)
            if clist[opmoves[i]] == ourcolor:
                opmoves.pop(i)
                i=i-1
        i=i+1
    if forcheck==True:
        return phit
    
    if num in hiddenchecks:
        if ourcolor=='w':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('w')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
            
                
                
        if ourcolor=='b':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('b')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
    
    return opmoves
def bmoves(num,forcheck):
    global stage
    global clist
    global plist
    global wincheck
    global bincheck
    opmoves=[]
    sub=num
    ourcolor=clist[num]
    n=1
    piece= findpieces()
    phit= [[]]
    #Up/right Down/left -7
    if num not in tb:
        if num not in rb:
            while n < 7:
                if sub-(7*n) in tb:
                    opmoves.append(sub-(7*n))
                    break
                elif sub-(7*n) in rb:
                    opmoves.append(sub-(7*n))
                    break
                elif sub-(7*n) in piece:
                    if clist[sub-7*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub-7*n,plist[sub-7*n],'-7'])
                        opmoves.append(sub-(7*n))
                        break
                    else:
                        break
                opmoves.append(sub-(7*n))
                n=n+1
    sub=num
    n=1
    if num not in lb:
        if num not in bb:
            while n < 7:
                if sub+(7*n) in lb:
                    opmoves.append(sub+(7*n))
                    break
                elif sub+(7*n) in bb:
                    opmoves.append(sub+(7*n))
                    break
                elif sub+(7*n) in piece:
                    if clist[sub+7*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub+7*n,plist[sub+7*n],'+7'])
                        opmoves.append(sub+(7*n))
                        break
                    else:
                        break
                opmoves.append(sub+(7*n))
                n=n+1
    #Up/left Down/right -9
    sub=num
    n=1
    if num not in tb:
        if num not in lb:
            while n < 7:
                if sub-(9*n) in tb:
                    opmoves.append(sub-(9*n))
                    break
                elif sub-(9*n) in lb:
                    opmoves.append(sub-(9*n))
                    break
                elif sub-(9*n) in piece:
                    if clist[sub-9*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub-9*n,plist[sub-9*n],'-9'])
                        opmoves.append(sub-(9*n))
                        break
                    else:
                        break
                opmoves.append(sub-(9*n))
                n=n+1
    sub=num
    n=1
    if num not in rb:
        if num not in bb:
            while n < 7:
                if sub+(9*n) in rb:
                    opmoves.append(sub+(9*n))
                    break
                elif sub+(9*n) in bb:
                    opmoves.append(sub+(9*n))
                    break
                elif sub+(9*n) in piece:
                    if clist[sub+9*n]!=ourcolor:
                        if forcheck==True:
                            phit.append([sub+9*n,plist[sub+9*n],'+9'])
                        opmoves.append(sub+(9*n))
                        break
                    else:
                        break
                opmoves.append(sub+(9*n))
                n=n+1
    if forcheck==True:
        return phit
    
    if num in hiddenchecks:
        if ourcolor=='w':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('w')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
            
                
                
        if ourcolor=='b':
            tplst=plist
            tclst=clist
            i=0
            while i<len(opmoves):
                piece=plist[num]
                plist[opmoves[i]]=piece
                cou=clist[num]
                clist[opmoves[i]]=cou
                if incheck('b')==True:
                    opmoves.pop(i)
                    i=i-1
                i=i+1
            plist=tplst
            clist=tclst
    
    return opmoves
def boolst():
    i=0
    boo_lst=[]
    while i<64:
        boo_lst.append(False)
        i=i+1
    return boo_lst
init1=boolst()
def get_init():
    boo=True
    for single in init1:
        if single==False:
            boo=False
    return boo
def setinit(num):
    init1[num]=True
    print(init1)

def movestoredclist(moves):
    checker=checkerclist()
    for move in moves:
        if move>-1 and move<64:
            checker[move]= 'red'
    return checker
    
f1.root.mainloop()

