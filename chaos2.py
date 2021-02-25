from SimpleGraphics import*
from math import*
import random
background("deep sky blue")

side=500
a2=50
a1=100
b,c,d=a1-side/2,a1+side/2,a2+side*(sqrt(3)/2)


setFill("pink")
vertex1=(a1,a2)
vertex2=(a1+side,a2)
vertex3=(a1+side,a2+side)
vertex4=(a1,a2+side)
polygon(vertex1[0],vertex1[1],vertex2[0],vertex2[1],vertex3[0],vertex3[1],vertex4[0],vertex4[1],vertex1[0],vertex1[1])
#polygon(300, 450, 350, 450, 500, 500, 500, 550, 450, 550, 300, 500)
#line(150, 300, 200, 350)
#line(100, 350, 100, 250, 200, 250, 200, 300)
i=0
pointy=random.uniform(a2,d)
pointx=random.uniform(a1-(-a2+pointy)/sqrt(3),a1+(-a2+pointy)/sqrt(3))
nvertex=random.randint(1, 4)
for i in range(100000):
	i+=1
	while True:
		nvertex1=random.randint(1,4)
		if nvertex1!=nvertex:
			nvertex=nvertex1
			break
	setFill("black")
	ellipse(pointx,pointy,1,1)
	if nvertex==1:
		pointx=(vertex1[0]+pointx)/2
		pointy=(vertex1[1]+pointy)/2
	if nvertex==2:
		pointx=(vertex2[0]+pointx)/2
		pointy=(vertex2[1]+pointy)/2
	if nvertex==3:
		pointx=(vertex3[0]+pointx)/2
		pointy=(vertex3[1]+pointy)/2
	if nvertex==4:
		pointx=(vertex4[0]+pointx)/2
		pointy=(vertex4[1]+pointy)/2
	
