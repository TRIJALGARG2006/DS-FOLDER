move_count = 0

def hanoi(n, src, aux, dst):
    global move_count
    if n == 1:
        move_count += 1
        if n == 3: print(f"Move disk 1 from {src} to {dst}")
        return
    hanoi(n-1, src, dst, aux)
    move_count += 1
    if n == 3: print(f"Move disk {n} from {src} to {dst}")
    hanoi(n-1, aux, src, dst)

print("Trace for N=3:")
hanoi(3, 'A', 'B', 'C')

move_count = 0 
hanoi(4, 'A', 'B', 'C')
print(f"Total moves for N=4: {move_count}")