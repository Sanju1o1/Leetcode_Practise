string = "Helloo"
dic={}
j = 0
end = False
for i in range(len(string)):
    if end:
        exit
    else:
        if string[j] in dic:
            print(j-1)
            end= True
        else:
            dic[string[j]] = j 
            j = j+1
   

