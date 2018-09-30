
class Task:
    
    def __init__(self, id, time, target):
        """
        initializes a new task
        
        Arguments:
            id: id of the task : integer
            time: when will the task be published/offered for Agents : integer
            target: target node (city/place) of a task : tuple
        """
        self.id = id
        #self.good = good probably not needed?
        self.time = time
        self.target = target
    
    def toString(self):
        return " Task nr "+str(self.id)+" at the time "+str(self.time)+" to "+str(self.target)
    def show(self):
        print("Task nr",self.id,"at the time",self.time,"to",self.target)
        