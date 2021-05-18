class Graph:
    def __init__(self):
        self.size = 0
        self.adjacentList = {}
    def addVertex(self,node):
        if self.adjacentList.get(node) is None:
            self.adjacentList[node] = []
    def addEdge(self,node1, node2):
        if self.adjacentList.get(node1) is not None and self.adjacentList.get(node2) is not None:
            self.adjacentList[node1].append(node2)
            self.adjacentList[node2].append(node1)
    def showConnections(self):
        for node in self.adjacentList:
            strList = "" + str(node) +" -> "+ " , ".join(self.adjacentList[node])
            print(strList)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')

myGraph.showConnections()
