#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from Initiator import Initiator
from Agent import Agent
from Task import Task
import networkx as nx
from World import World

from prettytable import PrettyTable
from pdfrw import *
from fpdf import FPDF

class Simulation:
    
    def __init__(self, config):
        # initialize tasks
        self.config = config
        self.tasks = []
        for t in config["tasks"]:
            self.tasks.append(Task(t["id"],t["time"],t["target"]))
        
        self.agents = []
        for a in config["agents"]:
            self.agents.append(Agent(a["id"],a["pos"],a["prefs"],maxCap=a["maxCap"],restTime=a["restTime"],speed=a["speed"]))
        self.world = World(rows=config["world"]["rows"], cols=config["world"]["cols"], agents=self.agents, tasks=self.tasks)
        for a in self.agents:
            a.world = self.world
        
        self.initiators = []
        
        headers = ["Step", "Task"]
        for a in self.agents:
            headers.append("A nr. "+str(a.id)+" offers:")
        self.pt = PrettyTable(headers)
    def countFinished(self):
        counter = 0
        for i in self.initiators:
            if i.contractor != None:
                counter += 1
        return counter
    def step(self, time ):
        # if there are any initiators to start at this time, initialize them
        for t in self.tasks:
            if t.time == time:
                self.initiators.append(Initiator(self.config["initiators"][t.id]["id"],self.agents, t))
                
        for i in self.initiators:
            i.step()
        for a in self.agents:
            a.show()
        for a in self.agents:
            a.collect()
            a.step()
            
    def simulate(self, max_steps = 10):
        time = 0
        contracts = ""
        self.world.show("world.png")
        while (self.countFinished()<len(self.initiators) and time < max_steps) or  time==0:
            print("------------------------- step nr",time,"begins -------------------------")
            self.step(time)
            
            print("------------------------- step nr",time,"ends   -------------------------")
            print("------------------------ step nr",time,"summary -------------------------")
            for i in self.initiators:
                print("    ",i.toString())
            print()
            for a in self.agents:
                a.show()
            for i in self.initiators:
                offers = []
                for a in i.agents:
                    offers.append(str(i.offers[a.id]))
                tab = [str(time),str(i.task.id)]
                tab.extend(offers)
                self.pt.add_row(tab)
            empty = []
            for i in range(len(self.agents)+2):
                empty.append(" ")
            self.pt.add_row(empty)
            time += 1
         
        
            
            
        print("----------------------------  final summary   ----------------------------")
        
        for i in self.initiators:
            if i.contractor == None:
                print("Task nr,",i.task.id," contracted to: no one")
                contracts += "Task nr "+str(i.task.id)+" contracted to: no one\n"
            else:
                print("Task nr,",i.task.id," contracted to: Agent nr",i.contractor.id)
                contracts += "Task nr "+str(i.task.id)+" contracted to: Agent nr "+str(i.contractor.id)+"\n"
        
        lines = self.pt.get_string()
        
        
        pdf = self.introProtocol();
        pdf.add_page()
        pdf.set_font('Courier','B',10)
        content = "5. Actual results:\n\n" + lines+"\n\n"+contracts
        pdf.multi_cell(0,3,content)
        
        pdf.output('protocols/protocol_'+self.config["name"]+'.pdf','F')
        
    def introProtocol(self):
        pdf=FPDF()
        pdf.set_font('Arial','B',20)
        pdf.add_page()
        
        header = "Protocol for "+self.config['name']
        pdf.cell(100,0,header, ln=1)
        pdf.cell(100,10,"", ln=1)
        pdf.set_font('Courier','B',9)
        temp = "1. About the scenario:\n\n"
        content = "2. Tasks used in the scenario:\n\n"+self.tasksToTable()+"\n\n3.Agents used in the scenario:\n\n"+self.agentsToTable()+"\n\n4. grid world used in the scenario:\n\n"
        full = temp+self.config['about']+"\n\n"+content
        pdf.multi_cell(w=0,h=3,txt=full)
        pdf.image("img/world.png", x=0, y=150, w = 100, h=74)
    
        return pdf
           
    def agentsToTable(self):
        headers = ["id","position","preferences","capacity","rest time", "speed"]
        pt = PrettyTable(headers)
        for a in self.agents:
            pt.add_row([str(a.id),str(a.pos),str(a.prefs),str(a.maxCap),str(a.restTime),str(a.speed) ])
        return pt.get_string()
        
    def tasksToTable(self):
        headers = ["id","time","target position"]
        pt = PrettyTable(headers)
        for t in self.tasks:
            pt.add_row([str(t.id),str(t.time),str(t.target) ])
        return pt.get_string()