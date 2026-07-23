class youtubers:
    count=0
    total_sub=0
    def __init__(self,name,type,subscribers):
        self.name=name
        self.type=type
        self.subscribers=subscribers
        youtubers.count +=1
        youtubers.total_sub+=subscribers


    def info(self):
        print(f"{self.name} is of {self.type}")

    @classmethod
    def count_youtubers(cls):
        return f"total numbers of yt={cls.count}"
    @classmethod
    def total_subs(cls):
            return f"total subscribers of yt={cls.total_sub}"
    
yt1=youtubers("live insaan","gaming",20)
yt2=youtubers("trigerred insaan","roasting",30)
yt3=youtubers("bro code","education",1)
yt1.info()
yt2.info()
yt3.info()
print(youtubers.total_subs())
print(youtubers.count_youtubers())