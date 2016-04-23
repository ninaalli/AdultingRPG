class View(object):
    #interaction with the user
    """docstring for View"""
    def __init__(self, arg):
        super(View, self).__init__()
        self.arg = arg

    def Welcome_to_Adulting(self):
        print ("Welcome to the world of adulting where you get to do all of everything for yourself. All those times you wished you could stay out late, now you can! Buy that radio flyer! Do everything you wanted to do! Make that money and spend it without ending up in debt or back in mommy and daddy's basement.")

    def login_or_registereduser(self):
        while True: #caps mean built in fx
            print ("login [0]") #if printing something they enter add ""
            print ("register [1]")
            choice = input ("Welcome! Are you a new or returing user?")
            if choice in ["0","1"]: #this limits them to these options
                                    #the colon tells the program you are done with the statement
                break #this will stop loop
        return int(choice) #not in quotes, bc its an input, not a variable

    def incorrect_login(self):
        print ("PBCK Error - please try again")

    def input_user_name(self):
        while True:
            name= input ("Please enter your name:  ")
                if name != ""
                #"" means empty
                break
        return name

    def occupation(self):
        while True:
            occupation= input ("Dreamjob:  ")
                if occupation != ""
                #"" means empty
                break
        return occupation

    def marital_status(self):
        while True: #caps mean built in fx
            print ("single [0]") #if printing something they enter add ""
            print ("married [1]")
            print ("significant other [2]")
            print ("it's complicated [3]")
            choice = input ("")
            if choice in ["0","1","2","3"]: #this limits them to these options
                                    #the colon tells the program you are done with the statement
                break #this will stop loop
        return int(choice) #not in quotes, bc its an input, not a variable

    def gender(self):
        while True:
            print ("nunya [0]") #if printing something they enter add ""
            print ("male [1]")
            print ("female [2]")
            print ("trans-m2f [3]")
            print ("trans-f2m [4]")
            choice = input ("")
            if choice in ["0","1","2","3","4"]: #this limits them to these options
                                    #the colon tells the program you are done with the statement
                break #this will stop loop
        return int(choice) #not in quotes, bc its an input, not a variable

    def age(self):
        while True:
            age=input ("Whats my age again?:  ")
                if age != ""
                #"" means empty
                break
        return int(age)

    def success(self):
        print ("You did it!!! w00t w00t High-Five!")

    def failure(self):
        print ("Looks grim friend. You don't want to end up couch surfing or back with mom and dad.")

    
#if putting pass, python will think you can pass
#daily adulting questions
