from SimpleGraphics import*
from math import*
import random
background("deep sky blue")



setFill("white")


ellipse(100,100,500,500)

pointx=random.uniform(100,600)
pointy=random.uniform(100,600)
# pointx=random.uniform(a1-(-a2+pointy)/sqrt(3),a1+(-a2+pointy)/sqrt(3))
# nvertex=random.randint(1, 4)
for i in range(100000):
	i+=1
	vertexx=random.uniform(100,600)
	nvertex=random.randint(1,2)
	vertexy=0
	if nvertex==1:
		vertexy=350-sqrt(250*250-(vertexx-350)**2)
	if nvertex==2:
		vertexy=350+sqrt(250*250-(vertexx-350)**2)
	pointx=(pointx+vertexx)/2
	pointy=(pointy+vertexy)/2
	setFill("black")
	ellipse(pointx,pointy,1,1)
