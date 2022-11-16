factskw=[['croaks','frogs'],['eats flies','frogs'],['frogs','green'],['chirp','canary'],['sing','canary'],['canary','yellow']]
def check(str,factDb):
    facts=[]
    flag=True
    while flag==True:
        flag=False
        for txt in str:
            for A1 in factDb:
                if A1[0]==txt:
                    tmp=[txt,A1[1]]
                    if not tmp in facts:
                        facts+=[tmp]
                        str+=[A1[1]]
                        flag=True
    return facts
result=check(['croaks','eats flies'],factskw)
print(result)