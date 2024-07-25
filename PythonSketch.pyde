def setup():
    global stage, titleX1, titleX2, titleY1, titleY2, speed, inGame, userText, choices, question, inStageOne, enterCount, instructions, answers, shirtColourOne, shirtColourTwo, shirtColourThree, skinColours, skinChosen, skinColourOne, skinColourTwo, skinColourThree, tallies, listTotal, inStageTwo, rectangle, previousY1, previousY2, previousY3, previousY4, rectangle1, rectangle2, rectangle3, rectangle4
    inGame = False 
    inStageOne = False
    inStageTwo = False
    answers = False 
    size(600,600)
    stage = 0 
    titleX1 = 67  
    titleX2 = 175
    titleY1 = 155
    titleY2 = 215
    speed = 1
    userText = ''
    question = ''
    choices = ["example","example","example","example"]
    enterCount = 0 
    instructions = ''
    # Variables that are used throughout the entirety of the code 

    skinColours = [141,85,36,198,134,66,224,172,105,241,194,125,255,219,172]
    shirtColourTwo = random(0,255)
    shirtColourTwo = random(0,255)
    shirtColourThree = random(0,255)
    skinChosen = int(random(5))
    skinColourOne = skinColours[skinChosen*3]
    skinColourTwo = skinColours[(skinChosen*3)+1]
    skinColourThree = skinColours[(skinChosen*3)+2]
    # Variables that relate to the people 

    tallies = [0,0,0,0]
    listTotal = 0 
    # Variables that relate to the data collecting part 

    rectangle1 = 0
    rectangle2 = 0
    rectangle3 = 0
    rectangle4 = 0
    previousY1 = 0
    previousY2 = 0
    previousY3 = 0
    previousY4 = 0
    # Variables that are specific to Stage 2 

def titleScreen(): 
    global titleX1, titleX2, titleY1, titleY2, speed
    background(64,106,194)

    if titleY1 > 185 or titleY1 < 100:
        speed *= -1
    titleY1 += speed 
    titleY2 += speed 
    # Creating the title movement and bounce  

    textAlign(LEFT)
    textSize(50)
    fill(238, 238, 238) 
    text("Data Management",titleX1,titleY1)
    text("Simulator",titleX2,titleY2)
    # Creating title 

    fill(114, 114, 114)
    rect(190,300,220,50,10)
    textSize(32)
    fill(194,197,204)
    text("Stage One",220,335)
    # First Button 

    fill(114, 114, 114)
    rect(190,400,220,50,10)
    textSize(32)
    fill(194,197,204)
    text("Stage Two",220,435)
    # Second Button 

def stageOne(): 
    global userText, question, instructions, choices, enterCount, answers, shirtColourOne,shirtColourTwo, shirtColourThree, skinColours, skinChosen, skinColourOne, skinColourTwo, skinColourThree, tallies
    background(129, 212, 250)
    fill(189, 189, 189)
    rect(0,400,600,200)
    fill(238, 238, 238)
    rect(0,0,200,400)
    # Setting up the stage's layout 

    fill(0)
    textAlign(LEFT, TOP)
    textSize(20)
    text(question,20,25,160,100)
    if enterCount == 0: 
        text(userText,250,50,300,50)
    elif enterCount >= 1 and enterCount <= 5:
        text(userText,250,50,120,50)
    text(instructions,25,425,550,175)
    # Creating the basic text for Stage 1 

    if enterCount == 0: 
        instructions = "For Stage 1, you must create a question that people will have to answer. For example, \"What is your favourite colour?\" or \"Who do you prefer more?\"."
    elif enterCount >= 1 and enterCount <= 5: 
        instructions = "Now, you must create four choices for the people to choose from. Make sure all these choices are different from each other!"
        if enterCount >= 2: 
            text(choices[0],20,150,120,50)
            if enterCount >= 3: 
                text(choices[1],20,200,120,50)
                if enterCount >= 4: 
                    text(choices[2],20,250,120,50)
                    if enterCount == 5: 
                        text(choices[3],20,300,120,50)
                        answers = True 
                        enterCount += 1 
    # Instruction changes and additional information to the side bar 
    
    if enterCount >= 6: 
        text(choices[0],20,150,120,50)
        text(choices[1],20,200,120,50)
        text(choices[2],20,250,120,50)
        text(choices[3],20,300,120,50)
        text(str(tallies[0]),170,150,30,50)
        text(str(tallies[1]),170,200,120,50)
        text(str(tallies[2]),170,250,120,50)
        text(str(tallies[3]),170,300,120,50)
        # Keeping all of the choices on the side bar (and not disappearing)

        if enterCount == 6: 
            instructions = "People will now start coming up to you and you will have to record their answers. Press enter to ask your question to the person." 
            # Setting up the instructions for this section
        elif enterCount == 7: 
            instructions = question+", said by the Player."  
            # Setting up the instructions for this section 

            fill(0)
            fill(shirtColourOne,shirtColourTwo,shirtColourThree)
            rect(350,200,100,200)
            fill(skinColourOne,skinColourTwo,skinColourThree)
            circle(350+50,200,150)
            # The drawing of the person who is being asked the questions 
        elif enterCount >= 7 and enterCount%2 == 1: 
            instructions = "The previous person has left and a new one has shown up! Press to ask your question to this person." 
            # Setting up the instructions for this section 

            fill(0)
            fill(shirtColourOne,shirtColourTwo,shirtColourThree)
            rect(350,200,100,200)
            fill(skinColourOne,skinColourTwo,skinColourThree)
            circle(350+50,200,150)
            # The drawing of the person who is being asked the questions 
        elif enterCount >= 7 and enterCount%2 == 0: 
            instructions = "The player said their question! The person has answered!" 
            # Setting up the instructions for this section 

            fill(0)
            text(userText,500,100,75,50)
            fill(shirtColourOne,shirtColourTwo,shirtColourThree)
            rect(350,200,100,200)
            fill(skinColourOne,skinColourTwo,skinColourThree)
            circle(350+50,200,150)
            # The drawing of the person who is being asked the questions  

