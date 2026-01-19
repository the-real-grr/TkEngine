class EventQueue: 
    def __init__(self,length,archetype={}): #Initialize event queue
        assert type(archetype) in {dict,list} #Archetypes should be dictionaries or lists in some rare cases
        assert type(length)==int #Length should be an integer.
        assert length>0 #Length should be greater than zero.
        self.length=length
        self.running=True
        self.now=0
        self.newid=0
        self.tasks=[[] for i in range(length)] #Task format:(id,*args)
        self.func=[]
        self.archetype=archetype
    def NewTask(self,tfunc): #Add new task to the function library. Returns its id.
        "Tfunc should not be a class method, but may take class instance as an argument"
        self.func.append(tfunc)
        return len(self.func)-1
    def AddTask(self,dt,tid,*args): #Adds a scheduled task by specifying delay in ticks, task id and arguments (*args)
        self.tasks[(self.now+dt)%self.length].append((tid,args));
    def Tick(self): #Do 1 tick of the event queue
        if self.running:
            for task in self.tasks[self.now]:
                self.archetype=self.func[task[0]](*task[1],archetype=self.archetype) #If this fails, your function may not be executable
            self.tasks[self.now]=[]
            self.now=(self.now+1)%self.length
    def ConfigureArchetype(self,new_archetype): #Change the archetype namespace of this queue
        assert type(new_archetype) in {dict,list} #Archetypes should be dictionaries or lists in some rare cases
        self.archetype=new_archetype
    def GetArchetype(self): #Get the current archetype namespace
        return self.archetype
    def HaltQueue(self): #Moves the task queue as a tuple of parameters from EventQueue to main code. Useful in overload situations.
        "Function library and archetypes will be kept"
        self.running=False
        return (self.queue,self._finish_halt())
    def UnhaltQueue(self,haltexitlog):
        assert type(haltexitlog[1])==int #AND WHAT DO YOU WANT TO SPECIFY???
        self.queue=haltexitlog[0]
        self.now=haltexitlog[1]
        self.running=True
    def _finish_halt(self):
        del self.queue
        self.queue=[[] for i in range(length)]
        return self.now
# A simple demo of an event queue
"""from time import sleep

#Make 3 tasks

def f1(message,archetype={}):
    print(message)
    return archetype
def f2(archetype={}):
    print(archetype["Message"])
    return archetype
def f3(archetype={}):
    archetype["Message"]=input()
    return archetype
Q=EventQueue(10,archetype={"Message":"NONE"})

#Define 3 tasks

F1=Q.NewTask(f1)
F2=Q.NewTask(f2)
F3=Q.NewTask(f3)

#Make a plot

Q.AddTask(1,F1,"TICK LOL") #Task F1 takes one string as argument,
Q.AddTask(2,F1,"Input a message:")
Q.AddTask(2,F3) #But task F3 takes no arguments.
Q.AddTask(3,F1,"I remembered it!")
Q.AddTask(5,F1,"And it is...")
Q.AddTask(6,F2) #Task F2 uses an variable written by F3 in Archetype as a message

#A gameloop

while 1:
    sleep(3)
    Q.Tick()"""
