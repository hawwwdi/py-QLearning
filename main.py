from agent import Agent

def main():
    map = [[-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]]
    #print(len(map))
    bot = Agent(map)
    bot.start(500)
    bot.think()

if __name__ == '__main__':
    main()

