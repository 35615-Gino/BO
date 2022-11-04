import time


def vraag1():
    time.sleep(1)
    print("Jouw wereld is in groot gevaar door het klimaat en een zwart gat. Wat ga je doen")
    time.sleep(1)
    answer = input("A:verzamel allerlei spullen. B: wacht tot het eind ").lower()
    if answer == "a":
            time.sleep(1)
            print("je verzamelt alle spullen en zet het in de raket")
            vraag3()
    elif answer == "b":
            time.sleep(1)
            print("Doe niks en wacht maar de raket staat wel klaar")
            vraag2()
    else:
            time.sleep(1)
            print("antwoord met A of B")
            vraag1()
    


def vraag2():
    time.sleep(1)
    print("Doe niks en wacht maar de raket staat wel klaar")
    time.sleep(1)
    answer = input("wat ga je doen, A:verzamel allerlei spullen. B: wacht tot het eind ").lower()
    if answer == "a":
            time.sleep(1)
            print("je bleef thuis en langzaam is je planeet opgezogen")
            Einde1()
    elif answer == "b":
            time.sleep(1)
            print("je gaat de raket toch wel in")
            vraag4()
    else:
            time.sleep(1)
            print("antwoord met A of B")
            vraag2()

    
def vraag3():
    time.sleep(1)
    print("je bent klaar en gaat de raket in. er is een fout. ")
    time.sleep(1)
    while True:
        answer = input("A: fixt het en gaat of B: je laat het ").lower()
        if answer == "a":
            time.sleep(1)
            print("A: Je zit in de raket en gaat nu de ruimte in")
            vraag4()
        elif answer == "b":
            time.sleep(1)
            print("je gaat de lucht in en de raket explodeert")
            Einde4()
        else:
            time.sleep(1)
            print("antwoord met A, B of C")
            vraag3()
    

def vraag4():
    time.sleep(1)
    print(" langzaam gaat de spullen op , wat ga je doen? ")
    time.sleep(1)
    while True:
            answer = input("A: je bespaart het B: je verspilt het ").lower()
            if answer == "a":
                time.sleep(1)
                print("je koos ervoor om je spullen te besparen en langzaam reis je door een wormgat")
                vraag8()
            elif answer == "b":
                time.sleep(1)
                print(" je koos ervoor om je spullen te verspillen en langzaam reis je door een wormgat")
                vraag5()
            else:
                time.sleep(1)
                print("antwoord met A, B of C")   
                vraag4() 
              

def vraag5():
    time.sleep(1)
    print("")
    time.sleep(1)
    answer = input(" langzaam gaan alle spullen die je hebt op, wat ga je doen?").lower()    
    if  answer == ("a"):         
        print ("rustig verlaat je het wormgat en gaat langzaam naar een planeet")   
        vraag6()
    elif answer == ("b"):
        print ("rustig verlaat je het wormgat en gaat langzaam naar een planeet")
        vraag7()
    else:
        print ("Not a option")       
        vraag5()  


def vraag6():
    time.sleep(1)
    print(" je valt snel")  
    time.sleep(1)
    answer = input("A:wacht tot inpact B: drop wat gewicht").lower() 
    if  answer==("a"):         
        print ("je ligt gewond op de grond en bent gepakt (in Amerika)")   
        vraag9()
    elif answer==("b"):
        print ("je landt heel veilig  in Amerika en er zijn mensen die buiten wachten")    
        vraag18()
    else:         
        print ("Not a option")  
        vraag6()         

def vraag7():
    time.sleep(1)
    print("er brak een gat in het schip")  
    time.sleep(1)
    answer = input("A:  laat het liggen B: blokkeer het gat in het schip ").lower() 
    if  answer==("a"):         
        print ("het ging niet bepaald goed") 
        vraag11()
    elif answer==("b"):
        print ("je laat het staan met hoe het is")  
        vraag10()
    else:         
        print ("Not a option")        
        vraag7()   

def vraag8():
    time.sleep(1)
    print("alle spullen zijn op")  
    time.sleep(1)
    answer = input("de spullen zijn op").lower() 
    if  answer==("a"):         
        print (" rustig verlaat je het wormgat en gaat langzaam naar een planeet")   
        vraag6()
    elif answer==("b"):
        print (" je zuurstof gaat te snel op.")     
        Einde4()
    else:         
        print ("Not a option")          
        vraag8()

def vraag9():
    time.sleep(1)
    print("je bent wakker en ziet een bewaker.")  
    time.sleep(1)
    answer = input("A: doe niks B: val aan").lower() 
    if  answer==("a"):         
        print ("ze hebben je en ze doen testen")   
        vraag20()
    elif answer==("b"):
        print ("je doet agressief en het gaat fout. je wordt neergeschoten")   
        Einde4()  
    else:         
        print ("Not a option")      
        vraag9()      

    
def vraag10():
    time.sleep(1)
    print("het ging goed en het is stabiel, wat ga je doen?")  
    time.sleep(1)
    answer = input("A: laat staan wat er is B: zet meer objecten neer").lower() 
    if  answer==("a"):         
        print ("het opende en je bent eruit gezogen")   
        Einde2()
    elif answer==("b"):
        print ("ga naar 18")     
        vraag18()
    else:         
        print ("Not a option")   
        vraag10()

