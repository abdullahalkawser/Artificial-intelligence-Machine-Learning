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

plt.savefig('plots.png', dpi=100 )  # উচ্চ রেজোলিউশনে সেভ করুন
plt.show()

