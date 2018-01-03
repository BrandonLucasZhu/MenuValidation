'''
Created on Dec 30, 2017

@author: Brandon Zhu
'''

import os
import sys
import requests
import json
import pprint

def getAllPages(link):
    
    initialresponse = requests.get(link)
    getTotalPage = json.loads(initialresponse.text)
    
    totalpages = getTotalPage["pagination"]["total"] 
    
    return totalpages

def getAllData(root, storeValues, link):
    
    storedValues = []
    #Go through all pages
    for num_pages in range(1,getAllPages(link)):
        #Iterate through all of the pages 
        totalresponse = requests.get("https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page="+str(num_pages))
        
        #Obtain entire json and store all root node information into one array
        childvalues = json.loads(totalresponse.text)
        storedValues += childvalues[root]
        
        
    return storedValues

def isValidMenu(rootId, checkChildIds, entireMenuData):
    nextId = ""
    queue = [rootId]
    explored = []
    pathChildIdLen = 0;

    while queue:
        
        node = queue.pop(0)
        
        if node not in explored:
            explored.append(node)
            
            #if pathChildIdLen == 0:
            child_ids = entireMenuData[int(node)-1]['child_ids'] #Get last 
            #else:
                
               #child_ids = entireMenuData[int(node[0])-1]['child_ids']

            #pathChildIdLen = len(child_ids)   #Need this to check and iterate all the path options in child_ids as it re-loops
            
            #if len(child_ids) > 0:
                #lastParent = explored[len(explored)-1] #Add last index from explored if there is multiple paths
                #explored.pop(len(explored)-1)#Pop last index
            for child_id in child_ids:
                    #morePaths = []
                    #morePaths.append(lastParent) 
                    #morePaths.append(child_id)
                queue.append(child_id)

            #else:
                #queue.append(child_id)        

    print (explored)    
    return explored                

def isAValidMenu(rootId, end, entireMenuData):
    
    queue = []
    queue.append([rootId])
    #stack = [(int(rootId), [int(rootId)])]
    while queue:
        path = queue.pop(0)
        node = path
        if node == end:
            return path
        for adjacent in entireMenuData[int(node)-1]['child_ids']:
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
            
        #(vertex, path) = stack.pop(0)
        #for next in entireMenuData[vertex-1]['child_ids']:
        #    if next == "":
        #        yield path + [next_node]
        #    else:
        #        stack.append((next,path + [next]))
   
    

if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"

    storeMenus = []
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
    
    #print (entireMenu)
   	

    root_id = ""
    set_validity = [] #sort menu whether if they are valid or not
        
    for i in range(len(entireMenu)):
    	#print (entireMenu[i])
    	if entireMenu[i].get("parent_id") is None:
    		root_id = entireMenu[i]["id"]
        	#print (root_id)

        	for j in range(len(entireMenu[i]["child_ids"])):
                    saveChildId = entireMenu[i]["child_ids"][j]
                    #isValidMenu("2", saveChildId, entireMenu)
                    print isAValidMenu(root_id, "" ,entireMenu)
                    #for val in isAValidMenu( root_id , "" , entireMenu ):
                        #print (val)
                    #[ print (x) for x in isAValidMenu( root_id , "" , entireMenu ) ]

                #print (saveChildId)
            #else:
                #store root_id and begin search through child node menus
                #root_id = entireMenu[i]["id"]
                #saveChildId = entireMenu[i]["child_ids"][j] 
                #print (root_id)    
            #for j in range(len(saveChildId)):    
            #    print (entireMenu[saveChildId[j]])
    
        
    
    
    
    
    
    
    
        

