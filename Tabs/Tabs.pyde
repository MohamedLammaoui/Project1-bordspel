#screensize:
screen_xSize = 1200
screen_ySize = 800
buttonWidth = 12.5
buttonHeight = 5
tabs = [0, 1, 2, 3, 4]
tabNames = ['Spel overzicht', 'Dueleren', 'Rad', 'Kaartregels', 'Namen']
spelerNamen = {"speler1":"", "speler2":"", "speler3":"", "speler4":""}
activeTab = 0
kaart = []
selected_field = None

def draw_bg(x, screen_xSize, screen_ySize):
    redraw()
    x.resize(screen_xSize, screen_ySize)
    x = background(x)
    return x

def active(tab):
    global screen_xSize, screen_ySize, buttonWidth
    fill(255,255,0)
    stroke(150)
    rect(50+(tab*150), 10, 125, 50, 10)
    noFill()


def fonts(font_type,font_size, state):
    return textFont(createFont(font_type,font_size, state))



def OverzichtGegevens():
    fill(0)
    #code
    noFill()


def Duel():
    fill(0)
    #code
    noFill()


    

def Rad1():
    fill(150)
    # code
    noFill()

    
def Kaartregels():
    global kaart, screen_xSize, screen_ySize
    card_width =  150 #150 px width card
    card_height = 250 #250 px height card
    cardText_width =  133 #5 px margin from x start x position ,card 133px
    cardText_height = 195 #40 px margin from y position,card 195px
    left_margin= screen_xSize/100*25 #margin from left 25%
    card = 0
    for yRow in range(4):
        for xRow in range(5):
            if card < 13:
                # left_margin/2 = 150px
                image(kaart[card],left_margin/2 + (xRow*card_width), 100 +(card_height*yRow))
                card+=1

    fill(140,0,0)
    fonts("Arial Bold Italic", 14, True)
    textAlign (LEFT)
    # text box with auto wrap (x,y, from x, from y)
    Aas = "Een pion uit het startveld op eigen startpositie (vlag icoontje) zetten of een pion 1 plaats vooruit zetten." 
    text(Aas, left_margin/2 + 5 + (cardText_width*0), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Twee = "Bij deze kaart moet je je pion twee stappen vooruit zetten."
    text(Twee, left_margin/2 + 22 + (cardText_width*1), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    Drie = "Bij deze kaart moet je je pion drie stappen vooruit zetten."
    text(Drie, left_margin/2 + 22 + (cardText_width*2), 100 + (cardText_height*0)+40 , cardText_width-11, cardText_height-40)
    # Vier = "Bij deze kaart moet je je pion vier stappen achteruit zetten." 
    # text(Vier,left_margin/2 + cardText_width*4, cardText_height*4, 128, 155)
    # Vijf = "Bij deze kaart moet je je pion vijf stappen vooruit zetten."
    # text(Vijf,left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    
    # Zes = text("Bij deze kaart moet je je pion zes stappen vooruit zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Zeven = text("Bij deze kaart kan je je pion zeven stappen vooruit zetten of splietsen over twee pionnen.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Acht = text("Bij deze kaart moet je je pion acht stappen vooruit zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Negen = text("Bij deze kaart moet je je pion negen stappen vooruit zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Tien =  text("Bij deze kaart moet je je pion tien stappen vooruit zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Boer = text("Een eigen pion met een pion van een andere speler omruilen.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Vrouw = text("Een pion twaalf plaatsen vooruit zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    # Heer = text("Een pion uit het startveld op eigen startpositie(vlag icoontje) zetten.",left_margin/2 + cardText_width*1, cardText_height*1, 128, 155)
    noFill()


def Names():
    global spelerNamen
    
    def field_colors(field):
        if field == 1: return fill(255,0,0)
        if field == 2: return fill(0,255,0)
        if field == 3: return fill(50,70,255)
        if field == 4: return fill(255,255,0)
        
    textAlign(CENTER)
    stroke(0,0,0)
    fill(0,0,0)
    rect(90,120,508,20)
    fill(255,255,255)
    fonts("Arial Bold", 18, True)
    text("Vul uw naam hier onder in:", 200, 120, 398,25)
    noFill()
    noStroke()
    
    fonts("Arial", 16, True)
    for x in range(len(spelerNamen)):
        stroke(0,0,0)
        field_colors(x+1)
        rect(90, 140+(x*20), 108, 20)  #column 1
        fill(255,255,255)
        rect(198, 140+(x*20), 400, 20) #column 2
        noFill()
        noStroke()

    for x in range(len(spelerNamen)):
        fill(0,0,0)
        textAlign(LEFT)
        text("speler" + str(x+1), 100, 155+(x*20))
        text(str(spelerNamen["speler"+str(x+1)]), 200, 155+(x*20))
        noFill()

def setup():
    global screen_xSize, screen_ySize
    global kaart
    global bg_img
    size(screen_xSize, screen_ySize)
    bg_img = loadImage("background_img.png")
    noStroke()

    for i in range (1,14):
        kaart.append(loadImage(str(i)+".jpg"))    

def menuButton():
    global tabs
    for tab in tabs:
        fill(150)
        stroke(150)
        rect(50+tabs[tab]*150, 10, 125, 50, 10)
        noStroke()
        noFill()

def menuText():
    global tabNames
    for x in range(len(tabNames)):   
        fill(0,0,0)
        fonts("Arial Bold Italic", 13, True)
        textAlign(CENTER)
        text(tabNames[x], 50+(x*150), 30, 125, 50)
        noFill()


def mousePressed():
    global activeTab
    global selected_field
    if mouseButton == LEFT:
        if mouseX > 50 and mouseX < 175 and mouseY > 10 and mouseY < 60:
            activeTab = 0
        if mouseX > 200 and mouseX < 325 and mouseY > 10 and mouseY < 60:
            activeTab = 1
        if mouseX > 350 and mouseX < 475 and mouseY > 10 and mouseY < 60:
            activeTab = 2
        if mouseX > 500 and mouseX < 625 and mouseY > 10 and mouseY < 60:   
            activeTab = 3
        if mouseX > 650 and mouseX < 775 and mouseY > 10 and mouseY < 60: 
            activeTab = 4
        
        if activeTab == 4:
            if mouseX >198 and mouseY > 140 and mouseX <598 and mouseY < 160:
                selected_field = 1
                return selected_field
            
            if mouseX >198 and mouseY > 160 and mouseX <598 and mouseY < 180:
                selected_field = 2
                return selected_field
            
            if mouseX >198 and mouseY > 180 and mouseX <598 and mouseY < 200:
                selected_field = 3
                return selected_field
            
            if mouseX >198 and mouseY > 200 and mouseX <598 and mouseY < 220:
                selected_field = 4
                return selected_field
        else:
            selected_field = None
                            
def keyPressed():
    global spelerNamen
    global selected_field
    global activeTab
    
    if activeTab == 4 and selected_field != None:
        # SHIFT keyCode = 16;
        # keyCode 17 = CONTROL, 18 = ALT pressed
        # keyCode 9 = TAB
        if key == TAB:
            if selected_field > 3:
                selected_field = 1
            else:
                selected_field = selected_field +1
        elif key==BACKSPACE:
            if len(spelerNamen["speler"+str(selected_field)]) > 0:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)][:len(spelerNamen["speler"+str(selected_field)])-1]
        elif key==ENTER or key==RETURN:
            # Enter new line, not used in this program.
            # spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + "\n"
            selected_field = None
        elif (key >= 'A' and key <='Z') or (key >='a' and key <= 'z') or keyCode == 32 or key == SHIFT:
            if len(spelerNamen["speler"+str(selected_field)]) < 44:
                spelerNamen["speler"+str(selected_field)] = spelerNamen["speler"+str(selected_field)] + str(key)
        
                                    
def draw():    
    draw_bg(bg_img, screen_xSize, screen_ySize)
    menuButton()
    active(activeTab)
    menuText()
    
    if activeTab == 0:
        OverzichtGegevens()
    elif activeTab == 1:
        Duel()
    elif activeTab == 2:
        Rad1()
    elif activeTab == 3:
        Kaartregels()
    elif activeTab == 4:
        Names()


    
