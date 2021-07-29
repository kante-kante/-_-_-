# 맵은 24 X 19의 행렬로 가정한다.
import time
import threading
import os
import msvcrt as ms
import random
"""
status=[0,0.5,1.0]
shuffle(status)
공이 벽이나 스틱, 블럭과 부딪혔을때 튕기는 정도를 랜덤으로 결정한다는 아이디어를 실현하기 위한 코드
"""
IsUpper=True # 공이 올라가는 중이면 True, 내려가는 중이면 False
ballStatus=1 #  -1 -0.5 0 0.5 1 
gameMap=[]
ballPosition=[21,9]
stickPosition=[22,9]
IsPlaying=False
tmp=0
move=0


def initValue():
    global tmp, gameMap, ballPosition, stickPosition, move
    gameMap=[]

    for i in range(24):
        tmp=i
        gameMap.append(['0' for j in range(19)])

    gameMap[ballPosition[0]][ballPosition[1]]='0'

    for k in range(-2,3):
        gameMap[stickPosition[0]][stickPosition[1]+k]='0'

    for k in range(-2,3):
        gameMap[22][9+k]='stick'

    gameMap[21][9]='ball'

    gameMap[3][6]='4'
    gameMap[7][2]='1'
    ballPosition=[21,9]
    stickPosition=[22,9]
    move=0
    
    


def drawMap():
    global gameMap, move
    os.system('cls')
    rep=''
    bar="▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤ ▤  "
    rep+=bar

    for i in range(24):
        rep+='\n▤ '

        for j in range(19):
            if gameMap[i][j]=='0':
                rep+='♭ '
            elif gameMap[i][j]=='stick':
                rep+='〓'
            elif gameMap[i][j]=='ball':
                rep+='⊙ '
            elif gameMap[i][j]=='1':
                rep+='▥ '
            elif gameMap[i][j]=='2':
                rep+='▨ '
            elif gameMap[i][j]=='3':
                rep+='▧ '
            elif gameMap[i][j]=='4':
                rep+='▦ '
            elif gameMap[i][j]=='5':
                rep+='▩ '
        rep+='▤'
    print(rep)

            