def stageTwo(): 
    global userText, question, instructions, choices, enterCount, answers, shirtColourOne,shirtColourTwo, shirtColourThree, skinColours, skinChosen, skinColourOne, skinColourTwo, skinColourThree, tallies, rectangle1, rectangle2, rectangle3, rectangle4, previousY1, previousY2, previousY3, previousY4
    background(0, 0, 139)
    fill(79, 79, 79)
    rect(0,400,600,200)
    fill(114, 114, 114)
    rect(0,0,200,400)
    # Setting up the layout of Stage 2 

    fill(255)
    textAlign(LEFT, TOP)
    textSize(20)
    text(question,20,25,160,100)
    text(instructions,25,425,550,175)
    # Setting up the text for Stage 2 

    text(choices[0],20,150,120,50)
    text(choices[1],20,200,120,50)
    text(choices[2],20,250,120,50)
    text(choices[3],20,300,120,50)
    text(str(tallies[0]),170,150,30,50)
    text(str(tallies[1]),170,200,120,50)
    text(str(tallies[2]),170,250,120,50)
    text(str(tallies[3]),170,300,120,50)
    # Putting information from Stage 1 onto sidebar of Stage 2 

    stroke(255)  
    strokeWeight(4)
    line(300,40,300,300)
    line(300,300,550,300)
    strokeWeight(1)
    linesY = 300
    for i in range(10):
        linesY -= 25
        line(300,linesY,550,linesY)
    stroke(0)
    fill(255)
    textSize(15)
    choiceX = 225
    for choice in choices: 
        choiceX += 75 
        text(choice,choiceX,325)
    iY = 315
    for i in range(11):
        iY -= 25
        text(i,275,iY)
    # Creating the componenents of the graph 
    
    if enterCount == 0: 
        instructions = "For Stage 2, you must create your own graph using the information collected from Stage 1. If you have not completed Stage 1, please rerun this program because information from Stage 1 is carried into Stage 2. Press enter to continue."
    elif enterCount == 1: 
        instructions = "Click on top of each choice name to create a bar for that choice. Using the information in the side bar, make this graph as accurate as possible. After you are finished, press enter."
    elif enterCount == 2: 
        instructions = "Great job! Here are some useful facts. The most chosen choice has a value of "+str(max(tallies))+" and the least chosen choice has a value of "+str(min(tallies))+'. You have now successfully completed this game! Play again by reruning the code!'
    # Changing the instructions everytime the player presses enter 
    
    if rectangle1 == 1: 
        rect(300,300,50,previousY1-300)
    if rectangle2 == 2: 
        rect(370,300,50,previousY2-300)
    if rectangle3 == 3: 
        rect(440,300,50,previousY3-300)
    if rectangle4 == 4:
        rect(510,300,50,previousY4-300)
    # The changes of size of the bars of the graph 

