import Hilbert3D
import Hilbert2D



def inter_freg (freg, proc):
    freg = float(freg)
    proc = float(proc)
    f1= open("/Users/xu/Documents/workspace/Cqsim/data/Results/Inner_Freg.csv", "a")
#     f1.write(str(freg))
#     f1.write("    ")
#     f1.write(str(proc))
#     f1.write("    ")
    f1.write(str.format('{0:.3f}', freg/proc))
    f1.write("\n")
       
    f1.close()
        
    return


def avg_pairwise_dis_Hilbert3D(alloc_list, Hilbert3d_location):
        
        i=0 
        location = []
        
        while (i<len(alloc_list)):
            h_index = alloc_list[i]
            coord = {"dim_x":-1, "dim_y":-1, "dim_z": -1}
            temp_coord = []
            temp_coord = Hilbert3d_location[h_index]
             
            coord["dim_x"] = temp_coord[0]
            coord["dim_y"] = temp_coord[1]
            coord["dim_z"] = temp_coord[2]
            location.append(coord) 
            i+=1
        
            
        sep_sign = "\t"
        f1= open("/Users/xu/Documents/workspace/Cqsim/data/Results/avg_pairwise_dis_Hilbert3D.csv", "a")
   
   
#         k=0
#         while(k<len(alloc_list)):
#             f1.write(str(alloc_list[k]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_x"]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_y"]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_z"]))
#             f1.write("\n")
#                             
#             k+=1
#         f1.write("\n\n")
         
        diameter = 0
        w=0
        l=0
        h=0
        mahantan_dis = 0
        i = 0
        while (i<len(location)):
            j=0 
            for j in range(len(location)):
                mahantan_dis += abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))+\
                                abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))+\
                                abs(int(location[i]["dim_z"])-int(location[j]["dim_z"]))
            
                if w< abs(int(location[i]["dim_x"])-int(location[j]["dim_x"])):
                    w =  abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))
                      
                if l< abs(int(location[i]["dim_y"])-int(location[j]["dim_y"])):
                    l =  abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))
                      
                if h< abs(int(location[i]["dim_z"])-int(location[j]["dim_z"])):
                    h =  abs(int(location[i]["dim_z"])-int(location[j]["dim_z"]))
       

            
            
            mahantan_dis /= len(alloc_list)  
            i += 1
        f1.write(str(mahantan_dis))
        f1.write("\n")
        f1.close()
         
      
        diameter = w+l+h
        max_dim = max(w,l,h) 
        f3= open("/Users/xu/Documents/workspace/Cqsim/data/Results/diameter_Hilbert3D.csv", "a")
        f2= open("/Users/xu/Documents/workspace/Cqsim/data/Results/max_dim_Hilbert3D.csv", "a")
        
        f3.write(str(diameter))
        f3.write("\n")
        f2.write(str(max_dim))
        f2.write("\n")
        f3.close()
        f2.close()
        

#         return mahantan_dis

#         return max_dim
         
        return diameter
            

    
  
def avg_pairwise_dis_DimenOrder3D(alloc_list, Rowcol_location):
        
        k=0
        location = []
        while(k<len(alloc_list)):
            d_index = alloc_list[k]
            coord = {"dim_x":-1, "dim_y":-1, "dim_z": -1}
            temp_coord = []
            temp_coord = Rowcol_location[d_index]             
            coord["dim_x"] = temp_coord[0]
            coord["dim_y"] = temp_coord[1]
            coord["dim_z"] = temp_coord[2]
            location.append(coord) 
            k+=1           
        
        sep_sign = "\t"
        f1= open("/Users/xu/Documents/workspace/Cqsim/data/Results/avg_pairwise_dis_DimenOrder3D.csv", "a")
                   
