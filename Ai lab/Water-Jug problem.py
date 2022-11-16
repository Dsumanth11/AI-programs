from collections import defaultdict
J1,J2,aim=4,3,2
visited=defaultdict(lambda:False)
def WJS(A1,A2):
	if (A1==aim and A2==0) or (A2==aim and A1==0):
		print(A1,A2)
		return True
	if visited[(A1,A2)]==False:
		print(A1,A2)
		visited[(A1,A2)]=True
		return (WJS(0,A2) or WJS(A1,0) or WJS(J1,A2) or WJS(A1,J2) or
				WJS(A1+min(A2,(J1-A1)),A2-min(A2,(J1-A1))) or 
                WJS(A1-min(A1,(J2-A2)),A2+min(A1,(J2-A2))))
	else:
		return False
print("Steps: ")
WJS(0,0)