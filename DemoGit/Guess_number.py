import random
import threading
import time

def countdown():
    global time_up
    time.sleep(10)
    time_up = True
    print("\n⏰ Hết giờ rồi!")

def guess_game():
    number = random.randint(1, 100)
    print("🎮 Trò chơi đoán số (1-100)")
    print("Bạn có 10 giây để đoán đúng số.")

    threading.Thread(target=countdown, daemon=True).start()
    attempts = 0

    while not time_up:
        try:
            guess = int(input("Đoán số của bạn: "))
            attempts += 1
            if guess == number:
                print(f"🎉 Đúng rồi! Bạn đoán đúng sau {attempts} lần thử.")
                return
            elif guess < number:
                print("🔺 Số lớn hơn.")
            else:
                print("🔻 Số nhỏ hơn.")
        except ValueError:
            print("⚠️ Nhập một số nguyên.")

    print(f"😢 Thua rồi! Số đúng là {number}")

# Biến cờ
time_up = False
guess_game()
