# 📦 MongoDB Daily Command Cheatsheet

এই নোটে MongoDB-এর গুরুত্বপূর্ণ কমান্ডগুলো সংক্ষিপ্তভাবে বর্ণনা করা হলো যেগুলো প্রতিদিনের ডেটাবেস ব্যবস্থাপনায় কাজে লাগবে।

---

## 🗃️ ডেটাবেস সম্পর্কিত কমান্ড

### 🔍 ১. সব ডেটাবেস লিস্ট করতে:
```js
show dbs
```

### ➕ ২. নতুন ডেটাবেস তৈরি বা সিলেক্ট করতে:
```js
use myDatabase
```

### ✅ ৩. বর্তমানে কোন ডেটাবেসে আছো তা দেখতে:
```js
db
```

---

## 📁 কালেকশন (Collection) সম্পর্কিত কমান্ড

### 📋 ৪. ডেটাবেসের সব কালেকশন দেখতে:
```js
show collections
```

### ➕ ৫. নতুন ডেটা ইনসার্ট (একটি ডকুমেন্ট):
```js
db.users.insertOne({ name: "Abdullah", age: 22 })
```

### ➕➕ ৬. একাধিক ডকুমেন্ট ইনসার্ট করতে:
```js
db.users.insertMany([
  { name: "Anisa", age: 20 },
  { name: "Rahim", age: 25 }
])
```

---

## 📄 ডেটা রিড / কোয়েরি

### 🔍 ৭. সব ডেটা রিড করতে:
```js
db.users.find()
```

### 🔍 ৮. ফিল্টার করে নির্দিষ্ট ডেটা দেখতে:
```js
db.users.find({ name: "Abdullah" })
```

### 🔢 ৯. নির্দিষ্ট একটি ডেটা দেখতে:
```js
db.users.findOne({ age: 22 })
```

---

## 🔁 আপডেট ও মুছা

### 🔧 ১০. একটি ডকুমেন্ট আপডেট করতে:
```js
db.users.updateOne(
  { name: "Abdullah" },
  { $set: { age: 23 } }
)
```

### 🔧 ১১. একাধিক ডকুমেন্ট আপডেট করতে:
```js
db.users.updateMany(
  { age: { $lt: 25 } },
  { $set: { status: "young" } }
)
```

### 🗑️ ১২. একটি ডকুমেন্ট ডিলিট করতে:
```js
db.users.deleteOne({ name: "Abdullah" })
```

### 🗑️ ১৩. একাধিক ডকুমেন্ট ডিলিট করতে:
```js
db.users.deleteMany({ age: { $gt: 30 } })
```

---

## 🧰 অতিরিক্ত গুরুত্বপূর্ণ কমান্ড

### 🛠️ ১৪. কালেকশন ড্রপ (মুছে ফেলা):
```js
db.users.drop()
```

### 🧨 ১৫. ডেটাবেস ড্রপ (সাবধান!):
```js
db.dropDatabase()
```

---

## 📌 নোটস

- MongoDB shell ব্যবহার করলে প্রতিটি কমান্ডের শেষে `;` না দিলেও চলে।
- `insertOne`, `find`, `updateOne` ইত্যাদি মেথডগুলো `db.collectionName.method()` ফরম্যাটে ব্যবহার হয়।

---

📚 **উপকারি রিসোর্স:**
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [MongoDB University (Free Courses)](https://university.mongodb.com/)
