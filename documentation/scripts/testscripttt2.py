# Script für Perl Template Toolkit
import random as r
import datetime as dt

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

myImageList = ["img4439",
                "img4407",
                "img26820",
                "img26707",
                "img26678",
                "img4748"]
                
mySitesList = ["Physiological Institute, University of Leipzig (1877)",
               "Physiological Institute, University of Leipzig (1909)"]

myLiteratureList = ["Aeby, Christoph. 1862. Untersuchungen über die Fortpflanzungsgeschwindigkeit der Reizung in der quergestreiften Muskelfaser. Braunschweig: George Westermann", "Lange, Carl. 1887. Ueber Gemüthsbewegungen. Eine psycho-physiologische Studie. Leipzig: Thomas", "Westphal, Rudolf. 1865. Geschichte der alten und mittelalterlichen Musik. Breslau: F. E. C. Leuckart (Staatliches Institut für Musikforschung)"]

myCommentList = ["In the late 1840s, the pathologist Rudolf Virchow recognized that most of the cells in the brain could be categorized into two distinct groups.", "By 1900 neuroscientists had established the image of a neural-network brain, whereas their knowledge about glial cells was still at the level of 'nerve glue.", "Przybyszewski, who was one of Waldeyer's students, made his literary debut in 1892 with Zur Psychologie des Individuums (The Psychology of the Individual).", "According to Przybyszewski, one effect of excess in the brain caused by inhibition is a pathologically increased sensitivity."] 

myNow = dt.datetime.now()
myDay = str(myNow.day).rjust(2, "0")
myMonth = str(myNow.month).rjust(2, "0")
myYear = str(myNow.year)
myDate = myYear + "-" + myMonth + "-" + myDay

myContent = """<div class="topsection">	
	<div class="figure">
        <img src="./images/[% template.image %].jpg" width="auto" height="auto" class="fig" />"
		<p class="figcaption">[% template.figcaption %]</p>		
	</div>	
	<div class="head">
		<h1>[% template.title %]</h1>
	 </div> <br clear="all" />
</div> <!-- topsection -->

<table>
	<tr>
		<th>Source</th>
		<td>
			[% template.source %]
		</td>
	</tr><tr>
			  <th>People</th><td>[% template.people %]</td>
	</tr><tr>
			  <th>Sites</th><td>[% template.sites %]</td>
	</tr><tr>
			  <th>Related Literature</th><td>[% template.literature %]</td>
	</tr><tr>
			  <th>Comment</th><td>[% template.comment %]</td>
	</tr><tr>
			  <th>Description</th><td>[% template.title %]</td>
	</tr>
				
</table>"""

print(myDate)

for i in range(1000):
    dateihandle =           open("/Users/admin/Documents/git/vlp/vlpstatisch2/vlptt2/templates/src/" + str(i+1).rjust(4, "0") + ".html", "w")
    myTitle = "VLP" + str(i+1).rjust(4, "0")
    dateihandle.write("[% META title = \"" + myTitle + "\"\n")
    dateihandle.write("\t\tdate = \"" + myDate + "\"\n")
    myHeader = (myHeaderList[r.randint(0, len(myHeaderList)-1)])
    dateihandle.write("\t\theader = \"" + myHeader + "\"\n")
    myFigcaption = (myFigcaptionList[r.randint(0, len(myFigcaptionList)-1)])
    dateihandle.write("\t\tfigcaption = \"" + myFigcaption + "\"\n")
    mySource = (mySourceList[r.randint(0, len(mySourceList)-1)])
    dateihandle.write("\t\tsource = \"" + mySource + "\"\n")
    myPeople = (myPeopleList[r.randint(0, len(myPeopleList)-1)])
    dateihandle.write("\t\tpeople = \"" + myPeople + "\"\n")
    mySite = (mySitesList[r.randint(0, len(mySitesList)-1)])
    dateihandle.write("\t\tsites = \"" + mySite + "\"\n")
    myLiterature = (myLiteratureList[r.randint(0, len(myLiteratureList)-1)])
    dateihandle.write("\t\tliterature = \"" + myLiterature + "\"\n")
    myComment = (myCommentList[r.randint(0, len(myCommentList)-1)])
    dateihandle.write("\t\tcomment = \"" + myComment + "\"\n")
    myImage = (myImageList[r.randint(0, len(myImageList)-1)])
    dateihandle.write("\t\timage = \"" + myImage + "\"\n" )
    dateihandle.write("%]\n\n")
    dateihandle.write(myContent)
    dateihandle.close()
    

