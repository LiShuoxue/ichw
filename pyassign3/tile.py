"""tile.py: 对一面m*n的墙用x*y的砖进行密铺，
            打印出所有密铺方案，
            并在turtle模块上实现可视化。
__author__ = "Shuoxue Li"
__pkuid__  = "1800011839"
__email__  = "1800011839@pku.edu.cn"
"""
import turtle
import sys
sys.getrecursionlimit=100000

def init_wall(m,n):
    """建立一个表现m*n墙的列表，每个基本单位都用坐标表示。
       坐标由[0,0]直到[m-1,n-1]
    """
    list=[]
    for x in range(n):
        for y in range(m):
            list.append([y,x])
    return list

def brick(coordinate,x,y):
    """以墙上的坐标为左下角，建立一个表现一块x*y砖块的列表，
       该列表中每一个元素是这块砖所占据的墙上的坐标。
    """
    a=init_wall(x,y)
    for element in a:
        element[0]+=coordinate[0]
        element[1]+=coordinate[1]
    return a

def set_brick(wall,x,y):
    """若某砖brick(wall[0],x,y)包含于墙wall内，
       则返回该砖的表达式，并从墙列表中删去该砖包含的坐标。
    """
    a=brick(wall[0],x,y)
    for dot in a:
        if dot in wall:
            continue
        else:
            break
    else:
        for dot in a:
            wall.remove(dot)
        return a

def coarse_methods(wall,x,y):
    """返回所有密铺方式，但会包含一些没有完全密铺的方式，
       未完全密铺的方式会有'Note'做标记。
    """
    a=wall.copy()
    b=wall.copy()
    if len(wall)==0:
        return [[]]
    if len(a)>0 and len(b)>0:
        c=set_brick(a,x,y)
        d=set_brick(b,y,x)
        if c!=None and d!=None:
            e=coarse_methods(a,x,y)
            for p in e:
                p.append(c) 
            f=coarse_methods(b,y,x)
            for q in f:
                q.append(d)
            return e+f
        if c!=None and d==None:
            e=coarse_methods(a,x,y)
            for p in e:
                p.append(c)
            return e
        if c==None and d!=None:
            f=coarse_methods(b,x,y)
            for q in f:
                q.append(d)
            return f
        if c==None and d==None:
            return[['Note']]
        
def final_methods(wall,x,y):
    """对coarse_methods得到的粗列表筛选出未标记，即完全密铺的方式，
       得到最终的密铺方式列表。
    """
    new_list=[]
    for element in coarse_methods(wall,x,y):
        if 'Note' not in str(element):
            new_list.append(element)
    return new_list

def output(m,n,x,y):
    """把密铺方式中基本单位的坐标形式变成整数格式，
       做符合要求的形式输出。
    """
    wall=init_wall(m,n)
    methods=final_methods(wall,x,y).copy()
    new_methods=[]
    for method in methods:
        new_method=[]
        for brick in method:
            new_brick=[]
            for coordinate in brick:
                number=m*coordinate[1]+coordinate[0]
                new_brick.append(number)
            new_method.append(tuple(new_brick))
        new_methods.append(new_method)
    for x in new_methods:
        print(x)
    
def draw_square(coordinate,length,fillcolor):
    """该函数可以以一个确定坐标为左下角画边长为length，涂色为fillcolor的正方形。
    """
    turtle.tracer(False)
    lsx=turtle.Turtle()
    lsx.color('black',fillcolor)
    lsx.up()
    lsx.goto(coordinate[0],coordinate[1])
    lsx.down()
    lsx.begin_fill()
    for x in range(4):
        lsx.forward(length)
        lsx.left(90)
    lsx.end_fill()
    lsx.hideturtle()
    turtle.tracer(True)
    
def draw_wall(m,n):
    """画出一面有正方形网格的墙体，即将init_wall可视化。
    """
    length=600/max(m,n)
    for element in init_wall(m,n):
        coordinate=(length*(element[0]-m/2),length*(element[1]-n/2))
        draw_square(coordinate,length,'white')
    return length

def draw_a_brick(brick,fillcolor,m,n):
    """以构造砖的坐标形式为自变量来绘制以fillcolor为颜色的砖块
    """
    length=600/max(m,n)
    for element in brick:
        coordinate=(length*(element[0]-m/2),length*(element[1]-n/2))
        draw_square(coordinate,length,fillcolor)

def draw_a_method(method,m,n,x,y):
    """用不同颜色的砖块，整体画出一种密铺方法。
       颜色从RGB色库中直接调取。
    """
    colorlist=[]
    for p in range(0,65536*256-1,(65536*256)//((m*n)//(x*y)+1)):
        colorlist.append('#'+'{:0>6s}'.format('{:X}'.format(p)))
    for brick in method:
        draw_a_brick(brick,colorlist[method.index(brick)%len(colorlist)],m,n)
        
def major(m,n,x,y):
    """该函数在打印出所有密铺结果，将其中任意一个在turtle上可视化。
    """
    wall=init_wall(m,n)
    draw_wall(m,n)
    methods=final_methods(wall,x,y)
    draw_a_method(methods[random.randrange(len(methods))],m,n,x,y)
    output(m,n,x,y)

def main():
    major(int(input('墙长度',)),int(input('墙宽度',)),\
          int(input('砖块长度',)),int(input('砖块宽度',)))

if __name__ == '__main__':
    main()