def vraag11():
    time.sleep(1)
    print(" het brak een groter gat in het voertuig")  
    time.sleep(1)
    answer = input("A: zet het dicht B: stres en doe niks").lower() 
    if  answer==("a"):         
        print ("ga naar 18")   
        vraag18()
    elif answer==("b"):
        print ("je valt eruit en je bent de klote")     
        Einde2()
    else:         
        print ("Not a option")     
        vraag11()       

def vraag12():
    time.sleep(1)
    print("het doet pijn en je doet een beetje agressief")  
    time.sleep(1)
    answer = input(":A: doe niks terug B: bijt een wetenschapper").lower() 
    if  answer==("a"):         
        print (" je zit terug in je cel en ziet een weg uit") 
        vraag19()  
    elif answer==("b"):
        print ("je zit langer vast")     
        vraag13()
    else:         
        print ("Not a option")    
        vraag12()  

def vraag13():
    time.sleep(1)
    print("je begint langzaam aan iets te denken om weg te gaan, wat ga je doen?")  
    time.sleep(1)
    answer = input("A: verzin een plan B: je blijft").lower() 
    if  answer==("a"):         
        print ("je wacht tot ze weg zijn en er liggen spullen")  
        vraag16()
    elif answer==("b"):
        print ("je wacht tot ze weg zijn en er liggen spullen")     
        vraag16()
    else:         
        print ("Not a option")         
        vraag13()   

def vraag14():
    time.sleep(1)
    print("je doet niks en dat vinden ze blijkbaar niet super leuk")  
    time.sleep(1)
    answer = input("A: doe dom B: blijf niks doen totdat ze boos worden").lower() 
    if  answer==("a"):         
        print ("je was niet zo slim en deed niet super leuk voor hum")   
        Einde4()
    elif answer==("b"):
        print ("je was niet zo slim en deed niet super leuk voor hum")  
        Einde4()
    else:         
        print ("Not a option")   
        vraag14()         

def vraag15():
    time.sleep(1)
    print("je rent naar buiten en er zijn mensen")  
    time.sleep(1)
    answer = input("A: verstop en ren later B: neem de risico ").lower() 
    if  answer==("a"):         
        print ("je hebt gewacht tot het moment dat ze weg liepen, ga naar 19")   
        vraag19()
    elif answer==("b"):
        print ("het ging fout en werd gepakt")     
        Einde3()
    else:         
        print ("Not a option")  
        vraag15()          

def vraag16():
    time.sleep(1)
    print("je weet wat je ermee kan doen, maar dit is niet het perfecte moment.")  
    time.sleep(1)
    answer = input("A: laat liggen B: gebruik ze C: doe niks").lower() 
    if  answer==("a"):         
        print ("Je breekt uit de cel wanneer iedereen weg is")   
        vraag17()
    elif answer==("b"):
        print ("Je breekt uit de cel wanneer iedereen weg is")
        vraag15()
    elif answer==("c"):
        print ("je doet niks en dat vinden ze blijkbaar niet super leuk")
        vraag14()
    else:         
        print ("Not a option")            

def vraag17():
    time.sleep(1)
    print("je loopt door de gangen van Area 51")  
    time.sleep(1)
    answer = input("A: kijk rond B: ga naar buiten C:bezorg chaos").lower() 
    if  answer==("a"):         
        print ("je keek rond en er was een bewaker")
        Einde3()   
    elif answer==("b"):
        print (" het ging fout en je bent gepakt") 
        Einde3()    
    elif answer==("c"):
        print ("dit was een grote fout en de bewaker richt een geweer op je.") 
        Einde4()
    else:         
        print ("Not an option")   
        vraag17()  

def vraag18():
    time.sleep(1)
    print("je bent gepakt dus wat doe je?")  
    time.sleep(1)
    answer = input("A: stres en val aan B:doe mee").lower() 
    if  answer==("a"):         
        print ("e bent dood") 
        Einde4()  
    elif answer==("b"):
        print ("je doet rustig mee en wordt langzaam op getest")  
        vraag12()   
    else:         
        print ("Not a option")  
        vraag18()         

def vraag19():
    time.sleep(1)
    print("je weet niet echt wat je moet gaan doen,")  
    time.sleep(1)
    answer = input("A: ren zonder plan B: ren weg met plan").lower() 
    if  answer==("a"):         
        print ("je bent vrij en weg van Area 51") 
        vraag21()
    elif answer==("b"):
        print ("je bent gepakt")     
        Einde3()
    else:         
        print ("Not a option")   
        vraag19()        

def vraag20():
    time.sleep(1)
    print("ze hebben je en ze doen testen")  
    time.sleep(1)
    answer = input("maakt niet uit wat je doet").lower() 
    if  answer==("a"):         
        print ("oof")   
        Einde3()
    elif answer==("b"):
        print ("oof")
        Einde3()     
    else:         
        print ("Not a option")  


def vraag21():
    time.sleep(1)
    print("je komt een onbekende tegen, wat ga je doen?")  
    time.sleep(1)
    answer = input("A: ga met hem mee of B:ga niet mee").lower() 
    if  answer==("a"):         
        print ("je bent gered!!!!")
        Einde1()   
    elif answer==("b"):
        print ("je bent gepakt")
        Einde3()     
    else:         
        print ("Not a option")  
        vraag21()       

def Einde1():
    print("Gefeliciteerd je bent nu beste vrienden met Elon Musk")

def Einde2():
    print("vast in de ruimte")

def Einde3():
    print("jammer je zit vast in Area 51 en je kan er niet uit komen")    

def Einde4():
    print("je bent dood gegaan")