import random
import time
import threading

secret = random.randint(1, 20)
guess = None
timeout = False

def countdown():
    global timeout
    for i in range(10, 0, -1):
        print(f"⏳ Còn {i} giây...", end='\r')
        time.sleep(1)
    timeout = True
    print("\n⛔ Hết giờ!")

def user_input():
    global guess
    try:
        guess = int(input("💡 Nhập số bạn đoán (1-20): "))
    except:
        guess = None

print("🎯 Trò chơi: Đoán số bí mật trong 10 giây!")
print("👉 Bạn chỉ có 1 lần đoán duy nhất!")

# Bắt đầu đồng hồ đếm ngược
thread1 = threading.Thread(target=countdown)
thread2 = threading.Thread(target=user_input)

thread1.start()
thread2.start()

# Chờ người dùng nhập hoặc hết giờ
thread2.join()
timeout = True  # nếu người dùng đoán xong thì ngắt luôn đếm giờ

if guess == secret:
    print("✅ Chính xác! Bạn thắng rồi!")
elif guess is None:
    print("❌ Bạn chưa nhập số hợp lệ.")
elif timeout:
    print(f"❌ Hết thời gian hoặc sai rồi. Số đúng là {secret}.")
else:
    print(f"❌ Sai rồi. Số đúng là {secret}.")