def ballMove():
    global gameMap, IsUpper, ballPosition, ballStatus, move # -1 ,-0.5 0 0.5 1
    move+=ballStatus

    if IsUpper==True and abs(move)<1: # IsUpper가 True이고 ballStatus가 0 혹은 +-0.5일때
        if ballPosition[0]>0:
            if gameMap[ballPosition[0]-1][ballPosition[1]]=='0':
                gameMap[ballPosition[0]][ballPosition[1]]='0'
                ballPosition[0]-=1
                gameMap[ballPosition[0]][ballPosition[1]]='ball'

            elif gameMap[ballPosition[0]-1][ballPosition[1]] !='0':
                gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                IsUpper=False
        else:
            IsUpper=False

    elif IsUpper==False and abs(move)<1: # IsUpper가 False이고 ballStatus가 0 혹은 +-0.5일때
        try:
            if gameMap[ballPosition[0]+1][ballPosition[1]] != 'stick':
                if gameMap[ballPosition[0]+1][ballPosition[1]]=='0':
                    gameMap[ballPosition[0]][ballPosition[1]]='0'
                    ballPosition[0]+=1
                    gameMap[ballPosition[0]][ballPosition[1]]='ball'

                elif  gameMap[ballPosition[0]+1][ballPosition[1]]!='0':
                    gameMap[ballPosition[0]+1][ballPosition[1]] = str(int(gameMap[ballPosition[0]+1][ballPosition[1]])-1)
                    IsUpper=True

            else:
                IsUpper=True

        except IndexError:
            return True

    # 대각선 방향 모두 구현해줘야 하는데... 조건문 남발하게 생겼다.... # +사이에 끼어있을땐 어떻게????????? 
    elif IsUpper==True and abs(move)>=1: # IsUpper가 True이고 ballStatus가 +-1일때
        if ballPosition[0]>0: # 공이 맵 내부에 있을때
            gameMap[ballPosition[0]][ballPosition[1]]='0'

            if ballPosition[1]+move > 18 or ballPosition[1]+move < 0: # 공이 좌우벽과 부딪히는 경우
                ballStatus = -ballStatus
                #ballPosition[0]-=1
            else: # 공이 벽과 부딪히지 않는 경우
                if move<0: # 왼쪽으로 이동중
                    if int(gameMap[ballPosition[0]-1][ballPosition[1]-1])==0 and int(gameMap[ballPosition[0]-1][ballPosition[1]])==0 and int(gameMap[ballPosition[0]][ballPosition[1]-1])==0: # 벽돌이 이동방향에 없을때
                        ballPosition[0]-=1
                        ballPosition[1]+=int(move)

                    elif int(gameMap[ballPosition[0]-1][ballPosition[1]])!=0 and int(gameMap[ballPosition[0]][ballPosition[1]-1])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]][ballPosition[1]-1])-1)
                        gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                        ballPosition[0]+=1
                        ballPosition[1]-=int(move)
                        ballStatus = -ballStatus

                    elif int(gameMap[ballPosition[0]-1][ballPosition[1]])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                        ballPosition[0]+=1
                        ballPosition[1]+=int(move)
                        ballStatus = -ballStatus

                    elif int(gameMap[ballPosition[0]][ballPosition[1]-1])!=0:
                        gameMap[ballPosition[0]][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]][ballPosition[1]-1])-1)
                        ballPosition[0]-=1
                        ballPosition[1]-=int(move)
                        ballStatus = -ballStatus

                    elif int(gameMap[ballPosition[0]-1][ballPosition[1]-1])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]-1][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]-1])-1)
                        ballPosition[0]+=1
                        ballPosition[1]-=int(move)
                        ballStatus = -ballStatus

                else: # 오른쪽으로 이동중
                    if int(gameMap[ballPosition[0]-1][ballPosition[1]+1])==0 and int(gameMap[ballPosition[0]-1][ballPosition[1]])==0 and int(gameMap[ballPosition[0]][ballPosition[1]+1])==0: # 벽돌이 이동방향에 없을때
                        ballPosition[0]-=1
                        ballPosition[1]+=int(move)

                    elif int(gameMap[ballPosition[0]][ballPosition[1]+1])!=0 and int(gameMap[ballPosition[0]-1][ballPosition[1]])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]][ballPosition[1]+1])-1)
                        gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                        ballPosition[0]+=1
                        ballPosition[1]-=int(move)
                        ballStatus = -ballStatus

                    elif int(gameMap[ballPosition[0]-1][ballPosition[1]])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                        ballPosition[0]+=1
                        ballPosition[1]+=int(move)
                        

                    elif int(gameMap[ballPosition[0]][ballPosition[1]+1])!=0:
                        gameMap[ballPosition[0]][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]][ballPosition[1]+1])-1)
                        ballPosition[0]-=1
                        ballPosition[1]+=int(move)
                        ballStatus = -ballStatus

                    elif int(gameMap[ballPosition[0]-1][ballPosition[1]+1])!=0:
                        IsUpper=False
                        gameMap[ballPosition[0]-1][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]+1])-1)
                        ballPosition[0]+=1
                        ballPosition[1]-=int(move)
                        ballStatus = -ballStatus
            gameMap[ballPosition[0]][ballPosition[1]]='ball'
            move=0
        else:
            IsUpper=False


    elif IsUpper==False and abs(move)>=1: # IsUpper가 False이고 ballStatus가 +-1일때
        try:
            if gameMap[ballPosition[0]+1][ballPosition[1]] != 'stick':
                gameMap[ballPosition[0]][ballPosition[1]]='0'

                if ballPosition[1]+move > 18 or ballPosition[1]+move < 0:
                    ballStatus = -ballStatus
                    #ballPosition[0]+=1

                else: # 공이 벽과 부딪히지 않는 경우
                    if move<0: # 왼쪽으로 이동중
                        if int(gameMap[ballPosition[0]+1][ballPosition[1]-1])==0 and int(gameMap[ballPosition[0]+1][ballPosition[1]])==0 and int(gameMap[ballPosition[0]][ballPosition[1]-1])==0: # 벽돌이 이동방향에 없을때
                            ballPosition[0]+=1
                            ballPosition[1]+=int(move)

                        elif int(gameMap[ballPosition[0]+1][ballPosition[1]])!=0 and int(gameMap[ballPosition[0]][ballPosition[1]-1])!=0:
                            IsUpper=True
                            gameMap[ballPosition[0]][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]][ballPosition[1]-1])-1)
                            gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                            ballPosition[0]-=1
                            ballPosition[1]-=int(move)
                            ballStatus = -ballStatus

                        elif int(gameMap[ballPosition[0]+1][ballPosition[1]])!=0:
                            IsUpper=True
                            gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                            ballPosition[0]-=1
                            ballPosition[1]+=int(move)
                            ballStatus = -ballStatus

                        elif int(gameMap[ballPosition[0]][ballPosition[1]-1])!=0:
                            gameMap[ballPosition[0]][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]][ballPosition[1]-1])-1)
                            ballPosition[0]+=1
                            ballPosition[1]-=int(move)
                            ballStatus = -ballStatus

                        elif int(gameMap[ballPosition[0]+1][ballPosition[1]-1])!=0:
                            IsUpper=True
                            gameMap[ballPosition[0]-1][ballPosition[1]-1] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]-1])-1)
                            ballPosition[0]-=1
                            ballPosition[1]-=int(move)
                            ballStatus = -ballStatus

                    else: # 오른쪽으로 이동중

                        if int(gameMap[ballPosition[0]+1][ballPosition[1]+1])==0 and int(gameMap[ballPosition[0]+1][ballPosition[1]])==0 and int(gameMap[ballPosition[0]][ballPosition[1]+1])==0: # 벽돌이 이동방향에 없을때
                            ballPosition[0]+=1
                            ballPosition[1]+=int(move)

                        elif int(gameMap[ballPosition[0]][ballPosition[1]+1])!=0 and int(gameMap[ballPosition[0]+1][ballPosition[1]])!=0:
                            IsUpper=False
                            gameMap[ballPosition[0]][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]][ballPosition[1]+1])-1)
                            gameMap[ballPosition[0]-1][ballPosition[1]] = str(int(gameMap[ballPosition[0]-1][ballPosition[1]])-1)
                            ballPosition[0]-=1
                            ballPosition[1]-=int(move)
                            ballStatus = -ballStatus

                        elif int(gameMap[ballPosition[0]-1][ballPosition[1]])!=0:
                            IsUpper=False
                            gameMap[ballPosition[0]+1][ballPosition[1]] = str(int(gameMap[ballPosition[0]+1][ballPosition[1]])-1)
                            ballPosition[0]-=1
                            ballPosition[1]+=int(move)
                            

                        elif int(gameMap[ballPosition[0]][ballPosition[1]+1])!=0:
                            gameMap[ballPosition[0]][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]][ballPosition[1]+1])-1)
                            ballPosition[0]+=1
                            ballPosition[1]+=int(move)
                            ballStatus = -ballStatus

                        elif int(gameMap[ballPosition[0]+1][ballPosition[1]+1])!=0:
                            IsUpper=False
                            gameMap[ballPosition[0]+1][ballPosition[1]+1] = str(int(gameMap[ballPosition[0]+1][ballPosition[1]+1])-1)
                            ballPosition[0]-=1
                            ballPosition[1]-=int(move)
                            ballStatus = -ballStatus

                gameMap[ballPosition[0]][ballPosition[1]]='ball'
                move=0
            else:
                IsUpper=True

        except IndexError:
            return True

    return False

    
    
        

