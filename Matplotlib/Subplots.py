

import matplotlib.pyplot as plt


import numpy as np

t = np.arange(0., 5., 0.2)


plt.figure() # ফিগারের আকার নির্ধারণ
plt.subplot(1, 3, 1) # ১ রো ফিগারের 3 টা অংশে ভাগ করে ১ম অংশে প্লট
plt.plot(t, t, 'r--')
plt.xlabel('u axis label')
plt.ylabel('m axis label')
plt.title('fist line graph')


# plt.show()

plt.figure() # ফিগারের আকার নির্ধারণ

plt.subplot(1, 3, 2) # ১ রো ফিগারের 3 টা অংশে ভাগ করে 2ম অংশে প্লট
plt.plot(t, t**2, 'bs')
plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('2nd line graph')
# plt.show()

plt.figure() # ফিগারের আকার নির্ধারণ নতুন গ্রাফ উইন্ডো

plt.subplot(1, 3, 3) # ১ রো ফিগারের 3 টা অংশে ভাগ করে 3ম অংশে প্লট
plt.plot( t, t**3, 'g^')
plt.xlabel('z axis label')
plt.ylabel('a axis label')
plt.title('last line graph')
plt.suptitle('My first graph borabor') # সব সাবপ্লটের জন্য টাইটেল
plt.tight_layout() # টাইটেল ও লেবেল গুলোর মাঝে জায়গা বাড়াবে

plt.show() # সব প্লট একসাথে দেখাবে

