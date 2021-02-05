from guizero import App, Text, TextBox, Combo, PushButton
import math as m


def main():
    t1rad = float(t1gon.value) * m.pi / 200
    t2rad = float(t2gon.value) * m.pi / 200
    xs.value = str(t1rad)
    ys.value = str(t2rad)
    a1y = float(s1.value)*m.sin(t1rad)
    a1x = float(s1.value)*m.cos(t1rad)
    a2y = float(s2.value)*m.sin(t2rad)
    a2x = float(s2.value)*m.cos(t2rad)
    dqy = a1y-a2y
    dqx = a1x-a2x
    dzy = float(y1.value)-float(y2.value)
    dzx = float(x1.value)-float(x2.value)
    dzy2 = dzy*dzy
    dzx2 = dzx*dzx
    dqy2 = dqy*dqy
    dqx2 = dqx*dqx
    sq = m.sqrt(dqy2 + dqx2)
    sz = m.sqrt(dzy2 + dzx2)
    mt = sz/ sq
    tlokalrad = m.atan(dqy/dqx)
    tueberrad = m.atan(dzy/dzx)
    tlokalgon= tlokalrad*200/m.pi
    tuebergon = tueberrad*200/m.pi
    if dqy > 0 and dqx > 0:
        tlokalgon = tlokalgon + 0
    elif dqy > 0 and dqx < 0:
        tlokalgon = tlokalgon + 200
    elif dqy < 0 and dqx < 0:
        tlokalgon = tlokalgon + 200
    elif dqy < 0 and dqx > 0:
        tlokalgon = tlokalgon + 400

    if dzy > 0 and dzx > 0:
        tuebergon = tuebergon + 0
    elif dzy > 0 and dzx < 0:
        tuebergon = tuebergon + 200
    elif dzy < 0 and dzx < 0:
        tuebergon = tuebergon + 200
    elif dzy < 0 and dzx > 0:
        tuebergon = tuebergon + 400


    rotagon = tuebergon-tlokalgon+400

    rotarad = rotagon *m.pi/200

    yp = float(y1.value)-mt*m.sin(rotarad)*a1x-mt*m.cos(rotarad)*a1y
    xp = float(x1.value)-mt*m.cos(rotarad)*a1x+mt*m.sin(rotarad)*a1y
    ys.value = str(yp)
    xs.value = str(xp)






app = App(title="Freie Stationierung", height=600, width=500, layout="grid")
app.bg = "white"
app.text_color = "black"
app.info("Hinweis", "Bitte . anstatt von , verwenden.")


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
button = PushButton(app, text="Rechnen", command=main, grid=[1,10])

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