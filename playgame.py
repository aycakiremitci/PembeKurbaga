import turtle
import pickle
import time
import random
import winsound

screen = turtle.Screen()
screen.setup(1.0, 1.0)
screen.bgcolor("grey")
kaya = "kaya.gif"
kurbagagif = "kurbaga.gif"
background = "background.gif"
screen.bgpic(background)
screen.addshape(kaya)
screen.addshape(kurbagagif)
screen.title("Pembe Kurbağa")
kurbaga = turtle.Turtle()
dikdortgen1 = turtle.Turtle()
dikdortgen2 = turtle.Turtle()
dikdortgen3 = turtle.Turtle()
dikdortgen4 = turtle.Turtle()
skorturtle = turtle.Turtle()
yuksekskorturtle = turtle.Turtle()
bilgi = turtle.Turtle()
oneri = turtle.Turtle()
skor = 0
yuksekskor = 0
havadakalma = False
ziplamadurumu = False
oyundurumu = True
sagdurum = False
soldurum = False
oyunbasladi = False
xkaya1 = random.randrange(-400, 400)
xkaya2 = random.randrange(-400, 400)
xkaya3 = random.randrange(-400, 400)
xkaya4 = random.randrange(-400, 400)
ykaya1 = 100
ykaya2 = 400
ykaya3 = 600
ykaya4 = 9000

def oyunubaslat():
    global oyunbasladi
    oyunbasladi = True

def oyundancik():
    global oyundurumu
    oyundurumu = False

def zipla():
    global havadakalma
    if not havadakalma:
        global skor, yuksekskor, ziplamadurumu, skorturtle, yuksekskorturtle
        ziplamadurumu = True
        havadakalma = True
        skor += 1
        if skor - 1 == yuksekskor:
            yuksekskor += 1
        skorturtle.clear()
        skorturtle.write("Skor: {}".format(skor), align="center", font=("Arial", 48, "normal"))
        if skor == yuksekskor:
            yuksekskorturtle.clear()
            yuksekskorturtle.write("Yüksek Skor: {}".format(yuksekskor), align="center",
                                   font=("Arial", 50, "normal"))

def ziplama():
    global ziplamadurumu
    ziplamadurumu = False

def sagagit():
    global sagdurum
    sagdurum = True

def sagagitme():
    global sagdurum
    sagdurum = False

def solagit():
    global soldurum
    soldurum = True

def solagitme():
    global soldurum
    soldurum = False


def kurbagacik():
    kurbaga.shape(kurbagagif)
    kurbaga.color("pink")
    kurbaga.penup()
    kurbaga.speed(0)
    kurbaga.goto(0, -290)
    kurbaga.setheading(90)
    kurbaga.shapesize(2, 2, 2)

    turtle.listen()

    turtle.onkey(zipla, "space")
    turtle.onkeypress(sagagit, "Right")
    turtle.onkeyrelease(sagagitme, "Right")
    turtle.onkeypress(solagit, "Left")
    turtle.onkeyrelease(solagitme, "Left")
    turtle.onkeypress(sagagit, "d")
    turtle.onkeyrelease(sagagitme, "d")
    turtle.onkeypress(solagit, "a")
    turtle.onkeyrelease(solagitme, "a")
    turtle.onkey(oyundancik, "c")

def kaya1():
    dikdortgen1.shape(kaya)
    dikdortgen1.color("black")
    dikdortgen1.penup()
    dikdortgen1.speed(0)
    dikdortgen1.goto(xkaya1, ykaya1)
    dikdortgen1.setheading(90)
    dikdortgen1.shapesize(2, 2, 2)

def kaya2():
    dikdortgen2.shape(kaya)
    dikdortgen2.color("black")
    dikdortgen2.penup()
    dikdortgen2.speed(0)
    dikdortgen2.goto(xkaya2, ykaya2)
    dikdortgen2.setheading(90)
    dikdortgen2.shapesize(2, 2, 2)

def kaya3():
    dikdortgen3.shape(kaya)
    dikdortgen3.color("black")
    dikdortgen3.penup()
    dikdortgen3.speed(0)
    dikdortgen3.goto(xkaya3, ykaya3)
    dikdortgen3.setheading(90)
    dikdortgen3.shapesize(2, 2, 2)

