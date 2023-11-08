books={ "sadsaltanhayi":10 , "bighane": 8 , "becoming": 30 , "almond": 5 ,
       "bofekor":22 , "emma":14 , "lord of rings":2 , "razkhorshid": 7 , "dezire": 9}
class student:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def kharid(self):
        sum=0
        x=input("che ketabayi mikhay?").split()
        for i in x:
            if i in books.keys():
                global y
                y=int(input("chand ta mikhay?"))
                if y>5 :
                    print("bish tar az panj ta ghabel gerftan nist")
                elif y<=books[i]:
                    print("mojod darim")
                    books[i]=books[i]-y
                    sum=sum+y
                else :
                    print("mojod nadarim")
    def payment(self):
        print("soart hesab shoma", sum*10 , "ast")
        payment=int(input("pol ketab:"))
        while payment!=sum*10:
            payment=int(input("pol eshtebah bood dobare vared kon"))
    def marjoii(self):
        marjoi=int(input("agar mikhay pass bedy(gharz) 1 bezan agar mikhay bargardony 0 ro vared kon"))
        if marjoi==1:
            bazgasht=input("esm ketabayi ke mikhay pass bedi ro vared kon").split()
            for i in range (0,len(bazgasht)):
                if bazgasht[i] in books.keys():
                    print(bazgasht[i],"movafagh bood")
                    x=int("chand ta mikhay barghardoni?")
                    books[bazgasht[i]]+=x
                    modat=int("chand rooz ketab daset bood")
                    if modat>30 :
                        print("bayad jarime bedi")
                        modat=modat-30
                        print("bayad jarime bedi",modat*10)
                        jarime=input(int("hazine ro vared kon"))
                        while jarime!=modat*10:
                            jarime=int(input("pol eshtebah bood dobare vared kon"))
        if marjoi==0:
            sum=0
            bazgasht=input("esm ketabayi ke mikhay bargardoni ro vared kon").split()
            for i in range (0,len(bazgasht)):
                if bazgasht[i] in books.keys():
                    print(bazgasht[i],"movafagh bood")
                    x=int("chand ta mikhay barghardoni?")
                    books[bazgasht[i]]+=x
                    sum+=x
            print("hasineye bargashti", sum*10)
class staff:
    def __init__(self,name,lastname,age):
        self.name=name
        self.lastname=lastname
        self.age=age
    def addon(self):
        for i in range (0,len(books.values())):
            x=list(books.items())
            if x[i][1]==0:
                taiid=int(input("darkhast baraye ketab",x[i][0],"chand ta mikhay? "))
                books[x[i][0]]+=taiid
name=input("enter your name ")
lastname=input("enter your lastname ")
age=int(input("enter your age "))
student1=student(name,lastname,age)
x=input("chy mikhay? kharid , marjoii , amanat")
if x=="kharid":
    student1.kharid()
    student1.payment()
elif x=="amanat":
    student1.kharid()
elif x=="marjoii":
    student1.marjoii()
else :
    print("khodahafz")

staff1=staff("mmd","mmdi",25)
staff1.addon()
