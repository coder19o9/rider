import time
import random
import os

def clear_screen():
    """Ekranni tozalash."""
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles):
    """Yo‘lni chizish."""
    road = ["|       |"] * 10
    for obs in obstacles:
        road[obs[1]] = "|   #   |" if obs[0] == 3 else f"| {obs[0] * ' '}# {3 - obs[0] * ' '}|"
    
    road[9] = "|       |"  # O‘yinchining yangi qatori
    road[9] = road[9][:player_pos + 1] + "P" + road[9][player_pos + 2:]
    clear_screen()
    for line in road:
        print(line)
    print("=========")

def move_obstacles(obstacles):
    """To‘siqlarni harakatlantirish."""
    return [[obs[0], obs[1] + 1] for obs in obstacles if obs[1] < 9]

def check_collision(player_pos, obstacles):
    """To‘qnashuvni tekshirish."""
    for obs in obstacles:
        if obs[1] == 9 and obs[0] == player_pos:
            return True
    return False

def main():
    print("Trafik Rider: Matnli Versiyasi")
    print("O‘yinni boshlash uchun ENTER bosing!")
    input()

    player_pos = 3
    obstacles = []
    score = 0

    try:
        while True:
            # Tasodifiy to‘siqlarni qo‘shish
            if random.random() < 0.3:
                obstacles.append([random.randint(1, 5), 0])
            
            # To‘siqlarni harakatlantirish
            obstacles = move_obstacles(obstacles)

            # To‘qnashuvni tekshirish
            if check_collision(player_pos, obstacles):
                print("O‘yin tugadi!")
                print(f"Jami ball: {score}")
                break

            # Yo‘lni chizish
            print_road(player_pos, obstacles)
            print("Harakat: [a] chapga | [d] o‘ngga | [q] chiqish")

            # Harakatni amalga oshirish
            action = input(">>> ").strip().lower()
            if action == "a" and player_pos > 1:
                player_pos -= 1
            elif action == "d" and player_pos < 5:
                player_pos += 1
            elif action == "q":
                print("O‘yin tugadi!")
                break

            score += 1
            time.sleep(0.2)  # Harakat tezligini boshqarish

    except KeyboardInterrupt:
        print("\nO‘yin to‘xtatildi.")

if __name__ == "__main__":
    main()
import time
import random
import os

def clear_screen():
    """Ekranni tozalash."""
    os.system("cls" if os.name == "nt" else "clear")

def print_road(player_pos, obstacles):
    """Yo‘lni chizish."""
    road = ["|       |"] * 10
    for obs in obstacles:
        road[obs[1]] = "|   #   |" if obs[0] == 3 else f"| {obs[0] * ' '}# {3 - obs[0] * ' '}|"
    
    road[9] = "|       |"  # O‘yinchining yangi qatori
    road[9] = road[9][:player_pos + 1] + "P" + road[9][player_pos + 2:]
    clear_screen()
    for line in road:
        print(line)
    print("=========")

def move_obstacles(obstacles):
    """To‘siqlarni harakatlantirish."""
    return [[obs[0], obs[1] + 1] for obs in obstacles if obs[1] < 9]

def check_collision(player_pos, obstacles):
    """To‘qnashuvni tekshirish."""
    for obs in obstacles:
        if obs[1] == 9 and obs[0] == player_pos:
            return True
    return False

def main():
    print("Trafik Rider: Matnli Versiyasi")
    print("O‘yinni boshlash uchun ENTER bosing!")
    input()

    player_pos = 3
    obstacles = []
    score = 0

    try:
        while True:
            # Tasodifiy to‘siqlarni qo‘shish
            if random.random() < 0.3:
                obstacles.append([random.randint(1, 5), 0])
            
            # To‘siqlarni harakatlantirish
            obstacles = move_obstacles(obstacles)

            # To‘qnashuvni tekshirish
            if check_collision(player_pos, obstacles):
                print("O‘yin tugadi!")
                print(f"Jami ball: {score}")
                break

            # Yo‘lni chizish
            print_road(player_pos, obstacles)
            print("Harakat: [a] chapga | [d] o‘ngga | [q] chiqish")

            # Harakatni amalga oshirish
            action = input(">>> ").strip().lower()
            if action == "a" and player_pos > 1:
                player_pos -= 1
            elif action == "d" and player_pos < 5:
                player_pos += 1
            elif action == "q":
                print("O‘yin tugadi!")
                break

            score += 1
            time.sleep(0.2)  # Harakat tezligini boshqarish

    except KeyboardInterrupt:
        print("\nO‘yin to‘xtatildi.")

if __name__ == "__main__":
    main()
