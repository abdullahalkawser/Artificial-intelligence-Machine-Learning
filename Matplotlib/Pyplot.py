import matplotlib.pyplot as plt


# ১. Basic Styling Elements

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(
    x, y,
    color='magenta',      # লাইন রঙ
    linestyle='--',        # লাইনস্টাইল
    linewidth=2,           # লাইন মোটা
    marker='*',            # মার্কার আকৃতি
    markersize=8,          # মার্কার সাইজ
    markerfacecolor='yellow',  # মার্কারের ভিতরের রঙ
    markeredgecolor='black',   # মার্কারের বাইরের রঙ
    label='Sales Growth'   # লেজেন্ড লেবেল
)

plt.title('Matplotlib Styling Example', fontsize=16, color='navy')
plt.xlabel('Months', fontsize=12)
plt.ylabel('Revenue', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', color='gray')
plt.show()
plt.savefig('plot.png', dpi=100)  # উচ্চ রেজোলিউশনে সেভ করুন



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
