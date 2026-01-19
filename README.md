# TkEngine
The Python game engine for Tkinter.

# DEMO:

#A simple demo of an event queue
from time import sleep
from TkEngine import EventQueue

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
    Q.Tick()
