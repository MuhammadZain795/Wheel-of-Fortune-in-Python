import random
import turtle
from turtle import *

color1 = ['#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE']
color2 = ['#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00']
color3 = ['#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000']
color4 = ['#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800']
color5 = ['#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800']
color6 = ['#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888']
color7 = ['#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0']
color8 = ['#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088']
color9 = ['#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE']
color10 = ['#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000']
color11 = ['#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400']
color12 = ['#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800']
color13 = ['#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000']
color14 = ['#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888']
color15 = ['#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0']
color16 = ['#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088']
color17 = ['#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE']
color18 = ['#884400','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000']
color19 = ['#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400']
color20 = ['#008800','#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800']
color21 = ['#008888','#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800']
color22 = ['#C0C0C0','#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888']
color23 = ['#440088','#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0']
color24 = ['#B0C4DE','#FF8C00','#000000','#888800','#008800','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#000000','#008888','#C0C0C0','#440088','#B0C4DE','#880000','#884400','#888800','#008800','#008888','#C0C0C0','#440088']
colors = [color1, color2, color3, color4, color5, color6, color7, color8, color9, color10, color11, color12, color13, color14, color15, color16, color17, color18, color19, color20, color21, color22, color23, color24]


result1 = ['$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50']
result2 = ['$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50', '$100']
result3 = ['$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50', '$100', '$1000']
result4 = ['$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500']
result5 = ['BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200']
result6 = ['$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT']
result7 = ['$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400']
result8 = ['$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1']
result9 = ['Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000']
result10 = ['$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play']
result11 = ['$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100']
result12 = ['$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400']
result13 = ['$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200']
result14 = ['$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1']
result15 = ['Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500']
result16 = ['$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn']
result17 = ['$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100']
result18 = ['$10', '$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000']
result19 = ['$200', '$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10']
result20 = ['$600', '$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200']
result21 = ['$650', 'BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600']
result22 = ['BANKRUPT', '$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650']
result23 = ['$250', '$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT']
result24 = ['$50','$100', '$1000', '$500', '$200', 'BANKRUPT', '$400', '$1', '$5000', 'Free Play', '$100', '$400', '$200', '$1', '$500', 'Lose turn', '$100', '$1000', '$10', '$200', '$600', '$650', 'BANKRUPT', '$250']
results = [result1, result2, result3, result4, result5, result6, result7, result8, result9, result10, result11, result12, result13, result14, result15, result16, result17, result18, result19, result20, result21, result22, result23, result24]
circle = Turtle()
ran = random.choice([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])


def wheel(colors, radius, center=(0, 0)):
    slice_angle = 360 / len(colors)
    heading, position = 90, (center[0] + radius, center[1])
    for color in colors:
        circle.color(color, color)
        circle.speed('fastest')
        circle.penup()
        circle.goto(position)
        circle.setheading(heading)
        circle.pendown()
        circle.begin_fill()
        circle.circle(radius, extent=slice_angle)
        heading, position = circle.heading(), circle.position()
        circle.penup()
        circle.goto(center)
        circle.end_fill()
    write('white', results[ran][19], toWrite[0], center=(25, 50))
    write('white', results[ran][20], toWrite[1], center=(25, 50))
    write('white', results[ran][21], toWrite[2], center=(25, 50))
    write('white', results[ran][22], toWrite[3], center=(25, 500))
    write('white', results[ran][23], toWrite[4], center=(25, 50))
    write('white', results[ran][0], toWrite[5], center=(25, 50))
    write('white', results[ran][1], toWrite[6], center=(25, 50))
    write('white', results[ran][2], toWrite[7], center=(25, 50))
    write('white', results[ran][3], toWrite[8], center=(25, 50))
    write('white', results[ran][4], toWrite[9], center=(25, 50))
    write('white', results[ran][5], toWrite[10], center=(25, 50))
    write('white', results[ran][6], toWrite[11], center=(25, 50))
    write('white', results[ran][7], toWrite[12], center=(25, 50))
    write('white', results[ran][8], toWrite[13], center=(25, 50))
    write('white', results[ran][9], toWrite[14], center=(25, 50))
    write('white', results[ran][10], toWrite[15], center=(25, 50))
    write('white', results[ran][11], toWrite[16], center=(25, 50))
    write('white', results[ran][12], toWrite[17], center=(25, 50))
    write('white', results[ran][13], toWrite[18], center=(25, 50))
    write('white', results[ran][14], toWrite[19], center=(25, 50))
    write('white', results[ran][15], toWrite[20], center=(25, 50))
    write('white', results[ran][16], toWrite[21], center=(25, 50))
    write('white', results[ran][17], toWrite[22], center=(25, 50))
    write('white', results[ran][18], toWrite[23], center=(25, 50))
    # circle.hideturtle()
    # turtle.done()


