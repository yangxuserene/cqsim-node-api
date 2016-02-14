from sys import argv

def d2xy(self, n, d):
        rx=0
        ry=0
        s=1
        t=d
        x = y = 0
        while(s<n):
            rx = 1 & (t/2)
            ry = 1 & (t ^ rx)
            if ry==0:
                if rx == 1:
                    x = s-1 - x
                    y = s-1 - y    
                x,y = y, x
            x += s * rx
            y += s * ry
            t /= 4
            
            s*=2
        
        return x,y
    
            
def hilbert2d (self, nodestruc_list):
        n=16
        node_num =  len(nodestruc_list)
        nodepool = []
        i = 0
        while(i<node_num):
            x = int(nodestruc_list[i]['location'][0])
            y = int(nodestruc_list[i]['location'][1])
            hil_indx = self.xy2d(n,x,y)
            nodepool.append(hil_indx)
            i+=1
        return nodepool
        
def xy2d(self, n, x, y):
        rx=0
        ry=0
        d=0
        s=n/2
        while s>0:
            rx = (x&s)>0
            ry = (y&s)>0
            d += s*s*((3*rx)^ry)
            if ry==0:
                if rx == 1:
                    x = n-1 - x
                    y = n-1 - y    
                x,y = y, x
            s/=2
        return d 