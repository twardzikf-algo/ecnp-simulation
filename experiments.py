
from Simulation import Simulation

a_1 = { "agents": [ { "id": 0, "pos":(0,0), "prefs":[2,1,0], "maxCap":3, "restTime": 1, "speed": 1 } ],
                "tasks": [ { "id": 0, "time": 0, "target": (2,2) }, 
                           { "id": 1, "time": 1, "target": (1,1) },
                           { "id": 2, "time": 2, "target": (0,0) } ],
                "initiators": [ { "id":0, "task":0 },
                                { "id":1, "task":1 },
                                { "id":2, "task":2 } ],
                "world": {"cols":3, "rows": 3}, "name": "part_a_scenario_1",
                "about": "This is first scenario used to test our ECNP implementation for transport domain. It consists of just 1 agent and three tasks. The tasks come at different times and in the order opposite to preferences of the agent. Additionally task nr. 0 that comes as first, is furthest away from the agent and has lowest priority for him. Since there are no other tasks at time unit nr. 0, agent bids for that task, offering an expected value of 5 (4 units for moving + 1 unit for charging). At following time units additional tasks come, that have higher priority for the agent and are placed nearer to him, so he should include them on his way to task nr. 0, in the end being able to get contracted for all three tasks and still stay at the overall cost of 5.\n This scenario tests ability of our implementation to introduce multiple tasks at different times, and make it possible for at least one agent to bid for them."} 

a_2 = { "agents": [ { "id": 0, "pos":(0,0), "prefs":[1,2], "maxCap":3, "restTime": 1, "speed": 1 },
                            { "id": 1, "pos":(2,2), "prefs":[2,1,0], "maxCap":3, "restTime": 1, "speed": 1 },
                            { "id": 2, "pos":(2,2), "prefs":[2,1], "maxCap":4, "restTime": 1, "speed": 2 }],
                "tasks": [ { "id": 0, "time": 0, "target": (0,0) }, 
                           { "id": 1, "time": 0, "target": (2,2) },
                           { "id": 2, "time": 0, "target": (1,0) } ],
                "initiators": [ { "id":0, "task":0 },
                                { "id":1, "task":1 },
                                { "id":2, "task":2 } ],
                "world": {"cols":3, "rows": 3}, "name": "part_a_scenario_2",
                "about": "In the second scenario we increase the number of agents to three. Two of them don't have task nr. 0 in their preferences, so they should not bid for that task as well as get contracted for it. Furthermore agents are no more equal in their parameters. Agent nr. 2 is able to move more fields in one move and has also bigger capacity, which should help him offer better bids even for tasks placed further away.\n This scenario tests the ability of our impementation to simulate correct bidding between more than one agent for multiple tasks. It also shows the influence of agent's parameters on the bidding process (ability to offer better/lower values)."}  

a_3 = { "agents": [ { "id": 0, "pos":(0,0), "prefs":[0], "maxCap":3, "restTime": 1, "speed": 1 },
                            { "id": 1, "pos":(6,6), "prefs":[0], "maxCap":2, "restTime": 1, "speed": 2 },
                            { "id": 2, "pos":(6,0), "prefs":[0], "maxCap":3, "restTime": 2, "speed": 2 },
                            { "id": 3, "pos":(0,6), "prefs":[0], "maxCap":4, "restTime": 1, "speed": 1 }],
                "tasks": [ { "id": 0, "time": 0, "target": (3,3) } ],
                "initiators": [ { "id":0, "task":0 }],
                "world": {"cols":7, "rows": 7}, "name": "part_a_scenario_3",
                "about": "Third scenario  goes more into detail in exploring the influence of different agent's parameters on the bidding possibilites. In the 7x7 wgrid four agents are placed in four corners of the grid while the task is in the middle on the grid. Differently parametrized agents compete to offer the best bid for that task." }

b_2 = { "agents": [ { "id": 0, "pos":(0,0), "prefs":[1,2,3,4,5], "maxCap":2, "restTime": 1, "speed": 1 },
                            { "id": 1, "pos":(2,2), "prefs":[2,1,0,5,4,3], "maxCap":2, "restTime": 1, "speed": 1 },
                            { "id": 2, "pos":(3,0), "prefs":[5,4,3,2,1,0], "maxCap":2, "restTime": 1, "speed": 2 }],
                "tasks": [ { "id": 0, "time": 0, "target": (0,0) }, 
                           { "id": 1, "time": 0, "target": (3,2) },
                           { "id": 2, "time": 1, "target": (1,0) },
                           { "id": 3, "time": 1, "target": (0,3) }, 
                           { "id": 4, "time": 2, "target": (2,2) },
                           { "id": 5, "time": 2, "target": (1,0) }],
                "initiators": [ { "id":0, "task":0 },
                                { "id":1, "task":1 },
                                { "id":2, "task":2 },
                                { "id":3, "task":3 },
                                { "id":4, "task":4 },
                                { "id":5, "task":5 }],
                "world": {"cols":4, "rows": 4}, "name": "part_b_scenario_2",
                "about": "" }

b_1 = { "agents": [ { "id": 0, "pos":(0,0), "prefs":[2,0,1], "maxCap":2, "restTime": 1, "speed": 1 },
                            { "id": 1, "pos":(0,4), "prefs":[2,0,1], "maxCap":2, "restTime": 1, "speed": 1 }],
                "tasks": [ { "id": 0, "time": 0, "target": (3,0) }, 
                           { "id": 1, "time": 0, "target": (3,4) },
                           { "id": 2, "time": 1, "target": (2,2) }],
                "initiators": [ { "id":0, "task":0 },
                                { "id":1, "task":1 },
                                { "id":2, "task":2 }],
                "world": {"cols":5, "rows": 5}, "name": "part_b_scenario_1",
                "about": "In this scenario we aim to construct a situation, where at least 3 rounds of bidding are needed to find an unequivocal contractor. For this purpose we defined a 5x5 grid world with 2 agents placed in the bottom corners of the grid. There are 3 tasks to be done, nr 0 and 1 at time 0, and task nr 2 at time 1. First both agents give offers for tasks 0 and 1. Rejection in case of task 0 for agent 1 means, that he can offer a better bid for task nr. 1. This results in pre rejection of bid for task 1 for agent 0." }

s = Simulation( b_1 )
s.simulate()


