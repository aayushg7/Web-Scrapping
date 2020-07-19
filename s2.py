try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
l= []
l.append('Asanka Abeysinghe')
l.append('Tania allard')
k = []
# to search
for i in range(len(l)):
    query = l[i]
    for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
        k.append(j)
print(k)