toWrite = [(230, 63), (200, 120), (170, 170), (140, 210), (90, 240), (30, 260), (-19, 260), (-80, 250), (-135, 220), (-170, 180), (-200, 130), (-215, 65), (-215, 15), (-200, -40), (-170, -90), (-130, -135), (-80, -175), (-30, -190), (35, -190), (90, -170), (140, -140), (170, -95), (210, -50), (220, 10)]


def wheelSpin(colors, radius, outer, inner, center=(0, 0)):
    global ran
    slice_angle = 360 / len(colors)
    heading, position = 90, (center[0] + radius, center[1])
    where = 0
    for color in colors:
        circle.color(color, color)
        circle.speed('fastest')
        circle.penup()
        circle.goto(position)
        circle.setheading(heading)
        circle.pendown()
        circle.begin_fill()
        circle.circle(radius, extent=slice_angle)
        heading, position = circle.heading(), circle.position()
        circle.penup()
        circle.goto(center)
        circle.end_fill()
        write('white', results[outer][inner], toWrite[where])
        where = where + 1
        inner = inner + 1
        circle.hideturtle()


def write(color, whatToWrite, toWrite, center=(0, 0)):
    circle.penup()
    circle.goto(toWrite)
    circle.pendown()
    circle.color(color)
    if (whatToWrite == 'BANKRUPT') or (whatToWrite == 'Lose turn') or (whatToWrite == 'Free Play'):
        circle.write(whatToWrite, font=("Arial", 8, "bold"))
    else:
        circle.write(whatToWrite, font=("Arial", 12, "bold"))
    circle.penup()
    circle.goto(center)


xcoor = -600
ycoor = 300
player1score = 1000
player2score = 1000
player1status = True
player2status = False


def getRandomPhraseFromFile(file):
    openFile = open(file).read().splitlines()
    line = random.choice(openFile)
    return line


puzzle = []
calledLetters = []
phrase = getRandomPhraseFromFile('phrases.txt')


def findCharInArray(char):
    for i in range(len(calledLetters)):
        if char == calledLetters[i]:
            return True
    return False


def generateDashes(line):
    dashes = list(line.split())
    res = len(dashes)
    print(res)
    for i in range(0, res):
        dashes[i] = list(dashes[i])
        res1 = len(dashes[i])
        for j in range(0, res1):
            if not findCharInArray(dashes[i][j]):
                dashes[i][j] = '*'
        dashes[i] = ''.join(dashes[i])
    dashes = ' '.join(dashes)
    return dashes


def updateScore(count):
    global player1score
    global player2score
    if player1status:
        player1score = player1score + count
    else:
        player2score = player2score + count


def isLetterInPhrase(string, letter):
    if findCharInArray(letter):
        return 0
    return string.count(letter)


def nextPlayersTurn():
    global player1status
    global player2status
    if player1status:
        player1status = False
        player2status = True
    else:
        player2status = False
        player1status = True


def consonantOrVowel():
    return input("Consonant or Vowel: ")


def checkScore():
    if player1status:
        return player1score
    else:
        return player2score


def deductScore():
    if player1status:
        global player1score
        player1score = player1score - 250
        return player1score
    else:
        global player2score
        player2score = player2score - 250
        return player2score


def isVowel(v):
    if (v == 'A') or (v == 'E') or (v == 'I') or (v == 'O') or (v == 'U'):
        return True
    return False


