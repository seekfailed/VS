#体积表面积

#圆系列

#圆形
def S_Circle(r):
	return 3.14*(r^2)
#圆柱

#表面积
def S_Cylinder(r,h):
	#求底面积
    r = int(r)
	bottom_area = 3.14*(r^2)*2
	#S侧
	h = int(h)
    lateral_area = (3.14*2*r)*h
    #表面积
    return lateral_area + bottom_area

#体积
def V_Cylinder(r,h):
	return 3.14*(r^2)*h

#球体

#体积
def V_Ball(r):
	return (4/3)*3.14*(r^3)

#表面积
def S_Ball(d):
	return 3.14*(d^2)

#正方体、正方形

#正方形面积
def S_Square(a):
	return a^2

#正方体

#表面积
def S_Cube(a):
	return a^2*6

#体积
def V_Cube(a):
	return a^3