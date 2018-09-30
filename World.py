
import networkx as nx
import matplotlib.pyplot as plt

class World:
    
    def __init__(self, rows=3, cols=3, agents=[], tasks=[]):
        self.world=nx.grid_2d_graph(rows, cols)
        self.cols = cols
        self.rows = rows
        self.agents = agents
        self.tasks = tasks
        
    def show(self, file_name=""):
        """
        draws the graph with positional labels,
        font size, font color, as well as node size and node color can be modified
        """
        pos = { w: (w[1],w[0]) for w in self.world}
        labels = { w: "("+str(w[1])+","+str(w[0])+")" for w in self.world}
        for k,v in labels.items():
            labels[k] += "\na:"
        for a in self.agents:
            labels[a.pos] += " "+str(a.id)
        for k,v in labels.items():
            labels[k] += "\nt:"
        for t in self.tasks:
            labels[t.target] += " "+str(t.id)
        nx.draw_networkx_labels(self.world,pos=pos,labels=labels, font_size=8, font_color='#ffffff', font_family="serif")
        nx.draw(self.world, pos=pos, with_labels=False,node_size=2000,node_color='#000000')
        if file_name != "":
            plt.savefig("img/"+file_name, format="PNG")
    
