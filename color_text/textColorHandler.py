class ColorTextHandler:
    def __init__(self,style=0,base=40):
        self.ESCSEQ = '\033['
        self.style = str(style) #0-5
        self.base = str(base)+"m" #40-47

        self.black = self.ESCSEQ+self.style+";30;"+self.base
        self.red = self.ESCSEQ+self.style+";31;"+self.base
        self.green = self.ESCSEQ+self.style+";32;"+self.base
        self.yellow = self.ESCSEQ+self.style+";33;"+self.base
        self.blue = self.ESCSEQ+self.style+";34;"+self.base
        self.purple = self.ESCSEQ+self.style+";35;"+self.base
        self.cyan = self.ESCSEQ+self.style+";36;"+self.base
        self.white = self.ESCSEQ+self.style+";37;"+self.base

Cth = ColorTextHandler()
print(Cth.red+"Helow World"+Cth.black+" World"+Cth.white)