import ast
import re
from PIL import Image, ImageDraw


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest



From=raw_input("Where are you?: ")
To=raw_input("Destination?: ")
graph_info=open('Map.txt','r')
MapIt=graph_info.read()
MapIt=re.sub(r"[\n\t\s]*", "", MapIt)
Yodlee=ast.literal_eval(MapIt)
count=0
multiple_doors=False
doors=[]
toDoors=[]
fromDoors=[]
path=[0]*40
isTo= False
isFrom= False
both=False
for key in Yodlee:
    if key[:-1]==To or key[:-1]==From:
        count+=1
        if key[:-1]==To:
            isTo = True
            toDoors.append(key)
        if key[:-1]==From:
            isFrom = True
            fromDoors.append(key)
     
if count>1:
    multiple_doors=True
    if isTo and isFrom:
        print "both"
        both=True
    elif isTo:
        From, To=To, From
        doors=toDoors
        doors=list(set(doors))
    else:
        doors=fromDoors
        doors=list(set(doors))



if multiple_doors and not both:
    for door in doors:
        possible_path= find_shortest_path(Yodlee, door, To)
        if len(possible_path)<len(path):
            path=possible_path
elif multiple_doors and both:
    for tdoor in toDoors:
        for fdoor in fromDoors:
            possible_path= find_shortest_path(Yodlee, fdoor, tdoor)
            if len(possible_path)<len(path):
                path=possible_path
    
    
else:
    path= find_shortest_path(Yodlee, From, To)

            
print path
pixel_info=open('Jpixels.txt','r')
pixels=pixel_info.read()
pixels=re.sub(r"[\n\t\s]*", "", pixels)
pixels=ast.literal_eval(pixels)
im=Image.open('Jupiter.png')
draw = ImageDraw.Draw(im)
for i in range(len(path)-1):
    draw.line([pixels[path[i]], pixels[path[i+1]]], fill=128, width=5)
im.show()
