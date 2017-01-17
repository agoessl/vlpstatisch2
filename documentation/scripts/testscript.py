import random as r

myTitleList = ["Balances",
               "Plant Breeding",
               "Artificial Respiration"]
               
myHeaderList = ["Hydrostatic balance", 
                "Rümker's balance for grain",
                "Treshingmashine",
                "Machines",
                "A pair of Bellows "]
                
myFigcaptionList = ["Hydrostatische Waage", 
                    "Rümkersche Körnerwaage",
                    "Strube- Schlanstedt: Ausdreschen der Vermehrungsparzellen des Zuchtgartens mittels einer Spezialdreschmaschine",
                    "Heine-Hadmersleben, Apparate",
                    "Blasebalg"]
                    
mySourceList = ["Gscheidlen, Richard. 1876. Physiologische Methodik: Ein Handbuch der Praktischen Physiologie. Braunschweig: Vieweg & Sohn", 
                    "Hillmann, Paul. 1910. Die deutsche landwirtschaftliche Pflanzenzucht. Berlin: Deutsche Landwirtschafts-Gesellschaft"]
                
myPeopleList = ["Ludwig, Carl [Karl] Friedrich Wilhelm (1816-1895)",
                "Hering, Karl Ewald Konstantin (1834-1918)"]

myImageList = ["img4439.jpg",
                "img4407.jpg",
                "img26820.jpg",
                "img26707.jpg",
                "img26678.jpg",
                "img4748.jpg"]
                
mySitesList = ["Physiological Institute, University of Leipzig (1877)",
               "Physiological Institute, University of Leipzig (1909)"]

myLiteratureList = []

myCommentList = [] 

for i in range(10):
    print ("+++")
    myHeader = (myHeaderList[r.randint(0, len(myHeaderList)-1)])
    print ("header = " + myHeader)
    myImage = (myImageList[r.randint(0, len(myImageList)-1)])
    print ("<img src='images/" + myImage + ">")
    print ("+++")
    print ("")