def stickMove():
    global IsPlaying, stickPosition, gameMap
    gameOver=False
    t=0

    while IsPlaying==True:
        i,j=stickPosition

        if ms.kbhit():
            key=ms.getch()

            if (key==b'a') and (j>=3):
                for k in range(-2,3):
                    gameMap[i][j+k]='0'
                    
                stickPosition[1]-=1
                i,j=stickPosition

                for k in range(-2,3):
                    gameMap[i][j+k]='stick'
                
            elif (key==b'd' )and (j<=15):
                for k in range(-2,3):
                    gameMap[i][j+k]='0'    
                stickPosition[1]+=1
                i,j=stickPosition

                for k in range(-2,3):
                    gameMap[i][j+k]='stick'
            else:
                pass
            t+=300
            
            drawMap()
            
                
        t+=1
        if t>=1800:
            gameOver = ballMove()
            t=0
            drawMap()

        if gameOver==True:
            IsPlaying=False
             
                
def GameStart():
    global gameMap, IsPlaying
    initValue()
    drawMap()
    print("s키를 누르면 시작합니다.")
    while True:
        if ms.kbhit():
            ch=ms.getch()
            if ch==b's':
                IsPlaying=True
                break
        
    while True:

        #gameMap[4][9]='3'
        drawMap()
        stickMove()
        print("GameOver")
        ch=input("다시하려면 r키를 눌러주세요.\n")

        if ch!='r':
            break
        else:
            initValue()
            IsPlaying=True
            #initValue()

        #IsPlaying=True
        #initValue()
        
GameStart()