#         k=0
#         while(k<len(location)):
#             f1.write(str(alloc_list[k]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_x"]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_y"]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_z"]))
#             f1.write("\n")
#                             
#             k+=1
#         f1.write("\n\n")
#         f1.close()
 
        diameter =0
        w=0
        l=0
        h=0
        mahantan_dis = 0
        i = 0
        while (i<len(location)):
            j=0 
            for j in range(len(location)):
                mahantan_dis += abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))+\
                                abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))+\
                                abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))
                
                if w< abs(int(location[i]["dim_x"])-int(location[j]["dim_x"])):
                    w =  abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))
                       
                if l< abs(int(location[i]["dim_y"])-int(location[j]["dim_y"])):
                    l =  abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))
                       
                if h< abs(int(location[i]["dim_z"])-int(location[j]["dim_z"])):
                    h =  abs(int(location[i]["dim_z"])-int(location[j]["dim_z"]))
        

                
            mahantan_dis /= len(alloc_list) 
            i += 1
        f1.write(str(mahantan_dis))
        f1.write("\n")
        f1.close()
         

            
        diameter = w+l+h
        max_dim = max(w,l,h) 
        f3= open("/Users/xu/Documents/workspace/Cqsim/data/Results/diameter_DimenOrder3D.csv", "a")
        f2= open("/Users/xu/Documents/workspace/Cqsim/data/Results/max_dim_DimenOrder3D.csv", "a")
         
        f3.write(str(diameter))
        f3.write("\n")
        f2.write(str(max_dim))
        f2.write("\n")
        f3.close()
        f2.close()
        
        
#         return mahantan_dis

#         return max_dim
         
        return diameter
        

  
  
  
    
def avg_pairwise_dis_Hilbert2D(self, alloc_list):
        
    i=0
    n=16 
    location = []
    
    while (i<len(alloc_list)):
        d = alloc_list[i]
        coord = {"dim_x":-1, "dim_y":-1}
        x,y = Hilbert2D.d2xy(n, d)(n, d)
        coord["dim_x"] = x
        coord["dim_y"] = y
        location.append(coord) 
        i+=1

    sep_sign = "\t"
    f1= open("/Users/xu/Documents/workspace/Cqsim/data/Results/avg_pairwise_dis_Hilbert2D.csv", "a")
 


    k=0
    while(k<len(alloc_list)):
        f1.write(str(alloc_list[k]))
        f1.write(sep_sign)
        f1.write(str(location[k]["dim_x"]))
        f1.write(sep_sign)
        f1.write(str(location[k]["dim_y"]))
        f1.write("\n")
                     
        k+=1
    f1.write("\n\n")
        
        
#         mahantan_dis = 0
#         i = 0
#         while (i<len(location)):
#             j=0 
#             for j in range(len(location)):
#                 mahantan_dis += abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))+\
#                                 abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))
#             
#             mahantan_dis /= len(alloc_list)  
#             i += 1
#         f1.write(str(mahantan_dis))
#         f1.write("\n")
        
    f1.close()
        
    return
  
    
def avg_pairwise_dis_DimenOrder2D(self, alloc_list):
        
        k=0
        n=16
        location = []
        while(k<len(alloc_list)):
            coord = {"dim_x":-1, "dim_y":-1}
            for j in range(n):
                for i in range(n):
                    if (alloc_list[k] == i*n +j):
                        coord["dim_x"] = i
                        coord["dim_y"] = j
                        location.append(coord)
            k+=1           
        
        self.avg_pair_wise(alloc_list, location)
        sep_sign = "\t"
        f1= open("/Users/xu/Documents/workspace/Cqsim/data/Results/avg_pairwise_dis_DimenOrder3D.csv", "a")
                                        
#         k=0
#         while(k<len(alloc_list)):
#             f1.write(str(alloc_list[k]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_x"]))
#             f1.write(sep_sign)
#             f1.write(str(location[k]["dim_y"]))
#             f1.write("\n")
#                         
#             k+=1
#         f1.write("\n\n")

        mahantan_dis = 0
        i = 0
        while (i<len(location)):
            j=0 
            for j in range(len(location)):
                mahantan_dis += abs(int(location[i]["dim_x"])-int(location[j]["dim_x"]))+\
                                abs(int(location[i]["dim_y"])-int(location[j]["dim_y"]))
            
            mahantan_dis /= len(alloc_list) 
            i += 1
        f1.write(str(mahantan_dis))
        f1.write("\n")
         
        f1.close()
        
        return
    
    
