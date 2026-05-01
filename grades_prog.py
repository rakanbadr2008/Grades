def calculate_grade():
    """
    برنامج متكامل لحساب تقدير الطالب بناءً على درجته
    مع معالجة الأخطاء والاستمرار في العمل.
    """
    print("--- مرحباً بك في برنامج نظام التقديرات ---")
    print("أدخل درجة الطالب (0-100) للحصول على التقدير، أو اكتب 'خروج' للإغلاق.")

    while True:
        user_input = input("\nأدخل الدرجة: ").strip().lower()

        # خيار الخروج من البرنامج
        if user_input == "خروج" or user_input == "exit":
            print("تم إغلاق البرنامج. شكراً لك!")
            break

        try:
            # التحويل لرقم عشري للتعامل مع الكسور
            grade = float(user_input)

            # التحقق من منطقية الدرجة (النطاق)
            if grade < 0 or grade > 100:
                print("خطأ: يرجى إدخال درجة منطقية بين 0 و 100.")
                continue

            # منطق تحديد التقدير
            if grade >= 90:
                result = "ممتاز"
            elif grade >= 80:
                result = "جيد جداً"
            elif grade >= 65:
                result = "جيد"
            else:
                result = "ضعيف"

            print(f"تقدير الطالب هو: {result}")

        except ValueError:
            # معالجة إدخال نصوص غير "خروج" أو رموز غير رقمية
            print("خطأ: مدخلات غير صالحة. يرجى إدخال رقم صحيح أو كلمة 'خروج'.")

if __name__ == "__main__":
    calculate_grade()