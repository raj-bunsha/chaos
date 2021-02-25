from SimpleGraphics import*
from math import*
import random
background("deep sky blue")

side=500
a2=100
a1=500
b,c,d=a1-side/2,a1+side/2,a2+side*(sqrt(3)/2)


setFill("pink")
vertex1=(a1,a2)
vertex2=(b,d)
vertex3=(c,d)
print(vertex1,vertex2,vertex3)
polygon(vertex1[0],vertex1[1],vertex2[0],vertex2[1],vertex3[0],vertex3[1])
#polygon(300, 450, 350, 450, 500, 500, 500, 550, 450, 550, 300, 500)
#line(150, 300, 200, 350)
#line(100, 350, 100, 250, 200, 250, 200, 300)
i=0
pointy=random.uniform(a2,d)
pointx=random.uniform(a1-(-a2+pointy)/sqrt(3),a1+(-a2+pointy)/sqrt(3))
for i in range(100000):
	i+=1
	print(pointx,pointy)

	nvertex=random.randint(1,3)
	print(nvertex)
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
	