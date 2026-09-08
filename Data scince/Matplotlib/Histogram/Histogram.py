import matplotlib.pyplot as plt

marks= [10, 20, 15, 30, 25, 40, 50, 60, 70, 80 ];

plt.hist(marks,bins= 10,color= 'red',edgecolor= 'white',alpha= 0.7,   density=True, range =(20,50), histtype = 'bar',orientation= 'vertical',)
plt.title("Histogram of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()


# 8️⃣ density=True ⭐
# Normal count-এর পরিবর্তে probability density দেখাবে।


# bins=5 মানে পুরো data range-কে প্রায় 5টা group/range-এ ভাগ করবে।

# যেমন:

# 30–42     → কতজন
# 42–54     → কতজন
# 54–66     → কতজন
# 66–78     → কতজন
# 78–90     → কতজন


# x
# bins
# range
# density
# cumulative
# color
# alpha
# edgecolor
# label


# 📊 plt.hist() — Short Chart
# Parameter	কাজ	মনে রাখার উপায়


# data	যে data দেখাবো	Data

# bins	কয়টা group/range	Group

# range	কোন range-এর data	Range

# density=True	Probability density	Probability

# cumulative=True	Cumulative frequency	যোগ হতে থাকবে
# color	রং	Color
# alpha	Transparency	Transparent
# edgecolor	Border	Edge = Border
# label	Data-এর নাম	Name
# histtype	Histogram-এর style	Type
# orientation	Vertical/Horizontal	Direction