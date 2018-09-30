

import math
from Agent import Agent

class Initiator:
    
    def __init__(self, id, agents = [], task = None):
        """
        initializes a grid graph with given number of rows and cols
        """
        self.id = id
        self.task = task
        self.agents = agents
        self.time = 0
        for a in agents:
            a.initiators.append(self)
            a.states[self.id] = "WAITING"
        agent_ids = [a.id for a in self.agents]
        print("Initiator nr",self.id,"created for",self.task.toString(),"with following participants: ",agent_ids)
        #self.showAgents()
        self.contractor = None
        self.offers = {}
        for a in self.agents:
            self.offers[a.id] = math.inf

    def step(self):
        
        if self.contractor == None:
            bestBid = math.inf
            bestAgent = None
            for a in self.agents:
                if a.states[self.id] == "WAITING":
                    a.states[self.id] = "CFP"

                if a.states[self.id] == "PRE_BID" or a.states[self.id] == "DEF_BID":
                    defbid_of_best = False
                    for a in self.agents:
                        if(self.offers[a.id]<bestBid):
                            bestBid = self.offers[a.id]
                            bestAgent = a.id
                            

                
            if(bestAgent != None):
                for a in self.agents:
                    if a.id == bestAgent:
                        if a.states[self.id] == "DEF_BID":
                            a.states[self.id] = "DEF_ACC"
                        else:
                            a.states[self.id] = "PRE_ACC"
                    else:
                        if a.states[self.id] == "PRE_BID":
                            a.states[self.id] = "PRE_REJ"
                        if a.states[self.id] == "DEF_BID":
                            a.states[self.id] = "DEF_REJ"
            
                
            
    
    def toString(self):
        agent_ids = [a.id for a in self.agents]
        return "Initiator nr "+str(self.id)+" task "+str(self.task.id)+" agents "+str(agent_ids)+" offers "+str(self.offers)
    
    def show(self):
        print("Initiator nr",self.id,"time",self.time,self.task.toString())
    
    def showOffers(self):
        for k,v in self.offers.items():
            print("Agent nr",k,"offers",v)
    def showAgents(self):
        for a in self.agents:
            a.show()
            



