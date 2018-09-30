# Extended Contract Net Protocol Simulation in Python
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://opensource.org/licenses/MIT)

## ECNP

Extended Contract Net Protocol is a protocol from the task sharing domain. It allows for a set of agents to offer tasks to other agents in order to bid for them with the objective to solve all tasks with respect to the agents own preferences. The world is represented as a grid on which agents and tasks are placed and agents can move for *x* cells at once *n* times before rest is needed, both parameters being given in the setup dictionary. Each agent has its own priorities and each task has a deadline. For further informations see [What is Contract Net Interaction Protocol?](http://www2.ensc.sfu.ca/research/iDEA/courses/files/Contract%20Net%20Protocol1.pdf).

## Configuration
Simulation setup is realised in experiments.py file which contains apropriate method calls to carry out the simulation as well as quite many ready setups as python dictionaries with following structure:

- **agents**: list of dictionaries each being a set of attributes defining an agent (id, starting cell, preferences, max capacity, resting time and speed)
- **tasks**: list of dictionaries each being a set of attributes defining a task (id, time, target cell)
- **initators**: list of dictionaries each being a set of attributes defining an initiator (id, task id)
- **world**: a dictionary containing a set of attributes defining the world (amount of columns and amount of rows)
- **name**: name of the runtime protocol file
- **about**: a textdescribing the simulation that appears in the runtime protocol file


## Implementation

My python implementation of the protocol consists of following classes: *Agent*, *Initiator*, *Task*, *World* and *Simulation*.

- *World*: used to generate a static grid world as a model for Agents to calculate routes as well as a visual represenation image for the pdf runtime raport.
- *Task*: pure entity class representing a single task and its attributes. 
- *Agent*: class representing an agent - participant. Implements communication with Initiators and calculating routes and bids.
- *Initiator*: class representing an agent - task initiator. Implements gathering and evaluating bids from agents as well as reacting with respective answers.
- *Simulation* main class that takes a  dictionary as a simulation setup and basing on it creates initiators, agents, tasks and carries out the simulation. Additionally it saves all changes to the state of simulation to a pdf file resulting in a runtime protocol.

Runtime protocols are saved as pdf files in /protocols. Images of the grids are saved as pnf files in /img.

**Libraries used: [matplotlib](https://github.com/matplotlib/matplotlib), [networkx](https://github.com/networkx), [prettytable](https://github.com/vishvananda/prettytable), [pdfrw](https://github.com/pmaupin/pdfrw), [fpdf](https://github.com/reingart/pyfpdf)**


