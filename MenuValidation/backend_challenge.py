'''
Created on Dec 30, 2017

@author: Brandon Zhu
'''

import os
import sys
import requests
import json
import pprint
import copy
import collections

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

#Function for searching all paths
def exploringGraph(start, graph,end, root, path = []):
    
    path = path + [start]

    if start == end:
        return [path]
    
    
    for checkChildId in graph[start]:
        #Break search if next node is an end
        if checkChildId == "end":
            break

        for check in graph[checkChildId]:
            if check  == root:
        #Check if the node goes back to root
            
                path.append(checkChildId)
                path.append(root)
                return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = exploringGraph(node,graph,end,root,path)
           
            for newpath in newpaths:
                paths.append(newpath)
   


    return paths

def findDuplicate (checkinglist, loopedtwice):
    unique = set(checkinglist)
    if len(unique) != len(checkinglist):
        return True
    else:
        return False                             

if __name__ == "__main__":
     
    #Get total amount of pages in API link
    linkpages = "https://backend-challenge-summer-2018.herokuapp.com/challenges.json?id=1&page=1"
    storeMenus = []
    storeMenusNodes = {}
    
    #Get all Data for Menu's 
    entireMenu = getAllData("menus", storeMenus, linkpages)
    
   

    root_id = ""
    set_validity = [] #sort menu whether if they are valid or not
    store_rootId = []

    #Create a hashmap of the graphing api
    for i in range(len(entireMenu)):
    
        if entireMenu[i].get("parent_id") is None:
            root_id = entireMenu[i]["id"]
            store_rootId.append(str(root_id))
          

            for j in range(len(entireMenu[i]["child_ids"])):
                saveChildId = entireMenu[i]["child_ids"][j]
                if str(root_id) in storeMenusNodes: 
                    storeMenusNodes[str(root_id)].append(str(saveChildId))  
                else: 
                        storeMenusNodes[str(root_id)] = [str(saveChildId)]    
        else:
            current_id = entireMenu[i]["id"]
            if len(entireMenu[i]["child_ids"]) is 0:
                storeMenusNodes[str(current_id)] = ["end"]
            else:    
                for j in range(len(entireMenu[i]["child_ids"])):
                        saveChildId = entireMenu[i]["child_ids"][j]
                       
                        if str(current_id) in storeMenusNodes: 
                            storeMenusNodes[str(current_id)].append(str(saveChildId))
                        else: 
                            storeMenusNodes[str(current_id)] = [str(saveChildId)]

    #Set up and store onto json file
    json_file = {}
    valid_menus = []
    invalid_menus = []
    json_file["valid_menus"] = valid_menus
    json_file["invalid_menus"] = invalid_menus
    for root in store_rootId:
        menu_node = exploringGraph(root,storeMenusNodes,"end",root)
        
        for nodeValues in menu_node:
            
            if findDuplicate(nodeValues,root):
                storeInvalid = {}
                storeInvalid["root_id"] = root
                nodeValues.pop(0)
                storeInvalid["children"] = nodeValues
                json_file["invalid_menus"].append(storeInvalid)
            
            else:
                storeValid = {}
                storeValid["root_id"] = root
                nodeValues.pop(0)
                nodeValues.pop(len(nodeValues)-1)
                storeValid["children"] = nodeValues
                json_file["valid_menus"].append(storeValid) 
    
    
    with open('data.json', 'w') as dataMenu:
        data = json.dumps(json_file,indent = 4)
        desiredResult = json.dump(data, dataMenu)

    print (data)



                
    
        
    
    
    
    
    
    
    
        

