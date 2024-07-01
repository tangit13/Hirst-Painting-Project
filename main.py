# import colorgram
# colors = colorgram.extract('hirst.jpg', 100)
#
# for i in colors:
#     r=(i.rgb.r)
#     g=(i.rgb.g)
#     b=(i.rgb.b)
#     color_list.append((r,g,b)) t(color_list)
import turtle as tim
import random
color_list = [(208, 157, 105), (228, 241, 238), (58, 98, 132), (156, 83, 53), (139, 159, 189), (231, 202, 104),
              (158, 167, 41), (52, 174, 121), (122, 189, 173), (201, 136, 154), (65, 39, 32), (76, 113, 88),
              (126, 80, 88), (133, 30, 48), (28, 48, 67), (195, 93, 74), (181, 93, 110), (115, 37, 23), (5, 66, 50),
              (56, 32, 44), (162, 190, 224), (75, 133, 198), (231, 203, 3), (34, 64, 103), (31, 163, 168), (13, 83, 56),
              (158, 209, 193), (220, 179, 171), (214, 178, 185), (77, 79, 40), (163, 204, 210), (49, 69, 75)]


tim.colormode(255)
t = tim.Turtle()
t.penup()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
num = 100

for dot in range(1, num + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    if dot % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.right(90)
        t.backward(500)
    if dot == 100:
        t.hideturtle()

screen = tim.Screen()
screen.exitonclick()
