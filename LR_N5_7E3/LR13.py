s= "словарь множество неизменяемое"

#st=input('enter string: ').split()
st=list(s.split())
llist = list(map(len,st))
llist_ind=llist.index(max(llist))+1

