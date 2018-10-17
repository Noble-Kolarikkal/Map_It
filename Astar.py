graph_info=open('Graph.txt','r')
ip=graph_info.read()
inputs=ip.split('\n')

no,no2=map(int,inputs[0].split())
S,G=inputs[1].split()
current = S
openq={}
close={}
closed=[]
heu={}
for i in range(no+2+no2,len(inputs)-1):
                heu_vals=list(inputs[i].split())
                heu[heu_vals.pop(0)]=int(heu_vals.pop())


openq[S]=heu[S]
close[S]=heu[S]
while(True):
        for i in range(no+2,no+2+no2):
            node_char=inputs[i].split()
            if (node_char[0]== current):
                    if(node_char[1] not in openq):
                        openq[node_char[1]]=int(node_char[2])+close[current]+heu[node_char[1]]-heu[current]
                    else:
                        if(int(node_char[2])+close[current]+heu[node_char[1]]-heu[current]<openq[node_char[1]]):
                            openq[node_char[1]]=int(node_char[2])+close[current]+heu[node_char[1]]-heu[current]
        print "Open:",openq
        to_close=min(openq, key=openq.get)
        close[to_close]=min(openq.values())
        current=to_close
        print "Close:",close
        print "----------------------------------------------------------------"
        openq.pop(to_close)
        closed.append(to_close)
        if(to_close==G):
            print close[to_close]
            print closed
            break

