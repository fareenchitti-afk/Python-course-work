#.OOPs
class Instagram:
    settings=['Ins', 'Sta', 'Pri']

    @classmethod
    def settingsupdate(cls):
        print(cls.settings)

    @staticmethod
    def welcome():
        print("Welcome to the Instagram. Have Fun!!!")

    def userdetails(self,username,password,bio=''):
        self.username=username
        self.password=password
        self.bio=bio
        print(f"Hello {self.username}\nWelcome to the Instagram.Have Fun!!!")
    
fareen = Instagram()
aara = Instagram()
fareen.userdetails("fareen","r@123")
aara.userdetails("aara","a@124","My life my rules")
print(fareen.username)
print(fareen.password)
print(fareen.bio)
print(fareen.settings)
print(Instagram.settings)

print(aara.username)
print(aara.password)
print(aara.bio)



fareen.settingsupdate()
Instagram.settingsupdate()

fareen.welcome()
Instagram.welcome()


#.Constractor
class Instagram:
    def __init__(self,username,pwd):
        self.username=username
        self.password=pwd
        self.bio=''
        self.followers={}
        self.following={}
        print("Welcome to the Instagram. Have Fun!!!")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

fareen = Instagram("Fareen","r@123")

#.public
class Instagram:
    def __init__(self,username,pwd):
        self.username=username
        self.__password=pwd
        self._post=[]

fareen = Instagram("Fareen","r@123")
print(f"Before: {fareen.username}")
fareen.username="aara"
print(f": After: {fareen.username}")
 
#.protected
class Instagram:
    def __init__(self,username,pwd):
        print("Welcome to the Instagram.Have Fun!!!")
        self.username = username
        self.__password = pwd
        self.__post = []
    def getPassword(self):
        return self.__password

    def setPassword(self,newPassword):
       self.__password = newPassword
       print("Password Updated")
       
    @property
    def viewPost(self):
        return self.__post

    @viewPost.setter

    def viewPost(self,post):
        self.__post.append(post)

fareen = Instagram("Fareen","r@123")
print(f"Before: {fareen.username}")
fareen.username="aara"
print(f"After: {fareen.username}")

print(f"Before: {fareen.getPassword()}")
fareen.setPassword("aara@234")
print(f"After: {fareen.getPassword()}")

print(fareen.viewPost)
fareen.viewPost = "hello"
fareen.viewPost = "First Reel"
print(fareen.viewPost)





