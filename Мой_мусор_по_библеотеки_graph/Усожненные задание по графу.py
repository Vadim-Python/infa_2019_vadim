from graph import*
# def needle():
# 	brushColor("#241c1c")
# 	penColor("#120d0d")
# 	while True:
# 		polygon([(232,496),(274,530),(280,526)])
# Создание тела черепашки
slep = 290
slep1 = 274
slep2 = 311
def forech_igol(x, a, b):
	brushColor("black")
	penColor("#3f0b0b")
	penSize(0.2)
	d = 443
	for i in range(8):
		igol = [(x,530),(a,d),(b,530)]
		polygon(igol)
		x += 15
		a += 15
		b += 15
		d -= 3
	brushColor("#f8690f")
	penColor("#cabdb4")
	circle(300,485,23)
	circle(325,480,23)
	brushColor("red")
	circle(385,473,23)
	brushColor("black")
	penColor("#3f0b0b")
	for i in range(8):
		igol = [(x,527),(a,453),(b - 5,527)]
		polygon(igol)
		x -= 15
		a -= 15
		b -= 15

	x = 400
	a = 445
	b = 410	
	d = 446
	for i in range(8):
		igol = [(x,520),(a,d),(b,520)]
		polygon(igol)
		x -= 15
		a -= 15
		b -= 15
		d += 1

	x = 320
	a = 325
	b = 330
	d = 490
	for i in range(4):
		igol = [(x,530),(a,d),(b,530)]
		polygon(igol)
		x -= 10
		a -= 10
		b -= 10
		d += 2.4
	penColor("#7d7570")
	brushColor("#483737")
def turtle(x1, y1, x2, y2, A, B, C):
	penColor("#7d7570")
	penSize(0.5)
	brushColor("#483737")
	penSize(2)
	# oval(278,534,300,521)
	# oval(285,550,430,480)
	circle(A, B , C) 
	oval(x1, y1, x2, y2)
	#(x1,y1,x2,y2)
	x1+=7;	y1+=16;	x2+=130; y2-=41  
	forech_igol(slep, slep1, slep2)
	oval(x1,y1,x2,y2)
	# oval(285,550,430,480)
	x1+=125;y1-=28;x2+=21;y2+=20
	oval(x1,y1,x2,y2)
	forech_igol(slep,slep1,slep2)
	# needle()
	penColor("#7d7570")
	brushColor("#483737")
	# oval(410,522,451,500)
	x1-=3;y1+=25;x2-=22;y2+=34
	oval(x1,y1,x2,y2)
	# oval(407,547,429,534)
	x1-=116;x2-=115;
	# oval(291,547,314,534)
	oval(x1,y1,x2,y2)
	penSize(0.2)
	brushColor("black")
	circle(440,505,2.5)
	circle(431, 509,3)
	penSize(1.4)
	circle(451,510,2)
# конец тела черепашки
windowSize(500, 600)
brushColor("#2ca05a")
rectangle(0, 0, 500, 250)
brushColor("#6c5d53")
rectangle(0, 252, 500, 600)
penColor("#788374")
penSize(3)
line(0, 251, 500, 251)
penSize(2)
brushColor("#d4aa00")
rectangle(0,   0, 72,  325)
rectangle(100, 0, 225, 585)
rectangle(327, 0, 399, 325)
rectangle(434, 0, 491, 400)
turtle(278,534,300,521,A=430,B=525,C=7,)


# A=430,B=525,R=7
# ?     
# turtle(217,299,242,291 )

run()