def draw():
    global stage, inStageOne, inStageTwo
    if stage == 2: 
        stageTwo()
        inStageOne = False 
        inStageTwo = True
    elif stage == 0: 
        titleScreen()
        inStageOne = False
        inStageTwo = False
    elif stage == 1: 
        stageOne()
        inStageOne = True 
        inStageTwo = False
    # The switching of screens 
    
def mousePressed(): 
    global stage, inGame, inStageTwo, inStageOne, rectangle, previousY1, previousY2, previousY3, previousY4, rectangle1, rectangle2, rectangle3, rectangle4
    if stage == 0: 
        if (mouseX >= 190 and mouseX <= 410) and (mouseY >= 300 and mouseY <= 350):  
            stage = 1 
            inGame = True 
        elif (mouseX >= 160 and mouseX <= 440) and (mouseY >= 400 and mouseY <= 450):  
            stage = 2
            inGame = True 
    # Making the buttons on the title screen actually work 
    if inStageTwo: 
        if (mouseX >= 300 and mouseX <= 370) and (mouseY >= 40 and mouseY <= 300): 
            rectangle1 = 1 
            previousY1 = mouseY
        elif (mouseX >= 370 and mouseX <= 440) and (mouseY >= 40 and mouseY <= 300):
            rectangle2 = 2 
            previousY2 = mouseY
        elif (mouseX >= 440 and mouseX <= 510) and (mouseY >= 40 and mouseY <= 300):
            rectangle3 = 3 
            previousY3 = mouseY
        elif (mouseX >= 510 and mouseX <= 580) and (mouseY >= 40 and mouseY <= 300):
            rectangle4 = 4 
            previousY4 = mouseY
    # Allowing the player to change the bar 
def keyPressed():
    global userText, count, question, inStageOne, choices, enterCount, tallies, shirtColourOne, shirtColourTwo, shirtColourThree, skinColours, skinChosen, skinColourOne, skinColourTwo, skinColourThree, listTotal, stage, titleX1, titleX2, titleY1, titleY2, speed, inGame, instructions, inStageTwo
    if inStageOne:
        if enterCount < 5:
            if keyCode == 8 and len(userText) > 0: 
                userText = userText[0:len(userText)-1]
            elif keyCode == 8:
                pass
            elif keyCode == 10 and question == '' and userText != '': 
                enterCount += 1
                question = userText 
                userText = ''
            elif keyCode == 10 and userText != '': 
                enterCount += 1 
                if choices[0] == 'example':
                    choices[0] = userText
                elif choices[1] == 'example':
                    choices[1] = userText
                elif choices[2] == 'example':
                    choices[2] = userText
                elif choices[3] == 'example':
                    choices[3] = userText
                userText = ''
            elif keyCode == 10: 
                pass
            elif keyCode == 16:  
                pass
            else: 
                userText += key
        # Allowing the player to type out the question and choices
        for i in tallies: 
            listTotal += int(i)
        if listTotal <= 10: 
            if keyCode == 10 and enterCount >= 6 and enterCount%2 == 0:
                enterCount += 1 
                shirtColourOne = random(0,255)
                shirtColourTwo = random(0,255)
                shirtColourThree = random(0,255)
                skinChosen = int(random(5))
                skinColourOne = skinColours[skinChosen*3]
                skinColourTwo = skinColours[(skinChosen*3)+1]
                skinColourThree = skinColours[(skinChosen*3)+2]
            elif keyCode == 10 and enterCount >= 6 and enterCount%2 == 1:
                enterCount += 1
                userText = choices[int(random(len(choices)))]
                if userText == choices[0]: 
                    tallies[0] += 1
                elif userText == choices[1]:
                    tallies[1] += 1
                elif userText == choices[2]:
                    tallies[2] += 1
                elif userText == choices[3]:
                    tallies[3] += 1
        # Randomizing the shirt colour and skin colour
        # Also counting how many people chose each option 
        listTotal = 0 
        if enterCount == 26: 
            stage = 0
            enterCount = 0
            inGame = False
            instructions = ''
            # Reseting values to original value 
            
            titleX1 = 67  
            titleX2 = 175
            titleY1 = 155
            titleY2 = 215
            speed = 1
            # Restating variables with their original value to prevent an issue from occuring for the title screen 
    if inStageTwo:
        if keyCode == 10: 
            enterCount += 1 
