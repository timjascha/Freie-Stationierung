from guizero import App, Text, TextBox, PushButton, CheckBox
import math as m
import angleconv as ac
import polarkart as pk
import quadrantenbetrachtung as qb
import visu as vs
import quad as q


def frei():

    # Polar zu kartesisch
    a1y = pk.pky(float(s1.value), ac.gr(float(t1gon.value)))
    a1x = pk.pkx(float(s1.value), ac.gr(float(t1gon.value)))
    a2y = pk.pky(float(s2.value), ac.gr(float(t2gon.value)))
    a2x = pk.pkx(float(s2.value), ac.gr(float(t2gon.value)))

    # Deltas bilden
    dqy = a1y - a2y
    dqx = a1x - a2x
    dzy = float(y1.value) - float(y2.value)
    dzx = float(x1.value) - float(x2.value)

    # Strecken im Quell- und Zielsystem
    sq = m.sqrt(q.q(dqy) + q.q(dqx))
    sz = m.sqrt(q.q(dzy) + q.q(dzx))

    # Maßstab
    mt = sz / sq

    # Lokale und uebergeordnete Totation berechnen
    tlokalrad = m.atan(dqy / dqx)
    tueberrad = m.atan(dzy / dzx)

    # Quadrantenbetrachtung
    tlokalgon = qb.qb(dqy, dqx, ac.rg(tlokalrad))
    tuebergon = qb.qb(dzy, dzx, ac.rg(tueberrad))
    # Rotation berechnen
    rotagon = tuebergon-tlokalgon+400
    # Rotation in Radiant umrechnen
    rotarad = ac.gr(rotagon)

    # Standort berechnen
    yp = float(y1.value) - mt * m.sin(rotarad) * a1x - mt * m.cos(rotarad) * a1y
    xp = float(x1.value) - mt * m.cos(rotarad) * a1x + mt * m.sin(rotarad) * a1y

    # Werte uebergeben
    ys.value = str(yp)
    xs.value = str(xp)
    y1v = float(y1.value)
    x1v = float(x1.value)
    y2v = float(y2.value)
    x2v = float(x2.value)
    s1v = float(s1.value)
    s2v = float(s2.value)
    if grafik.value == 1:
        vs.visu(yp, xp, y1v, x1v, y2v, x2v, s1v, s2v)
    if absteckencb.value == 1:
        abstecken(rotarad, yp, xp, mt)


def abstecken(rotarad, yp, xp, mt):

    # deltas bilden
    dy = float(npy.value) - yp
    dx = float(npx.value) - xp
    # Winkel berechnen
    tnprad = m.atan(dy / dx)
    # Winkel umrechnen
    tnpg = ac.rg(tnprad)
    # Quadrantenbtrachtung
    tnpgq = qb.qb(dy, dx, tnpg)
    # Winkel umrechnen
    tnpradq = ac.gr(tnpgq)
    rnrad = tnpradq-rotarad
    print(rnrad)
    rngon = ac.rg(rnrad) + 400
    sn = m.sqrt(q.q(dy) + q.q(dx))
    snk = sn / mt
    laengsab = snk - float(npsg.value)
    laengs.value = str(laengsab)
    querab = ac.gr((rngon - float(nptg.value)) * float(npsg.value))
    print(querab)
    quer.value = str(querab)


app = App(title="Freie Stationierung", height=600, width=320, layout="grid")
app.bg = "white"
app.text_color = "black"

text1 = Text(app, text="Y1", grid=[0, 0])
y1 = TextBox(app, text="0", grid=[3, 0])
text2 = Text(app, text="X1", grid=[0, 1])
x1 = TextBox(app, text="48.28872", grid=[3, 1])
text3 = Text(app, text="Winkel für P1", grid=[0, 2])
t1gon = TextBox(app, text="395.125", grid=[3, 2])
text4 = Text(app, text="Strecke für P1", grid=[0, 3])
s1 = TextBox(app, text="20.704", grid=[3, 3])
text5 = Text(app, text="Y2", grid=[0, 4])
y2 = TextBox(app, text="22.489745", grid=[3, 4])
text6 = Text(app, text="X2", grid=[0, 5])
x2 = TextBox(app, text="47.40545", grid=[3, 5])
text7 = Text(app, text="Winkel für P2", grid=[0, 6])
t2gon = TextBox(app , text="73.622", grid=[3, 6])
text8 = Text(app, text="Strecke für P2", grid=[0, 7])
s2 = TextBox(app, text="17.576", grid=[3, 7])
text9 = Text(app, text="YP", grid=[0, 8])
ys = TextBox(app, text=" ", grid=[3, 8])
text10 = Text(app, text="XP", grid=[0, 9])
xs = TextBox(app, text=" ", grid=[3, 9])
button = PushButton(app, text="Rechnen", command=frei, grid=[0, 10])
grafik = CheckBox(app, text="Grafik", grid=[3, 10])
absteckencb = CheckBox(app, text="Abstecken", grid=[4, 10])

text11 = Text(app, text="Absteckung:", grid=[0, 11])
text12 = Text(app, text="NPY", grid=[0, 12])
npy = TextBox(app, text="10", grid=[3, 12])
text13 = Text(app, text="NPX", grid=[0, 13])
npx = TextBox(app, text="22.862334", grid=[3, 13])
text14 = Text(app, text="Strecke gemessen", grid=[0, 14])
npsg = TextBox(app, text="9.817", grid=[3, 14])
text15 = Text(app, text="Winkel gemessen", grid=[0, 15])
nptg = TextBox(app, text="261.172", grid=[3, 15])
text16 = Text(app, text="Laengsabweichung", grid=[0, 16])
laengs = TextBox(app, text=" ", grid=[3, 16])
text17 = Text(app, text="Querabweichung", grid=[0, 17])
quer = TextBox(app, text=" ", grid=[3, 17])

app.display()