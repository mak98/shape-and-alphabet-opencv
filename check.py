import cv2
import numpy as np
checks = cv2.imread('test1.png',0)
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
    return(flag,sindex[i],min)
def checkalpha(check):
    adic={0 : 'AN.png',1 : 'AE.png',2 : 'AS.png',3 : 'AW.png',
    4 : 'BN.png',5 : 'BE.png',6 : 'BS.png',7 : 'BW.png',
    8 : 'CN.png',9 : 'CE.png',10 : 'CS.png',11 : 'CW.png',
    12 : 'DN.png',13 : 'DE.png',14 : 'DS.png',15 : 'DW.png',
    16 : 'EN.png',17 : 'EE.png',18 : 'ES.png',19 : 'EW.png',
    20 : 'FN.png',21 : 'FE.png',22 : 'FS.png',23 : 'FW.png',
    24 : 'GN.png',25 : 'GE.png',26 : 'GS.png',27 : 'GW.png',
    28 : 'JN.png',29 : 'JE.png',30 : 'JS.png',31 : 'JW.png',
    32 : 'KN.png',33 : 'KE.png',34 : 'KS.png',35 : 'KW.png',
    36 : 'LN.png',37 : 'LE.png',38 : 'LS.png',39 : 'LW.png',
    40 : 'MN.png',41 : 'ME.png',42 : 'MS.png',43 : 'MW.png',
    44 : 'PN.png',45 : 'PE.png',46 : 'PS.png',47 : 'PW.png',
    48 : 'QN.png',49 : 'QE.png',50 : 'QS.png',51 : 'QW.png',
    52 : 'RN.png',53 : 'RE.png',54 : 'RS.png',55 : 'RW.png',
    56 : 'SN.png',57 : 'SE.png',58 : 'SS.png',59 : 'SW.png',
    60 : 'TN.png',61 : 'TE.png',62 : 'TS.png',63 : 'TW.png',
    64 : 'UN.png',65 : 'UE.png',66 : 'US.png',67 : 'UW.png',
    68 : 'VN.png',69 : 'VE.png',70 : 'VS.png',71 : 'VW.png',
    72 : 'WN.png',73 : 'WE.png',74 : 'WS.png',75 : 'WW.png',
    76 : 'YN.png',77 : 'YE.png',78 : 'YS.png',79 : 'YW.png',
    80 : 'ZN.png',81 : 'ZE.png',82 : 'ZS.png',83 : 'ZW.png',
    84 : '1N.png',85 : '1E.png',86: '1S.png',87 : '1W.png',
    88 : '2N.png',89 : '2E.png',90 : '2S.png',91 : '2W.png',
    92 : '3N.png',93 : '3E.png',94 : '3S.png',95 : '3W.png',
    96 : '4N.png',97 : '4E.png',98 : '4S.png',99 : '4W.png',
    100 : '5N.png',101 : '5E.png',102 : '5S.png',103 : '5W.png',
    104 : '7N.png',105 : '7E.png',106 : '7S.png',107 : '7W.png',
    108 : '8N.png',109 : '8E.png',110 : '8S.png',111 : '8W.png'}
    alist=[]
    bdic={}
    ret, thresh = cv2.threshold(check,127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    ellipse = cv2.fitEllipse(cnt1)
    cv2.ellipse(thresh,ellipse,(150,200,100))
    fflag=0
    cv2.imshow('t',thresh)
    cv2.waitKey()
    for i in adic:
        temp=cv2.imread('Alpha/'+adic[i],0)
        ret, thresh2 = cv2.threshold(temp, 127, 255,0)
        _,contours,hierarchy = cv2.findContours(thresh2,2,1)
        cnt2 = contours[0] 
        ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        alist.append(ret)
        if ret==0:
            if i%4==0:
                orientation='North'
            elif i%4==1:
                orientation='East'
            elif i%4==2:
                orientation='South'
            elif i%4==3:
                orientation='West'
            flag=1
            obj=adic[i][0]
            fflag=1
            min=0
            break
    if fflag==0:
        min = alist[ 0 ]
        a=0
        b=0
        for c in alist:
            if c < min:
                min = c
                b=a
            a+=1
        obj=adic[b][0]
        if b%4==0:
                orientation='North'
        elif b%4==1:
                orientation='East'
        elif b%4==2:
                orientation='South'
        elif b%4==3:
                orientation='West'
        if min<0.09:
            flag=1
        else:
            flag=0
    return(flag,obj,orientation,min)

tr=cv2.imread('grb.jpg',0)
f,ob,ori,min=checkalpha(tr)
print(f,ob,ori,min)
    
f,ret,min=shapematch(checks)
print(f,ret,min)
cv2.waitKey()
cv2.destroyAllWindows()