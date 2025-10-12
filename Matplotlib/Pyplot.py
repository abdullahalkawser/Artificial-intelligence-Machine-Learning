import matplotlib.pyplot as plt


# # ১. Basic Styling Elements

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(
#     x, y,
#     color='magenta',      # লাইন রঙ
#     linestyle='--',        # লাইনস্টাইল
#     linewidth=2,           # লাইন মোটা
#     marker='*',            # মার্কার আকৃতি
#     markersize=8,          # মার্কার সাইজ
#     markerfacecolor='yellow',  # মার্কারের ভিতরের রঙ
#     markeredgecolor='black',   # মার্কারের বাইরের রঙ
#     label='Sales Growth'   # লেজেন্ড লেবেল
# )

# plt.title('Matplotlib Styling Example', fontsize=16, color='navy')
# plt.xlabel('Months', fontsize=12)
# plt.ylabel('Revenue', fontsize=12)
# plt.legend()
# plt.grid(True, linestyle=':', color='gray')

# plt.savefig('plot.png', dpi=100 , transparent = 1)  # উচ্চ রেজোলিউশনে সেভ করুন
# plt.show()



# plt.title('My first graph borabor')
# plt.ylabel('y  label borabor')
# plt.xlabel('x label borabor')
# plt.xticks([20, 40, 60, 80, 100]) # X-axis এর টিক মার্কার মানে হলো X-axis-এ কেবল এই মানগুলিতে টিক (নিশান) দেখাবে, বাকি মানগুলিতে টিক থাকবে না।
# plt.yticks([0, 2, 4, 6, 8, 10]) # Y-axis এর টিক মার্কার মানে হলো Y-axis-এ কেবল এই মানগুলিতে টিক (নিশান) দেখাবে, বাকি মানগুলিতে টিক থাকবে না।
# plt.show()




# short-hand notation
# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30], 'r*--')  
# plt.show()
# plt.plot(x, y, 'gs--')  # green square markers with dashed line


import numpy as np

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# # red dashes, blue squares and green triangles
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') #

# plt.show()



plt.figure() # ফিগারের আকার নির্ধারণ
plt.subplot(1, 3, 1) # ১ রো ফিগারের 3 টা অংশে ভাগ করে ১ম অংশে প্লট
plt.plot(t, t, 'r--')

# plt.show()

plt.figure() # ফিগারের আকার নির্ধারণ

plt.subplot(1, 3, 2) # ১ রো ফিগারের 3 টা অংশে ভাগ করে 2ম অংশে প্লট
plt.plot(t, t**2, 'bs')
# plt.show()

plt.figure() # ফিগারের আকার নির্ধারণ নতুন গ্রাফ উইন্ডো

plt.subplot(1, 3, 3) # ১ রো ফিগারের 3 টা অংশে ভাগ করে 3ম অংশে প্লট
plt.plot( t, t**3, 'g^')
plt.show()





# ✅ np.arange(0, 5, 0.2) → 0 থেকে 5 পর্যন্ত প্রতি 0.2 ধাপে মান তৈরি করে
# ✅ t, t → লিনিয়ার গ্রাফ (y = x)
# ✅ t, t**2 → পারাবোলা (y = x²)
# ✅ t, t**3 → কিউব গ্রাফ (y = x³)
# ✅ 'r--' → Red dashed line
# ✅ 'bs' → Blue square marker
# ✅ 'g^' → Green triangle marker
# ✅ plt.show() → গ্রাফ দেখায়

