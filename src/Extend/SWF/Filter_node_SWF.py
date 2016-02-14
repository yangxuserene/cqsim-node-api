import re
import Filter.Filter_node as filter_node

__metaclass__ = type
class Filter_node_SWF(filter_node.Filter_node):
    
        
        
    def show_module_info (self):
        self.myInfo += " [SWF]"
        #self.debug.line(1," ")
        self.debug.debug("-- "+self.myInfo,1)   
        
    def reset_config_data(self):
        self.config_start=';'
        self.config_sep='\\n'
        self.config_equal=': '
        self.config_data=[]
        self.config_data.append({'name_config':'MaxNodes','name':'MaxNodes','value':''})
        self.config_data.append({'name_config':'MaxProcs','name':'MaxProcs','value':''})
        
    def read_node_struc(self):
        nr_sign =';'    # Not read sign. Mark the line not the job data
#         sep_sign =' '   # The sign seperate data in a line
#         sep_sign2 =':'   # The sign seperate data in a line
        nameList=[]
        nameList.append(["MaxNodes","node"])
        nameList.append(["MaxProcs","proc"])
        regex_rest = " *: *([^\\n ]+)[\\n ]"
        regexList = []
        node_info={}
        
        for dataName in nameList:
            regexList.append([(dataName[0]+regex_rest),dataName[1]])
        
        nodeFile = open(self.struc,'r')
        while (1): # find the node number and processor number in .swf file
            tempStr = nodeFile.readline()
            if not tempStr :    # break when no more line
                break
            if tempStr[0] == nr_sign:   # The information line
                for dataRegex in regexList:
                    matchResult = re.findall(dataRegex[0],tempStr)
                    if (matchResult):
                        node_info[dataRegex[1]]=int(matchResult[0].strip())
                        break
                for con_data in self.config_data:
                    con_ex = con_data['name']+self.config_equal+"([^"+self.config_sep+"]*)"+self.config_sep
                    temp_con_List=re.findall(con_ex,tempStr)
                    if (len(temp_con_List)>=1):
                        con_data['value'] = temp_con_List[0]
                        break
            else:
                break
        nodeFile.close()
        self.node_data_build(node_info)
        self.nodeNum = {}
        self.nodeNum['proc'] = node_info['proc']
        self.nodeNum['node'] = node_info['node']
        
               
        
    def node_data_build(self,node_info):
        node_num = node_info['proc']# Num_Proc == Num_Node Xu Yang
        self.nodeList=[]
        i = 0
        while (i < node_num): 
#             list = self.get_location_2d(i)           
            list = self.get_location_3d(i)
            self.nodeList.append({"id": i+1, \
                                  "location": list, \
                                  "group": 1, \
                                  "state": -1, \
                                  "proc": 1, \
                                  "start": -1, \
                                  "end": -1, \
                                  "extend": None})
            i += 1        
        return 1

    
    def get_location_3d(self, id):
        '''
        this is for topology-aware
        Xu Yang
        '''
#         self.dim_x = 4
#         self.dim_y = 4
#         self.dim_z = 4
#         
#         self.dim_x = 8
#         self.dim_y = 8
#         self.dim_z = 8

        self.dim_x = 16
        self.dim_y = 16
        self.dim_z = 16
        
#         self.dim_x = 32
#         self.dim_y = 32
#         self.dim_z = 32
        
#         self.dim_x = 64
#         self.dim_y = 64
#         self.dim_z = 64
        
        '''
        this is for topology-aware
        '''
        coord_list = []
        for k in range(self.dim_z):
            for j in range(self.dim_y):
                for i in range(self.dim_x):
                    if (id == k*self.dim_x*self.dim_y + \
                        j*self.dim_x +i):
                        coord_list.append(i)
                        coord_list.append(j)
                        coord_list.append(k)
                        return coord_list 
     
    
    def get_location_2d(self, id):
        '''
        this is for topology-aware
        Xu Yang
        '''
        self.dim_x = 16
        self.dim_y = 16
        
        
        '''
        this is for topology-aware
        '''
        coord_list = []
        for j in range(self.dim_y):
            for i in range(self.dim_x):
                if (id == j*self.dim_x +i):
                    coord_list.append(j)
                    coord_list.append(i)
                    return coord_list 
     

    
    
    
    
    def output_node_data(self):
        if not self.save:
            print "Save file not set!"
            return
        
        sep_sign = ";"
        f2=open(self.save,"w")
        for nodeResult_o in self.nodeList:
            f2.write(str(nodeResult_o['id']))
            f2.write(sep_sign)
            f2.write(str(nodeResult_o['location']))
            f2.write(sep_sign)
            f2.write(str(nodeResult_o['group']))
            f2.write(sep_sign)
            f2.write(str(nodeResult_o['state']))
            f2.write(sep_sign)
            f2.write(str(nodeResult_o['proc']))
            f2.write("\n")
        f2.close()

    def output_node_config(self):
        '''
        This is node configuration file. It contains only node and processor number now.
        
        So If topology information is need, like torus or fattree, should be added here
        and written in to the xxx_node.con file
        
        XU YANG 
        '''
        if not self.config:
            print "Config file not set!"
            return
        
        format_equal = '='
        f2=open(self.config,"w")
        for con_data in self.config_data:
            f2.write(str(con_data['name_config']))
#             print con_data['name_config']
            f2.write(format_equal)
            f2.write(str(con_data['value']))
#             print con_data['value']
            f2.write('\n')
        f2.close()
        
        
        
        
        
        
        
        
        