# l=[x for x in range(11)]   #1
# #print (l)
# e=o=0
# for x in l:
#     if x == 0: continue
#     elif x % 2 == 0: e+=1
#     else: o+=1
# print("e= ",e,"o= ",o)

# print(input("enter string")[::-1]) #2

# dic={"a":1,"b":2}     #3
# print( (input("enter a key to find: ") in dic.keys()) and 'already in' or 'not in ')

# l=['abc','abcdfe','abcdfe','abcdefg']   #5
# n=int(input("Enter a max len"))
# for x in l :
#     if len(x) >= n: print(x)
#     else: print('nthng of the len')


# l1=[[1],[],[1,2]]                 #6
# for x in l1:
#     if len(x) == 0: print("list empty")
#     else: print("not empty")

#print(list(set([1,2,2,3,7,7,8,8]))) #7


# s=input("enter str").split()        #8
# d={x:s.count(x) for x in s}
# print(d)

# d={x:len(x) for x in s}           #9 simple
# print(d)
# print(max(s,key=len)) #only one o/p,multiple words same len dont fetch

# words=set("hai there hai there hello".split(" ")) #9 proper
# max_len= len(max(words,key=len))
# print([x for x in words if len(x)==max_len])

# ch="haii"    #10
# d={x:ch.count(x) for x in ch if x != " "}
# print(d)

# l=["hai","there","sid"]   #11
# #s="".join(l)         #o/p: no space among words
# print(" ".join(l))   #str_to_join.join(iterable) returns string

# l=[1,2,3]                   #12
# n=int(input("enter value to search"))
# if n in l : print( l.index(n)) #list.index(elem,[start,[end]]) returns first occurence of elem in list
#                                 #12 short_hand
# print(int(input("enter value to search")) in l and 'already in' or 'not in')


#print(int(input("enter a number:-")[::-1])) #13

