#num_disks = int(input("Enter the number of disks: "))
#def hanoi_tower(n, start, target, mid ,mid2, mid3):
#    if n > 0:
#        hanoi_tower(n-1, start, mid, mid2, mid3, target)
#        print(f"Move disk {n} from {start} to {target}")
#        hanoi_tower(n-1, mid, mid2, mid3, target, start)


# Solving the hanoi
#hanoi_tower(num_disks, 'branch1', 'branch3', 'branch4', 'branch5' , 'branch2')

# Recursive Python function to solve the tower of hanoi
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Move disk 1 from source", source, "to destination", destination)
        return
    
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)


# Driver code
n = 3
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of three rods and n are the number of disks