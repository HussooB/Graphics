from cs1graphics import*
c=Canvas(1000,500, "white")

#motor
all=Layer()
motor=Layer()

tire1=Layer()

c1=Circle(20)
c1.setFillColor("White")
c1.setBorderColor("black")
c1.setBorderWidth(4)
c1.setDepth(60)
tire1.add(c1)

c2=Circle(5)
c2.setFillColor("black")
tire1.add(c2)

tire1.moveTo(250,250)

r1=Rectangle(43,3)
r1.setFillColor("black")
tire1.add(r1)

r2=Rectangle(3,43)
r2.setFillColor("black")
tire1.add(r2)

motor.add(tire1)

tire2=Layer()

c3=Circle(20)
c3.setFillColor("white")
c3.setBorderColor("black")
c3.setBorderWidth(4)
c3.setDepth(60)
tire2.add(c3)

c4=Circle(5)
c4.setFillColor("black")
tire2.add(c4)

tire2.moveTo(350,250)

r2=Rectangle(43,3)
r2.setFillColor("black")
tire2.add(r2)

r2=Rectangle(3,43)
r2.setFillColor("black")
tire2.add(r2)

motor.add(tire2)

body1=Layer()
r3=Rectangle(80,10)
r3.setFillColor("orange")
r3.setBorderColor("black")
r3.rotate(-30)
r3.moveTo(280,230)
body1.add(r3)

motor.add(body1)

body2=Layer()
r4=Rectangle(70,10)
r4.setFillColor("pink")
r4.setBorderColor("black")
r4.rotate(50)
r4.setDepth(60)
r4.moveTo(330,222)
body2.add(r4)

motor.add(body2)

body3=Layer()
r5=Rectangle(110,5)
r5.setFillColor("chocolate")
r5.setBorderColor("black")
r5.moveTo(300,250)
body3.add(r5)

motor.add(body3)

body4=Layer()
r6=Rectangle(25,5)
r6.setFillColor("orange")
r6.setBorderColor("black")
r6.rotate(45)
r6.moveTo(275,215)
body4.add(r6)
body4.setDepth(70)

motor.add(body4)

sit=Layer()
t1=Polygon()
t1.addPoint(Point(40,30))
t1.addPoint(Point(40,40))
t1.addPoint(Point(50,35))
t1.setFillColor("gray")
t1.setBorderColor("black")
t1.scale(2)
t1.rotate(-15)
t1.moveTo(260,200)
sit.add(t1)
motor.add(sit)

body5=Layer()
r7=Rectangle(8,20)
r7.setFillColor("black")
r7.setBorderColor("white")
r7.moveTo(308,190)
body5.add(r7)
body5.setDepth(100)

motor.add(body5)

body6=Layer()
r8=Rectangle(20,8)
r8.setFillColor("black")
r8.setBorderColor("white")
r8.rotate(-30)
r8.moveTo(308,180)
body6.add(r8)
motor.add(body6)

body7=Layer()
k=tire1.clone()
k.scale(0.5)
body7.add(k)
motor.add(body7)

body8=Layer()
o=tire1.clone()
body8.add(k)
body8.scale(1.5)
body8.moveTo(-80,-125)
motor.add(body8)

body9=Layer()
u=Rectangle(35,3)
u.setFillColor("blue")
body9.add(u)
body9.setDepth(10)
body9.rotate(-15)
body9.moveTo(270,240)
motor.add(body9)

