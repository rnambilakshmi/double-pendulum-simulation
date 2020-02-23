GlowScript 2.6 VPython
scene.userzoom = False 

#parameters
L1=0.5
L2=0.3
k1=1
k2=20000000000 # approximation for massless rod
M1=0.12
M2=0.03
g=vector(0,-9.8,0)
theta1=20*pi/180
theta2=40*pi/180
theta1dot=0
theta2dot=0

#static animation - only rods and balls
pivot=sphere(pos=vector(0,L1,0), radius=0.05)
m1=sphere(pos=pivot.pos-vector(0,L1,0),radius=M1,color=color.red)
stick1=cylinder(pos=pivot.pos,axis=m1.pos-pivot.pos,radius=0.015,color=color.yellow)
m2=sphere(pos=m1.pos-vector(0,L2,0),radius=M2,color=color.red)
stick2=cylinder(pos=m1.pos, axis=m2.pos-m1.pos, radius=0.015,color=color.yellow)

#defining positions
m1.pos=pivot.pos+vector(L1*sin(theta1),-L1*cos(theta1),0)
m2.pos=m1.pos+vector(L2*sin(theta2),-L2*cos(theta2),0)
stick1.axis=m1.pos-pivot.pos
stick2.pos=m1.pos
stick2.axis=m2.pos-m1.pos

m1.p=vector(0,0,0)
m2.p=vector(0,0,0)
m1.m=M1
m2.m=M2

t=0
dt=0.00001

attach_trail(m2, retain=200)

# loop uptil time = 20s
while t<20:
    rate(100000)
    r1=m1.pos-pivot.pos
    r2=m2.pos-m1.pos
    F2=m2.m*g-k2*(mag(r2)-L2)*norm(r2)
    F1=m1.m*g-F2-k1*(mag(r1)-L1)*norm(r1)
    m1.p=m1.p+F1*dt
    m2.p=m2.p+F2*dt
    m1.pos=m1.pos+m1.p*dt/m1.m
    m2.pos=m2.pos+m2.p*dt/m2.m
    stick1.axis=m1.pos-pivot.pos
    stick2.pos=m1.pos
    stick2.axis=m2.pos-m1.pos
    t=t+dt
    Ug=m1.m*mag(g)*m1.pos.y+m2.m*mag(g)*m2.pos.y
    T=.5*m1.m*mag(m1.p/m1.m)*2+.5*m2.m*mag(m2.p/m2.m)*2
    Uk=.5*k1*(mag(r2)-L2)2+.5*k2(mag(r1)-L1)**2
    E=T+Ug+Uk
