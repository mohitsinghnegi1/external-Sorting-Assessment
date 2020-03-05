import os
import tempfile
import heapq
import sys
class externalSorting(object):
    def __init__(self):
        self.sorted_file_handlers=[]
        self.cwd=os.getcwd()
        self.fout=None

    def printTemporaryFiles(self):
        file_number=1
        #here we are using each file discriptor and reaing content of each file
        #after that we are moving to pos 0
        for i in self.sorted_file_handlers:
            print "--------file number : ",file_number,"file name : ",i.name.split('\\')[-1],"--------"
            print i.read()
            i.seek(0)
            file_number+=1
        print ""

    def printSotedOutputFile(self):
        
        print self.fout.read()
        print ""
    
    def splitFilesInSorted(self,input_file,chunck_size):
        
        #ifh - input file handler
        #tmep_buffer will store lines of input_file
        temp_buffer=[]
        size=0
        
        
        with open(input_file) as ifh:
            line=ifh.readline()
            i=0
            while len(line)>0:
                #adding each line to the temp_buzzer until its size becomes
                #equal to chunk size
                temp_buffer.append(line)
                line=ifh.readline()
            
                size+=1
                if(size%chunck_size==0 or len(line)==0 and temp_buffer!=[]):
                    #now time to sort the temp buffer
                    #after sorting buffer we keep it into new chuck file in sorted order
                    temp_buffer.sort(key=lambda x: x.strip())
                    
                    #a new file will be createdss
                    fh1=tempfile.NamedTemporaryFile(dir=self.cwd+'/temp',delete=False)
                    fh1.writelines(temp_buffer)
                    print temp_buffer
                    #this will create a chunk file with sorted data
                    fh1.seek(0)
                    self.sorted_file_handlers.append(fh1)
                    temp_buffer=[]

    def mergeFiles(self):
        #now perform k way merge
        min_array=[]#this array we will use for heap
        heapq.heapify(min_array)
        fout=open('outputSortedfile.txt','w+') 
        while(True):
            min1=None
            for i in self.sorted_file_handlers:
                #for each file handler we are inserting their min values into heap
                line=i.readline().strip()#strip is used to remove extra padding and new line char
                if len(line)>0 :
                    min1=len(line)
                    heapq.heappush(min_array,line)
                else:
                    continue
                        
            if(min1==None):
                break
        
        while(min_array!=[]):
            fout.write(heapq.heappop(min_array))
            fout.write("\n")
        fout.seek(0)
        self.fout=fout
        

if __name__=='__main__':
    input_file='inputFile.txt'
    chunck_size=3
    obj=externalSorting()#create object form 
    obj.splitFilesInSorted(input_file,chunck_size)

    obj.mergeFiles()
    obj.printSotedOutputFile()
    #obj.fout.close()
    
    
