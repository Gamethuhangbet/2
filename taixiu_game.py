import random

def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

def is_bao(bau):  # Kiểm tra bộ ba
    return bau[0] == bau[1] == bau[2]

def main():
    print("Chào mừng đến với game Tài Xỉu 🎲")
    
    while True:
        choice = input("Chọn Tài (T) hoặc Xỉu (X), hoặc Q để thoát: ").strip().upper()
        if choice == 'Q':
            print("Cảm ơn bạn đã chơi!")
            break
        if choice not in ['T', 'X']:
            print("Lựa chọn không hợp lệ. Hãy thử lại.")
            continue

        dice = roll_dice()
        total = sum(dice)
        print(f"🎲 Xúc xắc ra: {dice[0]}, {dice[1]}, {dice[2]} => Tổng: {total}")

        if is_bao(dice):
            print("💥 Bộ ba! Nhà cái thắng!")
        elif (total >= 11 and total <= 17 and choice == 'T') or (total >= 4 and total <= 10 and choice == 'X'):
            print("🎉 Bạn thắng!")
        else:
            print("😞 Bạn thua!")

        print("-" * 30)

if __name__ == "__main__":
    main()
