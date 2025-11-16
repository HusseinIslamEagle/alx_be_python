# pattern_drawing.py

# سؤال المستخدم عن حجم النمط
size = int(input("Enter the size of the pattern: "))

# عداد الصفوف
row = 0

# حلقة while لتكرار الصفوف
while row < size:
    # حلقة for لطباعة النجوم في الصف الواحد
    for col in range(size):
        print("*", end="")
    print()  # الانتقال للسطر الجديد بعد كل صف
    row += 1
