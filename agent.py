from random import randint


class Agent:
    
    def __init__(self, map, gamma=0.8):
        self.map = map
        self.gamma = gamma
        self.maxLen = len(map)
        self.brain = [[0 for i in range(self.maxLen)] for j in range(self.maxLen)]
        #self.state = randint(maxLen)
        pass
    

    def __getPossbleActions(self, state):
        return [i for i in range(self.maxLen) if self.map[state][i]!=-1]

    def devideBrain(self):
        maximum = max([max(row) for row in self.brain])
        if maximum>100:
            self.brain = [list(map(lambda x: round((x/maximum)*100), row)) for row in self.brain]
        else: 
            pass

    def __updatebrain(self):
        possibleActions = self.__getPossbleActions(self.state)
        action = possibleActions[randint(0, len(possibleActions)-1)]
        #if action !=5:
        self.brain[self.state][action] = self.map[self.state][action] + (self.gamma* max([self.brain[action][i] for i in self.__getPossbleActions(action)])) 
        #else: 
        #self.brain[self.state][action] = 100
        print(f'state:{self.state} action:{action}')
        self.state = action
    
    def printBrain(self):
        """ for ls in self.brain:
            for i in ls:
                print(i, end=' ')
            print() """
        print('\n\n\n'.join([''.join(['{:7}'.format(item) for item in row]) 
        for row in self.brain]))
        pass

    def start(self, tryCount):
        for i in range(tryCount):
            self.state = randint(0, self.maxLen-1)
            flag = True
            while self.state != 5 or flag:
                #elf.printBrain()
                flag = False
                self.__updatebrain()
            else: 
                self.printBrain()
                print('goal state reached')
        else:
            self.devideBrain()
            self.printBrain()
            print(f'brain after {tryCount} try!')

    def think(self):
        self.state = randint(0,self.maxLen-1)
        print(f'starting state: {self.state} ', end='')
        count = 0
        while self.state != 5:
            newStatePoint = max(self.brain[self.state])
            newState = self.brain[self.state].index(newStatePoint)
            if newStatePoint == 0:
                print("sorry brain not respondig\n selecting random action")
                possibleActions = self.__getPossbleActions(self.state)
                newState = possibleActions[randint(0, len(possibleActions)-1)]
            print(f'--> {newState} ', end=' ')
            self.state = newState
            count += 1 
        print(f'done\n count: {count}')





