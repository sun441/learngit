
from turtle import*

color("pink","blue")

begin_fill()

i=0
while i<=4:
    back(150)
    left(144)
    i=i+1

end_fill()

up()
fd(200)
down()
fillcolor("red")
begin_fill()

i=0
while i<5:
    fd(100)
    right(144)
    i+=1
end_fill()