def vowelChoosed():
    if checkScore() < 250:
        print("Your amount is less than 250$: ", checkScore(), " ,So, you must have to spin.")
        spinTheWheel()
    else:
        vowel = input("Give a vowel: ")
        while not isVowel(vowel):
            vowel = input("Please enter VOWEL: ")
        if isLetterInPhrase(phrase, vowel) > 0:
            calledLetters.append(vowel)
            puzzle.append(generateDashes(phrase))
            print(generateDashes(phrase))
            print(deductScore())
            choiceBtwVowelSpinSolve()
        else:
            nextPlayersTurn()
            afterChoosingConsonantOrVowel()


def checkPuzzle():
    res = input("Write complete phrase in Capital words: ")
    if res == phrase:
        return True
    return False


def winner():
    if player1status:
        print("Player 1 is winner of this Game with winning price: ", player1score)
    else:
        print("Player 2 is winner of this Game with winning price: ", player2score)


def choiceBtwVowelSpinSolve():
    choice2 = input("What you want to do now? Spin the wheel or Buy a vowel or Solve the puzzle: ")
    if choice2 == "Spin the wheel":
        spinTheWheel()
    elif choice2 == "Buy a vowel":
        vowelChoosed()
    elif choice2 == "Solve the puzzle":
        if checkPuzzle():
            winner()
        else:
            nextPlayersTurn()
            afterChoosingConsonantOrVowel()


def displayScore():
    global player1status
    global player1score
    global player2score
    if player1status:
        return player1score
    return player2score


def afterChoosingConsonantOrVowel():
    choice = consonantOrVowel()
    if (choice == "vowel") or (choice == "Vowel"):
        vowelChoosed()
    elif (choice == "consonant") or (choice == "Consonant"):
        letter = input("ok now provide a letter: ")
        count = isLetterInPhrase(phrase, letter)
        while isVowel(letter):
            letter = input("Please do not enter VOWEL: ")
        if count > 0:
            updateScore(count)
            print(displayScore())
            calledLetters.append(letter)
            puzzle.append(generateDashes(phrase))
            print(generateDashes(phrase))
            choiceBtwVowelSpinSolve()
        else:
            nextPlayersTurn()


def bankrupt():
    global player1score
    global player1status
    global player2score
    global player2status
    if player1status:
        player1score = 0
    else:
        player2score = 0
    nextPlayersTurn()
    spinTheWheel()


def loseTurn():
    nextPlayersTurn()
    spinTheWheel()


def freePlay():
    res = input("Call anything vowel or consonant: ")
    if isLetterInPhrase(phrase, res) > 0:
        calledLetters.append(res)
        print(generateDashes(phrase))
        spinTheWheel()


def writePuzzles():
    p1 = turtle.Turtle()
    p1.penup()
    p1.goto(xcoor, ycoor)
    p1.pendown()
    p1.write(generateDashes(phrase), font=("Arial", 20, "bold"))


def arrow():
    arrow = turtle.Turtle()
    arrow.penup()
    arrow.goto(360, 85)
    arrow.left(180)
    arrow.pendown()
    arrow.forward(30)


def spinTheWheel():
    temp = ran
    temp1 = 0
    writePuzzles()
    arrow()
    for i in range(0, temp):
        if temp1 <= 23:
            temp1 = temp1 + 1
            wheelSpin(colors[i], 250, temp1, 0, center=(25, 50))
    # res = input("Enter output of wheel spin: ")
    # if res == "Number":
    #     afterChoosingConsonantOrVowel()
    # elif res == "Bankrupt":
    #     bankrupt()
    # elif res == "Lose a turn":
    #     loseTurn()
    # elif res == "Free Play":
    #     freePlay()


def displayBoard():
    # wn = turtle.Screen()
    # wn.title("Wheel of Fortune")
    # wn.bgcolor('grey')
    # wn.setup(width=650, height=600)
    # wn.tracer(0)
    writePuzzles()


    # p = turtle.Turtle()
    # p.penup()
    # p.goto(-600, 300)
    # p.pendown()
    # p.write(generateDashes(phrase), font=("Arial", 20, 'bold'))
    arrow()
    wheel(colors[0], 250, center=(25, 50))


displayBoard()
# spinTheWheel()
# print(results[ran][0])
circle.hideturtle()
turtle.done()
