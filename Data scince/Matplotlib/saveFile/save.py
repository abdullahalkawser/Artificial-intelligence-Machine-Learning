
Matplotlib-এ plot different resolution-এ export করতে মূলত plt.savefig() ব্যবহার করবে।
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y)

plt.savefig("student marks",dpi = 600,bbox_inches = "tight")
plt.show()

plt.savefig("student_marks.pdf")
plt.savefig("student_marks.svg")


# bbox_inches="tight" দিলে চারপাশের unnecessary whitespace কমে যায়।

# dpi=72    → low resolution
# dpi=100   → normal
# dpi=150   → good
# dpi=300   → high quality
# dpi=600   → very high quality