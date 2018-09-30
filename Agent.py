
import math
from math import ceil
from networkx import shortest_path_length


class Agent:
    
    def __init__(self, id, initPos, prefs, world = None, maxCap=3, restTime=1, speed=1 ):
        """
        initializes a transport agent
        
        Arguments:
            initiator: reference to the initiator : pointer
            id: id of an agent : integer
            initPos : initial position : (int, int)
            prefs : list of tasks ids sorted by > : [integer]
            maxcap: maximum capacity of an agent, how many km
                can he drive without a break : integer
            restTime: time needed to recharge capacity to maxCap value
            speed: how many km can an agent drive in one time unit : integer
        """
        self.world = world
        self.id = id
        self.initiators = []
        self.maxCap = maxCap
        self.curCap = maxCap
        self.restTime = restTime
        self.restTimeCounter = 0
        self.speed = speed
        self.prefs = prefs
        self.tasks = []
        self.pos = initPos
        self.contracted = []
        self.states = {}
        self.currentBid = {}
        for p in self.prefs:
            self.currentBid[p] = math.inf
    
    def show(self):
        print("    Agent nr",self.id,"cap",self.maxCap,"speed",self.speed,"pos",self.pos,"prefs",str(self.prefs),"tasks queue",str([t.id for t in self.tasks]),"states ",str(self.states))

    def showInitiators(self):
        for i in self.initiators:
            i.show()
    def collect(self):
        for i in self.initiators:
            if self.states[i.id]=="CFP":
                if i.task.id not in self.prefs:
                    self.states[i.id] = "DEF_REJ"
                else:
                    self.tasks.append(i.task)
                    self.states[i.id] = "PRE_BID"
            elif self.states[i.id]=="PRE_REJ":
                self.states[i.id] = "PRE_REJ"
            elif self.states[i.id]=="PRE_ACC":
                self.states[i.id] = "DEF_BID"
            elif self.states[i.id]=="DEF_ACC":
                i.contractor = self
                self.states[i.id]="CONTRACTOR"
                self.contracted.append(i.task.target)
        
    def step(self):
        for i in self.initiators:
            if self.states[i.id]=="PRE_BID":
                i.offers[self.id] = self.calculateBid(i.task)
                self.currentBid[i.task.id] = i.offers[self.id]
                self.states[i.id] = "PRE_BID"
            
            elif self.states[i.id] == "DEF_BID":
                i.offers[self.id] = self.currentBid[i.task.id]
                pass
            
            elif self.states[i.id]=="PRE_REJ":
                newBid = self.calculateBid(i.task)
                #print("new bid : ",newBid)
                if newBid < self.currentBid[i.task.id]:
                    i.offers[self.id] = newBid
                    self.currentBid[i.task.id] = newBid
                    self.states[i.id] = "PRE_BID"
                else:
                    self.states[i.id] = "DEF_REJ"
            


    def sortTasks(self):
        sorted_tasks = []
        for i in range(len(self.prefs)):
            for t in self.tasks:
                if self.prefs[i] == t.id:
                    sorted_tasks.append(t)
                    break
        self.tasks = sorted_tasks


    def calculateBid(self, task):
        # collect tasks in correct order according to preferences
        def ceildiv(a, b):
            return -(-a // b)
        
        def positivize(a):
            return 0 if a < 0 else a
        #print("before filter:" ,[t.id for t in self.tasks])
        for i in self.initiators:
           self.tasks = list(filter( lambda t: self.states[t.id] not in ["PRE_REJ","DEF_REJ"] ,self.tasks))
        
        if task not in self.tasks:
            self.tasks.append(task)
        #print("after filter and append, before sort:" ,[t.id for t in self.tasks])
        self.sortTasks()
        #print("---------------------")
        #print("after sort:" ,[t.id for t in self.tasks])


        route = [self.pos]
        route.extend(self.contracted)
        route.extend([ t.target for t in self.tasks[: self.tasks.index(task)+1]])
        #print("current path to follow:",route)
        #print(route) 
        length = sum([ shortest_path_length(self.world.world,route[i-1],route[i]) for i in range(1,len(route)) ])
        length = ceildiv(length, self.speed)
        return length + positivize(ceildiv(length,self.maxCap)-1)*self.restTime
    
        

        