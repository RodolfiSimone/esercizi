'''data la parabola y = ax^2+bx+c, definisci due funzioni per carcolare il vertice ed il fuoco'''

def delta_parabola(a,b,c):
    delta = (b**2)-4*a*c 
    
    return delta


def vertice_parabola(a,b, delta):
    vertice_x = -b/(2*a)
    vertice_y = -delta/(4*a)
    
    print("le coordinate del vertice sono :", "(", vertice_x, ",", vertice_y, ")")


def fuoco_parabola(a,b, delta):
    fuoco_x = -b/(2*a)
    fuoco_y = (1-delta)/(4*a)
    
    print("le coordinate del fuoco sono :", "(", fuoco_x, ",", fuoco_y, ")")


def main():
    print("data la parabola y = ax^2+bx+c")
    a = float(input("inserire valore a: "))
    b = float(input("inserire valore b: "))
    c = float(input("inserire valore c: "))
    delta = delta_parabola(a, b, c)
    vertice_parabola(a, b, delta)
    fuoco_parabola(a, b, delta)


main()