"""
#f = open("C://Vijaya//PyTest.txt","w")  # 'w' - opens the file for write only, if file not exist then it will create new one. if already exists then it will over write it
f=open("C://Vijaya//PyTest.txt","a") # 'a' - means we append the data to the existing file content in the file
f.write("This is sample file created from python prog and appending the data using 'a'-append mode")
f.close() """

f= open("C:\\Vijaya\\PyTest1.txt","r") # 'r' - reads a file, if file not exist then it will throw error
f_out = open("C:\\Vijaya\\PyTest2.txt","w")
for line in f:
    tokens = line.split(' ')
    print(str(tokens))
    f_out.write("Line wordcount-->"+str(len(tokens)) +" line is-->" +line)
f.close()