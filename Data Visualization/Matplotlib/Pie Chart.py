import matplotlib.pyplot as plt

# ১. প্রতিটি ক্যাটাগরির মান (যেমন শতাংশ বা সংখ্যা)
sizes = [40, 25, 20, 15]
labels = ['ai', 'al', 'ml', 'gen ai']

# ২. Pie চার্ট আঁকা
plt.pie(
    sizes,
    labels=labels,        # slice-এর নাম
    autopct='%1.1f%%',    # শতাংশ দেখাবে (1 decimal)
    startangle=90,        # চার্ট কোন এঙ্গেল থেকে শুরু হবে
    shadow=True,          # ছায়া যোগ করা
    explode=[0.1, 0, 0, 0] # প্রথম slice একটু বাইরে বের হবে (highlight)
)

# ৩. টাইটেল যোগ করা
plt.title("Pie Chart Example")
plt.legend()

# ৪. সমান অনুপাত রাখা যাতে pie ঠিকভাবে গোল হয়
plt.axis('equal')

# ৫. চার্ট দেখানো
plt.show()



# ✅ গুরুত্বপূর্ণ Parameters
# Parameter	কাজ
# labels	প্রতিটি slice-এর নাম
# autopct	শতাংশ দেখানো
# startangle	শুরু করার কোণ
# explode	কোন slice আলাদা করে দেখানো
# shadow	ছায়া যোগ করা
# colors	slice-এর রঙ কাস্টমাইজ করা
# plt.axis('equal')	Pie চার্টকে গোল রাখা