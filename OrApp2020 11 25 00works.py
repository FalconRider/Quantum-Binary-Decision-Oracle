# Copyright 2019 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.



print("")
print("")


print("  The QUANTUM ORACLE - A DECISION INDEPENDANCE SUPPORT PROOF ")
print("---------------------------------------------------------------------")
print("")
title  = input("Decision in regards to :    ")
print("")
# Import networkx for graph tools
#import networkx as nx          TESTING FIX

# using time module 
import time, datetime
from datetime import date
from datetime import datetime
from hashlib import sha256
import random

# ts stores the time in seconds 
ts = time.time()


today = date.today()
print("Decision Requested    ", today)
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("Time:", t)
print ("")  
# print the current timestamp 
print("TimeStamp",ts) 

# Import dwave_networkx for d-wave graph tools/functions
#import dwave_networkx as dnx   TESTING


print(" ")
# Set the solver we're going to use
#from dwave.system.samplers import DWaveSampler TESTING
#from dwave.system.composites import EmbeddingComposite TESTING

#sampler = EmbeddingComposite(DWaveSampler())TESTING

Choice1  = input("Alternative One   ")
print("")
Choice2  = input("Alternative Two   ")



# Create empty graph
#G = nx.Graph()     TESTING

# Add edges to graph - this also adds the nodes
#G.add_edges_from([(3, 4),(1,2)]) TESTING

# Find the maximum independent set, S
# S = dnx.maximum_independent_set(G, sampler=sampler, num_reads=10)TESTING

# Print the solution for the user
#print('Maximum independent set size found is', len(S))
#print(S)
#zz =S[0]   TESTING
zz = random.randint(1,2)     #TESTING
#random.randint(a, b)
#print (zz, "testing")
print("")
print("  ")
print("  ")
print("AS to the Decision in regards to ", title)
print("  ")
print("WHERE AS Alternative One was  " ,Choice1)
print("AND Alternative Two was       ", Choice2) 
print("  ")
print("  ")
print("The DECISION is    ") 

print("******************************************")
if zz ==1:
    print(Choice1)
    decision = Choice1
if zz  == 2:
    print(Choice2)
    decision = Choice2
print("******************************************")   
 



timestamp = ts    # Testing
print ("TIMESTAMPED  ",ts)
#timestamp = 42
#print("testing ts", timestamp)


#hashbase = (Choice1+Choice2 + str(decision) + str(timestamp))
hashbase = (str(Choice1)+str(Choice2) + str(decision) + str(timestamp))
hash = (sha256(hashbase.encode('utf-8')).hexdigest())
#hash = sha256(hashbase)  testing

print("")
print("Cryptografic Certification of Proof :")
print("   ", hash)
print(" ")
print ("------------------------------------------------------------------------- ")