def kaya4():
    dikdortgen4.shape(kaya)
    dikdortgen4.color("black")
    dikdortgen4.penup()
    dikdortgen4.speed(0)
    dikdortgen4.goto(xkaya4, ykaya4)
    dikdortgen4.setheading(90)
    dikdortgen4.shapesize(2, 2, 2)

def playmusic():
    song = "sarki.wav"
    winsound.PlaySound(song, winsound.SND_ASYNC)

def oyundongusu():
    global xkaya1,xkaya2,xkaya3,xkaya4,skor
    xkaya1 = random.randrange(-550, 400)
    xkaya2 = random.randrange(-550, 400)
    xkaya3 = random.randrange(-550, 400)
    xkaya4 = random.randrange(-550, 400)
    ykaya1 = 100
    ykaya2 = 350
    ykaya3 = 600
    ykaya4 = 850

    kurbagacik()
    kaya1()
    kaya2()
    kaya3()
    kaya4()

    try:
        with open('score.dat', 'rb') as file:
            global yuksekskor
            yuksekskor = pickle.load(file)
    except:
        yuksekskor = 0

    skor = 0

    skorturtle.speed(0)
    skorturtle.color("black")
    skorturtle.penup()
    skorturtle.pencolor("black")
    skorturtle.setposition(-525, 250)
    skorturtle.write("Skor: {}".format(skor), align="center", font=("Arial", 48, "normal"))
    skorturtle.hideturtle()

    yuksekskorturtle.speed(0)
    yuksekskorturtle.color("black")
    yuksekskorturtle.penup()
    yuksekskorturtle.pencolor("black")
    yuksekskorturtle.setposition(-500, 330)
    yuksekskorturtle.write("Yüksek Skor: {}".format(yuksekskor), align="center", font=("Arial", 50, "normal"))
    yuksekskorturtle.hideturtle()

    bilgi.speed(0)
    bilgi.color("black")
    bilgi.penup()
    bilgi.pencolor("black")
    bilgi.setposition(-485, -320)
    bilgi.write("Zıplamak için Space tuşuna\nOyundan çıkmak için C'ye basın.", align="center", font=("Arial", 25, "normal"))
    bilgi.hideturtle()

    oneri.color("red")
    oneri.pencolor("red")
    oneri.penup()
    oneri.setposition(-800, -240)
    oneri.pendown()
    oneri.goto(800, -240)
    oneri.penup()
    oneri.setposition(550, -220)
    oneri.write("Önerilen zıplama noktası", align="center", font=("Arial", 25, "normal"))
    oneri.hideturtle()

    while oyundurumu:
        if skor == yuksekskor:
            with open('score.dat', 'wb') as file:
                pickle.dump(skor, file)

        xkurbaga = kurbaga.xcor()
        ykurbaga = kurbaga.ycor()
        if xkurbaga > 600:
            global sagdurum
            sagdurum = False
        if xkurbaga < -600:
            global soldurum
            soldurum = False
        if ykurbaga > -275:
            oyunubaslat()
        if ykurbaga < -400:
            global oyunbasladi
            oyunbasladi = False
            time.sleep(1.5)
            skorturtle.clear()
            yuksekskorturtle.clear()
            oneri.clear()
            oyundongusu()
        if (xkaya1 - 128 < xkurbaga < xkaya1 + 128) and (ykaya1 - 40 < ykurbaga + 53 < ykaya1 - 10):
            global ziplamadurumu
            soldurum = False
            sagdurum = False
            ziplamadurumu = False
        if (xkaya2 - 128 < xkurbaga < xkaya2 + 128) and (ykaya2 - 40 < ykurbaga + 53 < ykaya2 - 10):
            soldurum = False
            sagdurum = False
            ziplamadurumu = False
        if (xkaya3 - 128 < xkurbaga < xkaya3 + 128) and (ykaya3 - 40 < ykurbaga + 53 < ykaya3 - 10):
            soldurum = False
            sagdurum = False
            ziplamadurumu = False
        if (xkaya4 - 128 < xkurbaga < xkaya4 + 128) and (ykaya4 - 40 < ykurbaga + 53 < ykaya4 - 10):
            soldurum = False
            sagdurum = False
            ziplamadurumu = False
        if (ykaya1 < ykurbaga - 44 < ykaya1 + 10) and (xkaya1 - 128 < xkurbaga < xkaya1 + 128):
            ykurbaga += 4
            global havadakalma
            havadakalma = False
            if (ykaya1 > -460 and ykaya2 > -460 and ykaya3 > -460 and ykaya4 > -460) or ziplamadurumu:
                if skor < 20:
                    ykaya1 -= 5
                    ykaya2 -= 5
                    ykaya3 -= 5
                    ykaya4 -= 5
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                elif skor < 40:
                    ykaya1 -= 8
                    ykaya2 -= 8
                    ykaya3 -= 8
                    ykaya4 -= 8
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                else:
                    ykaya1 -= 12
                    ykaya2 -= 12
                    ykaya3 -= 12
                    ykaya4 -= 12
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
        if (ykaya2 < ykurbaga - 44 < ykaya2 + 10) and (xkaya2 - 128 < xkurbaga < xkaya2 + 128):
            ykurbaga += 4
            havadakalma = False
            if ykaya1 > -460 and ykaya2 > -460 and ykaya3 > -460 and ykaya4 > -460 or ziplamadurumu:
                if skor < 20:
                    ykaya1 -= 5
                    ykaya2 -= 5
                    ykaya3 -= 5
                    ykaya4 -= 5
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                elif skor < 40:
                    ykaya1 -= 8
                    ykaya2 -= 8
                    ykaya3 -= 8
                    ykaya4 -= 8
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                else:
                    ykaya1 -= 12
                    ykaya2 -= 12
                    ykaya3 -= 12
                    ykaya4 -= 12
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
        if (ykaya3 < ykurbaga - 44 < ykaya3 + 10) and (xkaya3 - 128 < xkurbaga < xkaya3 + 128):
            ykurbaga += 4
            havadakalma = False
            if ykaya1 > -460 and ykaya2 > -460 and ykaya3 > -460 and ykaya4 > -460 or ziplamadurumu:
                if skor < 20:
                    ykaya1 -= 5
                    ykaya2 -= 5
                    ykaya3 -= 5
                    ykaya4 -= 5
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                elif skor < 40:
                    ykaya1 -= 8
                    ykaya2 -= 8
                    ykaya3 -= 8
                    ykaya4 -= 8
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                else:
                    ykaya1 -= 12
                    ykaya2 -= 12
                    ykaya3 -= 12
                    ykaya4 -= 12
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
        if (ykaya4 - 10 < ykurbaga - 44 < ykaya4 + 10) and (xkaya4 - 128 < xkurbaga < xkaya4 + 128):
            ykurbaga += 4
            havadakalma = False
            if ykaya1 > -460 and ykaya2 > -460 and ykaya3 > -460 and ykaya4 > -460 or ziplamadurumu:
                if skor < 20:
                    ykaya1 -= 5
                    ykaya2 -= 5
                    ykaya3 -= 5
                    ykaya4 -= 5
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                elif skor < 40:
                    ykaya1 -= 8
                    ykaya2 -= 8
                    ykaya3 -= 8
                    ykaya4 -= 8
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
                else:
                    ykaya1 -= 12
                    ykaya2 -= 12
                    ykaya3 -= 12
                    ykaya4 -= 12
                    dikdortgen1.goto(xkaya1, ykaya1)
                    dikdortgen2.goto(xkaya2, ykaya2)
                    dikdortgen3.goto(xkaya3, ykaya3)
                    dikdortgen4.goto(xkaya4, ykaya4)
        if oyunbasladi:
            ykurbaga -= 4
        else:
            havadakalma = False
        if ziplamadurumu and ykurbaga < 90:
            ykurbaga += 8
        if ziplamadurumu and ykurbaga <= 180:
            ykurbaga += 7
        if ziplamadurumu and (180 < ykurbaga < 184):
            ykurbaga += 6
        if ziplamadurumu and (184 <= ykurbaga < 197):
            ykurbaga += 5
        if ziplamadurumu and (197 <= ykurbaga < 200):
            ykurbaga += 4
            ziplama()
        if sagdurum:
            xkurbaga += 5
        if soldurum:
            xkurbaga -= 5
        if ykaya1 < -400:
            ykaya1 = 600
        if ykaya2 < -400:
            ykaya2 = 600
        if ykaya3 < -400:
            ykaya3 = 600
        if ykaya4 < -400:
            ykaya4 = 600

        kurbaga.goto(xkurbaga, ykurbaga)


oyundongusu()