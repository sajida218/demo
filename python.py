20/02/25

LIST:-
l=["apple","banana","cherry"]
for i in l:
    print(i)


OUTPUT:-
apple
banana
cherry


...Program finished with exit code 0
Press ENTER to exit console.
---------------------------------------------------
ACCESSING ITEMS:-

l=["apple","banana","cherry"]
for i in l:
    print(i)
print(l[1]) 
print(l[1+1])
print(l[0])
print(l[2-1])

OUTPUT:-
apple
banana
cherry
banana
cherry
apple
banana
--------------------------------------------------
ADDING ITEMS:-

APPEND OPEATER (it uses when we need to add single variabel)

l=["apple","banana","cherry"]
print (l)
print("After appending(adding)")
l.append("orange")
print(l)

OUTPUT:-
['apple', 'banana', 'cherry']
After appending(adding)
['apple', 'banana', 'cherry', 'orange']
--------------------------
EXTEND OPETER  (it uses when we have to add multipel values)

l=["apple","banana","cherry"]
print (l)
print("After using extend")
l.extend(["orange","mango"])
print(l)

OUTPUT:-
['apple', 'banana', 'cherry']
After using extend
['apple', 'banana', 'cherry', 'orange', 'mango']
-------------------------------------------------------------
DELETING THE IEMES:-

REMOVE:-

l=["apple","banana","cherry"]
print (l)
l.remove("banana")
print(l)

OUTPUT:-
['apple', 'banana', 'cherry']
['apple', 'cherry']
------------------------------
POP:-
l=["apple","banana","cherry"]
print (l)
l.pop(1)
print(l)

OUTPUT:-
['apple', 'banana', 'cherry']
['apple', 'cherry']
--------------------------------------------------------------
SORTING'S:-
1.SORT
l=["banana","apple","cherry"]
print (l)
l.sort()
print(l)

OUTPUT:-
['banana', 'apple', 'cherry']
['apple', 'banana', 'cherry']
2.REVERES
 
l=["banana","apple","cherry"]
print (l)
l.reverse()
print(l)
OUTPUT:-
['banana', 'apple', 'cherry']
['cherry', 'apple', 'banana']
-------------------------------------------------------------------------------------------
TUPLES:-



t=(10,20,30)
print(t[0])
print(t[1])
print(t[2])
print("using for")
for i in t:
    print(i)
print("finding the length of the tuple")
print(len(t))
print("counting the spesific number in tupule")
print(t.count(20))

OUTPUT:-
10
20
30
using for
10
20
30
finding the length of the tuple
3
counting the spesific number in tupule
1
----------------------------------
CONVERTING LIST to TUPLE

b=1,2,3,
l=list(b)
print(l)
t=tuple(l)
print(t)

OUTPUT:-

[1, 2, 3]
(1, 2, 3)
---------------------------------------------------------
DICTIONARY

ADDIND THE ele IN dic
d={"a":1,"b":2,"c":3}
print(d["b"])
d["d"]=4
print(d["d"])

OUTPUT:-
2
4
------------
DELETING THE ele IN dic

d={"a":1,"b":2,"c":3}
print(d["b"])
d["d"]=4
print(d["d"])
d.pop("b")		#delete the item b
print(d)
print(d.popitem())  	#delete the item lastly inserted
print(d)

OUTPUT:-
{'a': 1, 'c': 3, 'd': 4}
('d', 4)
{'a': 1, 'c': 3}
----------------------------------------------------------
SETS
s={1,2,3,3,}
print(s)

OUTPUT:-
{1,2,3}

l="🎈😁 😂  🤣  😛 "
print(l)
output:-
🎈😁 😂  🤣  😛 