import cv2
import numpy as np
def shapematch(check):
    ret, thresh = cv2.threshold(check,127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    sindex={1:'square',2:'rectangle',3:'circle',4:'cross',5:'hexagon',6:'octagon'
    ,7:'triangle',8:'star',9:'trapezium',10:'semi-circle',11:'pentagon',12:'quarter circle'
    ,13:'heptagon'}
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
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(rectangle, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(circle, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(cross, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(hexagon, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(octagon, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(triangle, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)


    ret, thresh2 = cv2.threshold(star, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(trapezium, 127, 255,0)
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(semi, 127, 255,0)
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
    _,contours,hierarchy = cv2.findContours(thresh2,2,1)
    cnt2 = contours[0] 
    ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
    slist.append(ret)

    ret, thresh2 = cv2.threshold(septagon, 127, 255,0)
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
    adic={0 :'AN.png',1 :'ANE.png',2 :'AE.png',3 :'ASE.png',4 :'AS.png',5 :'ASW.png',6 :'AW.png',7 :'ANW.png',
    8 :'BN.png',9 :'BNE.png',10 :'BE.png',11 :'BSE.png',12 :'BS.png',13 :'BSW.png',14 :'BW.png',15 :'BNW.png',
    16 :'CN.png',17 :'CNE.png',18 :'CE.png',19 :'CSE.png',20 :'CS.png',21 :'CSW.png',22 :'CW.png',23 :'CNW.png',
    24 :'DN.png',25 :'DNE.png',26 :'DE.png',27 :'DSE.png',28 :'DS.png',29 :'DSW.png',30 :'DW.png',31 :'DNW.png',
    32 :'EN.png',33 :'ENE.png',34 :'EE.png',35 :'ESE.png',36 :'ES.png',37 :'ESW.png',38 :'EW.png',39 :'ENW.png',
    40 :'FN.png',41 :'FNE.png',42 :'FE.png',43 :'FSE.png',44 :'FS.png',45 :'FSW.png',46 :'FW.png',47 :'FNW.png',
    48 :'GN.png',49 :'GNE.png',50 :'GE.png',51 :'GSE.png',52 :'GS.png',53 :'GSW.png',54 :'GW.png',55 :'GNW.png',
    56 :'JN.png',57 :'JNE.png',58 :'JE.png',59 :'JSE.png',60 :'JS.png',61 :'JSW.png',62 :'JW.png',63 :'JNW.png',
    64 :'KN.png',65 :'KNE.png',66 :'KE.png',67 :'KSE.png',68 :'KS.png',69 :'KSW.png',70 :'KW.png',71 :'KNW.png',
    72 :'LN.png',73 :'LNE.png',74 :'LE.png',75 :'LSE.png',76 :'LS.png',77 :'LSW.png',78 :'LW.png',79 :'LNW.png',
    80 :'MN.png',81 :'MNE.png',82 :'ME.png',83 :'MSE.png',84 :'MS.png',85 :'MSW.png',86 :'MW.png',87 :'MNW.png',
    88 :'PN.png',89 :'PNE.png',90 :'PE.png',91 :'PSE.png',92 :'PS.png',93 :'PSW.png',94 :'PW.png',95 :'PNW.png',
    96 :'QN.png',97 :'QNE.png',98 :'QE.png',99 :'QSE.png',100 :'QS.png',101 :'QSW.png',102 :'QW.png',103 :'QNW.png',
    104 :'RN.png',105 :'RNE.png',106 :'RE.png',107 :'RSE.png',108 :'RS.png',109 :'RSW.png',110 :'RW.png',111 :'RNW.png',
    112 :'SN.png',113 :'SNE.png',114 :'SE.png',115 :'SSE.png',116 :'SS.png',117 :'SSW.png',118 :'SW.png',119 :'SNW.png',
    120 :'TN.png',121 :'TNE.png',122 :'TE.png',123 :'TSE.png',124 :'TS.png',125 :'TSW.png',126 :'TW.png',127 :'TNW.png',
    128 :'UN.png',129 :'UNE.png',130 :'UE.png',131 :'USE.png',132 :'US.png',133 :'USW.png',134 :'UW.png',135 :'UNW.png',
    136 :'VN.png',137 :'VNE.png',138 :'VE.png',139 :'VSE.png',140 :'VS.png',141 :'VSW.png',142 :'VW.png',143 :'VNW.png',
    144 :'WN.png',145 :'WNE.png',146 :'WE.png',147 :'WSE.png',148 :'WS.png',149 :'WSW.png',150 :'WW.png',151 :'WNW.png',
    152 :'YN.png',153 :'YNE.png',154 :'YE.png',155 :'YSE.png',156 :'YS.png',157 :'YSW.png',158 :'YW.png',159 :'YNW.png',
    160 :'1N.png',161 :'1NE.png',162 :'1E.png',163 :'1SE.png',164 :'1S.png',165 :'1SW.png',166 :'1W.png',167 :'1NW.png',
    168 :'2N.png',169 :'2NE.png',170 :'2E.png',171 :'2SE.png',172 :'2S.png',173 :'2SW.png',174 :'2W.png',175 :'2NW.png',
    176 :'3N.png',177 :'3NE.png',178 :'3E.png',179 :'3SE.png',180 :'3S.png',181 :'3SW.png',182 :'3W.png',183 :'3NW.png',
    184 :'4N.png',185 :'4NE.png',186 :'4E.png',187 :'4SE.png',188 :'4S.png',189 :'4SW.png',190 :'4W.png',191 :'4NW.png',
    192 :'5N.png',193 :'5NE.png',194 :'5E.png',195 :'5SE.png',196 :'5S.png',197 :'5SW.png',198 :'5W.png',199 :'5NW.png',
    200 :'7N.png',201 :'7NE.png',202 :'7E.png',203 :'7SE.png',204 :'7S.png',205 :'7SW.png',206 :'7W.png',207 :'7NW.png',
    208 :'8N.png',209 :'8NE.png',210 :'8E.png',211 :'8SE.png',212 :'8S.png',213 :'8SW.png',214 :'8W.png',215 :'8NW.png',}
    alist=[]
    bdic={"HN.png":'North',"HE.png":'East',"HNE.png":'North East',"HNW.png":'North West',
    "IN.png":'North',"IE.png":'East',"INE.png":'North East',"INE.png":'North West',
    "NN.png":'North',"NE.png":'East',"NNE.png":'North East',"NSE.png":'South East',
    "O.png":'North',"XN.png":'North',"XNE.png":'North East',"XNW.png":'North West',
    "ZN.png":'North',"ZNE.png":'North East',"ZNW.png":'North West',"0N.png":'North',
    "0E.png":'East',"0NE.png":'North East',"0NW.png":'North West',"6.png":'North',"9.png":'North'}
    ret, thresh = cv2.threshold(check,127, 255,0)
    _,contours,hierarchy= cv2.findContours(thresh,2,1)
    cnt1 = contours[0]
    ellipse = cv2.fitEllipse(cnt1)
    cv2.ellipse(thresh,ellipse,(150,200,100))
    cv2.imshow('t',thresh)
    cv2.waitKey()
    fflag=0
    for i in adic:
        temp=cv2.imread('Alpha/'+adic[i],0)
        ret, thresh2 = cv2.threshold(temp, 127, 255,0)
        _,contours,hierarchy = cv2.findContours(thresh2,2,1)
        cnt2 = contours[0] 
        #cv2.imshow('',thresh2)
        #cv2.waitKey()
        ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        alist.append(ret)
        if ret==0:
            if i%8==0:
                orientation='North'
            elif i%8==1:
                orientation='North East'
            elif i%8==2:
                orientation='East'
            elif i%8==3:
                orientation='South East'
            elif i%8==4:
                orientation='South'
            elif i%8==5:
                orientation='South West'
            elif i%8==6:
                orientation='West'
            elif i%8==7:
                orientation='North West'
            flag=1
            obj=adic[i][0]
            fflag=1
            min=0
            break
    for i in bdic:
        temp=cv2.imread('Alpha/'+i,0)
        ret, thresh2 = cv2.threshold(temp, 127, 255,0)
        _,contours,hierarchy = cv2.findContours(thresh2,2,1)
        cnt2 = contours[0] 
        #cv2.imshow('',thresh2)
        #cv2.waitKey()
        ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
        alist.append(ret)
        if ret==0:
            orientation=bdic[i]
            fflag=1
            flag=1
            min=0
            obj=i[0]
            break
    if fflag==0:
        min = alist[ 0 ]
        a=0
        b=0
        for c in alist:
            if c <=min:
                min = c
                b=a
            a+=1
        obj=adic[b][0]
        if b%8==0:
            orientation='North'
        elif b%8==1:
            orientation='North East'
        elif b%8==2:
            orientation='East'
        elif b%8==3:
            orientation='South East'
        elif b%8==4:
            orientation='South'
        elif b%8==5:
            orientation='South West'
        elif b%8==6:
            orientation='West'
        elif b%8==7:
            orientation='North West'
        if min<0.9:
            flag=1
        else:
            flag=0
    return(flag,obj,orientation,min)
tr=cv2.imread('9.png',0)
f,ob,ori,min=checkalpha(tr)
print(f,ob,ori,min)