graph_info=open('Graph.txt','r')
ip=graph_info.read()
inputs=ip.split('\n')

node_char=inputs[0].split()
no=int(node_char[0])
no2=int(node_char[1])
current = "S"
openq=['S']
close=[]
while('G' not in openq):
        for i in range(no+2,no+2+13):
                node_char=inputs[i].split()
                if (node_char[0]== current and node_char[1] not in openq):
                        openq.append(node_char[1])
        close.append(openq[0])
        openq.pop(0)
        current=openq[0]
        print "Open:",openq
        print "------------------------------------------------------------"
close.append('G')
print "Close:",close
