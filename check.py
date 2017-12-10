import cv2
import numpy as np
checks = cv2.imread('test1.png',0)
checka= cv2.imread("grb.jpg",0)
def shapematch(check):
    ret, thresh = cv2.threshold(check,127, 255,0)
    cv2.imshow('shape',thresh)
    sindex={1:'square',2:'rectangle',3:'circle',4:'cross',5:'hexagon',6:'octagon',7:'triangle',8:'star',9:'trapezium',10:'semi-circle',11:'pentagon',12:'quarter circle',13:'heptagon'}
    slist=[]

    square=cv2.imread('square.png',0)
    rectangle=cv2.imread('rect.png',0)
    circle=cv2.imread('circle.png',0)
    cross=cv2.imread('cross.png',0)
    hexagon= cv2.imread('hex.png',0)
    octagon=cv2.imread('oct.png',0)
    triangle=cv2.imread('tri.png',0)
    star=cv2.imread('star.png',0)
    trapezium=cv2.imread('trap.png',0)
    semi=cv2.imread('semi.png',0)
    pentagon=cv2.imread('pent.png',0)
    quarter=cv2.imread('quarter.png',0)
    septagon=cv2.imread('heptagon.png',0)

    ret, thresh2 = cv2.threshold(square, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(rectangle, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(circle, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(cross, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(hexagon, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(octagon, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(triangle, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(star, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(trapezium, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(semi, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(pentagon, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(quarter, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(septagon, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    flag=0
    min = slist[ 0 ]
    i=1
    ai=1
    for a in slist:
        if a < min:
            min = a
            i=ai
        ai+=1
    if min<0.2:
        flag=1
    else:
        flag=0
    return(flag,sindex[i])

def alphanumeric(check):
    ret, thresh = cv2.threshold(check,127, 255,0)
    cv2.imshow('alpha',thresh)
    adic={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',27:'0',28:'1',29:'2',30:'3',31:'4',32:'5',33:'6',34:'7',35:'8',36:'9'}
    alist=[]
    a=cv2.imread('a.png',0)
    b=cv2.imread('b.png',0)
    c=cv2.imread('c.png',0)
    d=cv2.imread('d.png',0)
    e=cv2.imread('e.png',0)
    f=cv2.imread('f.png',0)
    g=cv2.imread('g.jpg',0)
    h=cv2.imread('h.png',0)
    i=cv2.imread('i.jpg',0)
    j=cv2.imread('j.png',0)
    k=cv2.imread('k.png',0)
    l=cv2.imread('l.png',0)
    m=cv2.imread('m.png',0)
    n=cv2.imread('n.jpg',0)
    o=cv2.imread('o.png',0)
    p=cv2.imread('p.png',0)
    q=cv2.imread('q.png',0)
    r=cv2.imread('r.jpeg',0)
    s=cv2.imread('s.png',0)
    t=cv2.imread('t.png',0)
    u=cv2.imread('u.png',0)
    v=cv2.imread('v.jpg',0)
    w=cv2.imread('w.png',0)
    x=cv2.imread('x.png',0)
    y=cv2.imread('y.png',0)
    z=cv2.imread('z.png',0)

    n0=cv2.imread('0.png',0)
    n1=cv2.imread('1.png',0)
    n2=cv2.imread('2.png',0)
    n3=cv2.imread('3.png',0)
    n4=cv2.imread('4.jpg',0)
    n5=cv2.imread('5.png',0)
    n6=cv2.imread('6.png',0)
    n7=cv2.imread('7.png',0)
    n8=cv2.imread('8.png',0)
    n9=cv2.imread('9.png',0)


    ret, thresh2 = cv2.threshold(a, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(b, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(c, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(d, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(e, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(f, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(g, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(h, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(i, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(j, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(k, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(l, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(m, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(o, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(p, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(q, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(r, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(s, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(t, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(u, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(v, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(w, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(x, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(y, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(z, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n0, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n1, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n2, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n3, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n4, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n5, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n6, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n7, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n8, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)

    ret, thresh2 = cv2.threshold(n9, 127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    alist.append(ret)
    flag=0
    min = alist[ 0 ]
    ai=1
    bi=1
    for ci in alist:
        if ci < min:
            min = ci
            bi=ai
        ai+=1
    if min<0.2:
        flag=1
    else:
        flag=0
    return(flag,adic[bi])
    
shapematch(checka)
alphanumeric(checks)
cv2.waitKey()
cv2.destroyAllWindows()