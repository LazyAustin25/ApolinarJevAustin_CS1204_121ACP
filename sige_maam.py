def print_christmas_tree(height):
    height = int(input("gaano kalaki ang puno mo?: "))
    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for k in range(2 * i + 1):
            print("*", end="")
        print()
    
    for i in range(int(height/2)):
        for j in range(height - 1):
            print(" ", end="")
        print("*")

tree_height = 5
print_christmas_tree(tree_height)
