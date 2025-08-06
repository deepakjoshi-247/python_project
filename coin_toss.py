coin_game_v2/main.py
# idk how but it worked 
# highscore checker with coin toss
import random
with open("D:/testing/coin_score.txt","r+") as coin:
    # coin.seek(0)
    # coin.write("Highscore- "+ str(highscore))  no need as highscore is already set
    score = 0
    line = coin.read()
    highscore = int(line.strip().split("-")[1])
    while(True):
        user = int(input("Choose one coin side : 1.Heads  2.Tails  3.exit\n"))
        if(user==3 or (user!=1 and user!=2 )):  break
        pc = random.choice((1,2))
        if(pc==user):
            print("I am feeling lucky today")
            score+=1
        else:   print("uh-oh dangit!")
    if(score>highscore):    
        coin.seek(0)
        coin.write("Highscore- "+ str(score))
        coin.truncate() # dont know what in loving grace it does but it helps from make old + new 
    coin.seek(0)
    hs = coin.read()
    print(hs)
