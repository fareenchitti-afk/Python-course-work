#.single inheritance

class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")
fareen = Whatsapp_v1()
print("Fareen- v1") 
fareen.sharepics()

#.Multi level inheritance(parent class to child class)

class Whatsapp_v1:
    def messaging(self):
        print("You can message")

    def sharepics(self):
        print("You can share the photos")


class Whatsapp_v2(Whatsapp_v1):
    def messaging(self):
        print("You can message")

    def status(self):
        print("You can share the photos")
    def videos(self):
        print("You can share the videos")


class Whatsapp_v3(Whatsapp_v2):
    def messaging(self):
        print("You can message")

    def status(self):
        print("You can share the photos")
    def group(self):
        print("You can create a group")
    def calls(self):
        print("You can do video and audio calls")


class Community:
    def clubgroup(self):
        print("You can create a community with clubing the group")

class Meta:
    def ai(self):
        print("You can chat, generate images and genarate videos")

class Meta:
    def chat(self):
        print("You can chat")

class Meta1(Meta):
    def ai_images(self):
        print("You can generate images")

class Meta2(Meta):
    def human_emotions(self):
        print("You can share you feelings")

class Meta3(Meta1,Meta2):
    def technical(self):
        print("You can ask technical Question also. Meta Can provide all kind of things")



class Whatsapp_v4(Whatsapp_v3,Community,Meta3): #. single child multiple parents
    def channel(self):
        print("You can create channel to engage with your followers")
    def status(self):
        print("You can share the photos")
    def group(self):
        print("You can create a group")
    def calls(self):
        print("You can do video and audio calls")
    def videos(self):
        print("You can share the videos")
    def sharepics(self):
        print("You can share the photos")   
    def messaging(self):
        print("You can message")



        

fareen = Whatsapp_v1()
print("Fareen- v1")
fareen.messaging()
fareen.sharepics()

priya = Whatsapp_v2()
print("\n\npriya- v2")
priya.messaging()
priya.status()
priya.videos()

rama = Whatsapp_v3()
print("\n\nrama- v3")
rama.messaging()
rama.status()
rama.group()
rama.calls()

aara = Whatsapp_v4()
print("\n\aara- v4")
aara.messaging()
aara.status()
aara.group()
aara.calls()
aara.sharepics()
aara.videos()
aara.channel()
aara.clubgroup()
aara.chat()
aara.ai_images()
aara.technical()
aara.human_emotions()

#.Super method
class Whatsapp_v1:
    def status(self):
        print("Upload picture and video with limited duration")

fareen = Whatsapp_v1()
fareen.status()


#.Super key(use)

class Whatsapp_v1:
    def status(self):
        print("Upload picture and video with limited duration")


class Whatsapp_v2(Whatsapp_v1):
    def status(self):
        super().status()
        print("You can like the status and mention your friends")

fareen = Whatsapp_v2()
fareen.status()

#.1

class Whatsapp_v1:
    def status(self):
        print("Upload picture and video with limited duration")


class Whatsapp_v2:
    def status(self):
        print("You can like the status and mention your friends")

class Whatsapp_v3(Whatsapp_v1,Whatsapp_v2):
    def status(self):
        super().status()
        super().status()
        print("You can add music and share it on cross platform")
        

fareen = Whatsapp_v3()
fareen.status()        







    
                
