import matplotlib.pyplot as plt


def visu(a, b, c, d, e, f, g, h):

    # Koordinaten definiert
    x = [a, c, e]
    y = [b, d, f]
    # Plot erstellen
    plt.plot(x, y, "ko", label="Punkte")
    # Achsen beschriftet
    plt.xlabel("Y")
    plt.ylabel("X")
    # Linie erzeugen
    plt.plot([a, c], [b, d], "g-", label=str(g)+"m")
    plt.plot([a, e], [b, f], "r-", label=str(h)+"m")
    # Punkte beschriften
    plt.annotate("Standpunkt", xy=(a, b), xytext=(a+1, b))
    plt.annotate("AP1", xy=(c, d), xytext=(c+1, d))
    plt.annotate("AP2", xy=(e, f), xytext=(e+1, f))
    plt.grid()
    plt.legend(loc="best")
    plt.savefig("Plot.pdf")
    plt.show()


def visu2(a, b, c, d, e, f, g, h, i, j, k):

    # Koordinaten definiert
    x = [a, c, e, i]
    y = [b, d, f, j]
    # Plot erstellen
    plt.plot(x, y, "ko", label="Punkte")
    # Achsen beschriftet
    plt.xlabel("Y")
    plt.ylabel("X")
    # Linie erzeugen
    plt.plot([a, c], [b, d], "g-", label=str(g)+"m")
    plt.plot([a, e], [b, f], "r-", label=str(h)+"m")
    plt.plot([a, i], [b, j], "b-", label=str(k)+"m")
    # Punkte beschriften
    plt.annotate("Standpunkt", xy=(a, b), xytext=(a+1, b))
    plt.annotate("AP1", xy=(c, d), xytext=(c+1, d))
    plt.annotate("AP2", xy=(e, f), xytext=(e+1, f))
    plt.annotate("NP", xy=(i, j), xytext=(i+1, j))
    plt.grid()
    plt.legend(loc="best")
    plt.savefig("Plot.pdf")
    plt.show()