body10=Layer()
u=Rectangle(35,3)
u.setFillColor("blue")
body10.add(u)
body10.setDepth(10)
body10.rotate(15)
body10.moveTo(270,260)
motor.add(body10)
'''
body7=Layer()
t1=Polygon()
t1.addPoint(Point(10,40))
t1.addPoint(Point(40,15))
t1.addPoint(Point(50,40))
t1.setFillColor("light green")
t1.setBorderColor("black")
t1.scale(2)
t1.rotate(5)
t1.moveTo(260,249)
body7.add(t1)
body7.setDepth(60)

motor.add(body7)

body8=Layer()
r9=Rectangle(8,15)
r9.setFillColor("gray")
r9.setBorderColor("white")
r9.moveTo(280,258)
body8.add(r9)
body8.setDepth(60)

motor.add(body8)

body9=Layer()
r10=Rectangle(40,10)
r10.setFillColor("gray")
r10.setBorderColor("white")
r10.moveTo(266,268)
body9.add(r10)

motor.add(body9)
'''
#biker

biker=Layer()

abdomin=Ellipse(20,45)
abdomin.setFillColor("white")
abdomin.moveTo(270,190)
biker.add(abdomin)



head1=Circle(10)
head1.setFillColor("white")
head1.moveTo(270,155)
biker.add(head1)

hand1=Rectangle(23,5)
hand1.setFillColor("white")
hand1.moveTo(290,190)
hand1.rotate(-14)
biker.add(hand1)

hand2=Rectangle(45,5)
hand2.setFillColor("white")
hand2.moveTo(290,178)
hand2.rotate(-10)
biker.add(hand2)

leg1=Rectangle(5,48)
leg1.setFillColor("white")
leg1.moveTo(280,225)
leg1.rotate(-30)
leg1.setDepth(5)
biker.add(leg1)


'''smoke=Layer()

e1=Ellipse(40,8)
e1.setFillColor("gray")
e1.setBorderColor("gray")
e1.moveTo(220,270)
smoke.add(e1)

e2=Ellipse(40,8)
e2.setFillColor("gray")
e2.moveTo(220,270)
e2.rotate(45)
e2.setDepth(90)
e2.setBorderColor("gray")
smoke.add(e2)

e3=Ellipse(40,8)
e3.setFillColor("gray")
e3.moveTo(220,270)
e3.rotate(-45)
e3.setDepth(90)
e3.setBorderColor("gray")
smoke.add(e3)

e4=Ellipse(40,8)
e4.setFillColor("gray")
e4.moveTo(220,270)
e4.rotate(90)
e4.setDepth(90)
e4.setBorderColor("gray")
smoke.add(e4)
smoke.scale(0.5)
smoke.moveTo(120,135)


smoke2=smoke.clone()
smoke2.moveTo(20,60)
smoke2.scale(1.5)


smoke3=smoke.clone()
smoke3.moveTo(-100,-30)
smoke3.scale(2)'''

'''biker2=Layer()

abdomin1=Ellipse(20,45)
abdomin1.setFillColor("black")
abdomin1.moveTo(300,85)
biker2.add(abdomin1)

head2=Circle(10)
head2.setFillColor("black")
head2.moveTo(300,50)
biker2.add(head2)

hand3=Rectangle(30,5)
hand3.setFillColor("black")
hand3.moveTo(285,85)
hand3.rotate(-60)
biker2.add(hand3)

hand4=Rectangle(30,5)
hand4.setFillColor("black")
hand4.moveTo(315,85)
hand4.rotate(60)
biker2.add(hand4)

leg2=Rectangle(5,30)
leg2.setFillColor("black")
leg2.moveTo(295,120)
biker2.add(leg2)

leg3=Rectangle(5,30)
leg3.setFillColor("black")
leg3.moveTo(305,120)
biker2.add(leg3)

biker2.setDepth(40)
biker2.moveTo(-30,330)'''

'''all.add(biker2)'''
motor.add(biker)
all.add(motor)
c.add(all)



'''for i in range(190):
    biker2.move(0,-1)
all.remove(biker2)
motor.add(biker)

for i in range(10):
    motor.move(1,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3,0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)'''
for i in range(500):
    motor.move(5,0)
    leg1.rotate(4)
    tire1.rotate(19)
    tire2.rotate(19)
    leg1.rotate(-4)

