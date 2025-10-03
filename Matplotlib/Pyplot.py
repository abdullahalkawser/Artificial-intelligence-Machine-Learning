import matplotlib.pyplot as plt

plt.plot(
    [98, 80, 30, 40],        # X-axis এর মান
    [9, 5, 6, 7],        # Y-axis এর মান
    color='red',         # লাইন আর মার্কারের রঙ হবে লাল
    marker='x',          # প্রতিটি পয়েন্টে গোল ডট (⭕) বসবে
    linestyle='dashed',  # লাইন হবে ড্যাশড (----)
    linewidth=2,         # লাইনের মোটা হবে 2 পিক্সেল
    markersize=12        # প্রতিটি ডটের সাইজ হবে বড় (১২ পিক্সেল)
)


plt.title('My first graph borabor')
plt.ylabel('y  label borabor')
plt.xlabel('x label borabor')
plt.xticks([20, 40, 60, 80, 100]) # X-axis এর টিক মার্কার মানে হলো X-axis-এ কেবল এই মানগুলিতে টিক (নিশান) দেখাবে, বাকি মানগুলিতে টিক থাকবে না।
plt.yticks([0, 2, 4, 6, 8, 10]) # Y-axis এর টিক মার্কার মানে হলো Y-axis-এ কেবল এই মানগুলিতে টিক (নিশান) দেখাবে, বাকি মানগুলিতে টিক থাকবে না।
plt.show()