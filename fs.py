from guizero import App, Text, TextBox, PushButton, CheckBox
import math as m
import angleconv as ac
import polarkart as pk
import quadrantenbetrachtung as qb
import visu as vs


def main():
    #Winkel in Gon umrechnen
    t1rad = ac.rg(float(t1gon.value))
    t2rad = ac.rg(float(t2gon.value))

    #Polar zu kartesisch
    a1y = pk.pky(float(s1.value),t1rad)
    a1x = pk.pkx(float(s1.value),t1rad)
    a2y = pk.pky(float(s2.value),t2rad)
    a2x = pk.pkx(float(s2.value),t2rad)

    #Deltas bilden
    dqy = a1y-a2y
    dqx = a1x-a2x
    dzy = float(y1.value)-float(y2.value)
    dzx = float(x1.value)-float(x2.value)

    #Deltas quadriert
    dzy2 = dzy*dzy
    dzx2 = dzx*dzx
    dqy2 = dqy*dqy
    dqx2 = dqx*dqx

    #Strecken im Quell- und Zielsystem
    sq = m.sqrt(dqy2 + dqx2)
    sz = m.sqrt(dzy2 + dzx2)

    #Maßstab
    mt = sz/ sq

    #Lokale und uebergeordnete Totation berechnen
    tlokalrad = m.atan(dqy/dqx)
    tueberrad = m.atan(dzy/dzx)

    #Winkel in Gon umrechnen
    tlokalgon= ac.gr(tlokalrad)
    tuebergon = ac.gr(tueberrad)

    #Quadrantenbetrachtung
    tlokalgon = qb.qb(dqy,dqx,tlokalgon)
    tuebergon = qb.qb(dzy,dzx,tuebergon)
    #Rotation berechnen
    rotagon = tuebergon-tlokalgon+400
    #Rotation in Radiant umrechnen
    rotarad = ac.rg(rotagon)

    #Standort berechnen
    yp = float(y1.value)-mt*m.sin(rotarad)*a1x-mt*m.cos(rotarad)*a1y
    xp = float(x1.value)-mt*m.cos(rotarad)*a1x+mt*m.sin(rotarad)*a1y

    #Werte uebergeben
    ys.value = str(yp)
    xs.value = str(xp)
    y1v = float(y1.value)
    x1v = float(x1.value)
    y2v = float(y2.value)
    x2v = float(x2.value)
    s1v = float(s1.value)
    s2v = float(s2.value)

    if grafik.value==1:
        vs.visu(yp, xp, y1v, x1v, y2v, x2v, s1v, s2v)




app = App(title="Freie Stationierung", height=350, width=220, layout="grid")
app.bg = "white"
app.text_color = "black"

text1 = Text(app, text="Y1", grid=[0,0])
y1 = TextBox(app, text="0", grid=[3,0])
text2 = Text(app, text="X1", grid=[0,1])
x1 = TextBox(app, text="48.28872", grid=[3,1])
text3 = Text(app, text="Winkel für P1", grid=[0,2])
t1gon = TextBox(app, text="395.125", grid=[3,2])
text4 = Text(app, text="Strecke für P1", grid=[0,3])
s1 = TextBox(app, text="20.704", grid=[3,3])
text5 = Text(app, text="Y2", grid=[0,4])
y2 = TextBox(app, text="22.489745", grid=[3,4])
text6 = Text(app, text="X2", grid=[0,5])
x2 = TextBox(app, text="47.40545", grid=[3,5])
text7 = Text(app, text="Winkel für P2", grid=[0,6])
t2gon = TextBox(app , text="73.622", grid=[3,6])
text8 = Text(app, text="Strecke für P2", grid=[0,7])
s2 = TextBox(app, text="17.576", grid=[3,7])
text9 = Text(app, text="YP", grid=[0,8])
ys = TextBox(app, text=" ", grid=[3,8])
text10 = Text(app, text="XP", grid=[0,9])
xs = TextBox(app, text=" ", grid=[3,9])
button = PushButton(app, text="Rechnen", command=main, grid=[0,10])
grafik = CheckBox(app, text="Grafik", grid=[3,10])
#text11 = Text(app, text="Absteckung:", grid=[0,11])
#text12 = Text(app, text="NPY", grid=[0,12])
#npy = TextBox(app, text=" ", grid=[3,12])
#text13 = Text(app, text="NPX", grid=[0,13])
#npx = TextBox(app, text=" ", grid=[3,13])
#text14 = Text(app, text="Strecke gemessen", grid=[0,14])
#npsg = TextBox(app, text=" ", grid=[3,14])
#text15 = Text(app, text="Winkel gemessen", grid=[0,15])
#nptg = TextBox(app, text=" ", grid=[3,15])
#text16 = Text(app, text="Laengsabweichung", grid=[0,16])
#laengs = TextBox(app, text=" ", grid=[3,16])
#text17 = Text(app, text="Querabweichung", grid=[0,17])
#quer = TextBox(app, text=" ", grid=[3,17])

#abstecken = PushButton(app, text="Abstecken!",command=abstecken,  grid=[1,18])

app.display()