class ColorTextHandler:
    def __init__(self,style=0,base=40):
        self.ESCSEQ = '\033['
        self.style = str(style) #0-5
        self.base = str(base)+"m" #40-47

        self.blackstr = self.ESCSEQ+self.style+";30;"+self.base
        self.redstr = self.ESCSEQ+self.style+";31;"+self.base
        self.greenstr = self.ESCSEQ+self.style+";32;"+self.base
        self.yellowstr = self.ESCSEQ+self.style+";33;"+self.base
        self.bluestr = self.ESCSEQ+self.style+";34;"+self.base
        self.purplestr = self.ESCSEQ+self.style+";35;"+self.base
        self.cyanstr = self.ESCSEQ+self.style+";36;"+self.base
        self.whitestr = self.ESCSEQ+self.style+";37;"+self.base

    def black(self,txt): print(self.blackstr+txt+self.whitestr)
    def red(self,txt): print(self.redstr+txt+self.whitestr)
    def green(self,txt): print(self.greenstr+txt+self.whitestr)
    def yellow(self,txt): print(self.yellowstr+txt+self.whitestr)
    def blue(self,txt): print(self.bluestr+txt+self.whitestr)
    def purple(self,txt): print(self.purplestr+txt+self.whitestr)
    def cyan(self,txt): print(self.cyanstr+txt+self.whitestr)
    def white(self,txt): print(self.whitestr+txt+self.whitestr)

