import turtle

def draw_pithagoras_tree(t, branch_len, level):
    if level == 0:
        return

    # Стилізація
    t.pensize(level * 2)
    if level <= 2:
        t.color("green")
    else:
        t.color("brown")

    t.forward(branch_len)
    angle = 30

    t.right(angle)
    draw_pithagoras_tree(t, branch_len * 0.75, level - 1)
    
 
    t.left(angle * 2) 
    draw_pithagoras_tree(t, branch_len * 0.75, level - 1)
    
   
    t.right(angle) 

    if level > 2:
        t.color("brown")
    else:
        t.color("green")

    t.backward(branch_len)

def main():
    try:
        recursion_level = int(input("Введіть рівень рекурсії (рекомендую 6 або 7): "))
    except ValueError:
        print("Введіть ціле число.")
        return

    screen = turtle.Screen()
    screen.title("Пишне Дерево Піфагора (Анімація)")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)  
    t.up()
    t.goto(0, -200) 
    t.down()

    print("Починаємо малювати...")
    draw_pithagoras_tree(t, 100, recursion_level)
    
    print("Готово! Клікніть на вікно, щоб вийти.")
    screen.exitonclick()

if __name__ == "__main__":
    main()