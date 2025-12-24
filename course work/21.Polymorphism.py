#.Overriding
class HotStar:
    def __init__(self,username):
        print(f"Hi {username} Welcome to the HotStar".center(40,'-'))
                                                            
                                                        
    def playvideo(self):
        print("Movie with Ads")
        print("Limited access for movies")
        print("Quality is limited")
        print("One device login")
        print("No download option")
        print("No live access")
        print("Sound Quality reduces")

    def login(self):
        print("Login is same")
    def interface(self):
        print("Same interface")
    def profile(self):
        print("Profile is same")

class PremiumUser(HotStar):
    def __init__(self,username):
        print(f" Hi {username} enjoy your premium".center(60,'-'))

        
    def playvideo(self):
        print("Movie without Ads")
        print("UnLimited access for movies")
        print("Quality is high")
        print("Multiple device login")
        print("Download option is available")
        print("live access")
        print("Improved Sound Quality")

fareen=HotStar("fareen")
fareen.playvideo()
fareen.login()

rama=PremiumUser("rama")
rama.playvideo()
rama.login()

#.Instagram

class Instagram:
    def feed(self):
        print("Feed is same for all")
    def scrolling(self):
        print("Scrolling is same for all")
    def share(self):
        print("Share is same for all")
    def like(self):
        print("Like is same for all")
    def share(self):
        print("Share is same for all")
    def repost(self):
        print("Repost is same for all")
    def comment(self):
        print("Comment is same for all")
    def profile(self):
        print("NO Professional dashboard")
    def posting(self):
        print("No insights are available")

class creator(Instagram):
    def profile(self):
        print("Professional dashboard is adding in their grid")
    def posting(self):
        print("You can  see the reach, profile acitivies all")

priya=creator()
priya.profile()
priya.posting()

bindu=Instagram()
bindu.profile()
bindu.posting()

#.Overloding

class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,other):
        return self.num+other.num

n1=Number(10)
n2=Number(20)

print(n1+n2)



        
