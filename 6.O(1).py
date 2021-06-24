class DS:

    def __init__(self):

        self.arr = []

        self.hashd = {}

    def add(self, x):

        if x in self.hashd:
            return

        s = len(self.arr)
        self.arr.append(x)

        self.hashd[x] = s

    def remove(self, x):
         
        index = self.hashd.get(x, None)
        if index == None:
            return
 
        del self.hashd[x]
 
        size = len(self.arr)
        last = self.arr[size - 1]
        self.arr[index], self.arr[size - 1] = self.arr[size - 1],self.arr[index]
        del self.arr[-1]
 
        self.hashd[last] = index

if __name__=="__main__":
    ds = DS()
    ds.add(10)
    ds.add(20)
    ds.add(30)
    ds.add(40)
    ds.remove(20)
