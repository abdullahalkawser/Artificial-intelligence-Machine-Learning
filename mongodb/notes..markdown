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

### 🔢 ৯. নির্দিষ্ট একটি ডেটা দেখতে: db: এটি বর্তমান সিলেক্ট করা ডাটাবেজকে নির্দেশ করে।

users: এটি একটি collection (যেটা রিলেশনাল ডেটাবেসে table-এর মতো)।

.find(): এটি একটি query method, যেটা নির্দিষ্ট শর্ত অনুযায়ী ডেটা খুঁজে বের করে।

{age: 25}: এটি হলো query object — অর্থাৎ আমরা এমন সব ডকুমেন্ট চাই যাদের বয়স (age) ২৫।
```js
db.users.findOne({ age: 22 })

db.collection.find(query, projection)

// query: কী খুঁজবে (যেমন { age: 25 })

// projection: কোন ফিল্ডগুলো দেখাবে (যেমন { name: 1 })

[
  { "_id": 1, "name": "Abdullah", "age": 25, "city": "Dhaka" },
  { "_id": 2, "name": "Rahim", "age": 23, "city": "Chittagong" }
]


 db.users.find({}, { _id: false, name: true })

db.users.find({}) → সব ডেটা খুঁজবে (query অংশ ফাঁকা, মানে সব ডেটা)

projection: { _id: false, name: true } → শুধুমাত্র name ফিল্ড দেখাবে, এবং _id দেখাবে না।

 db.users.find({},{_id: false ,name:true})

```

db.collection.find().sort({ field: 1 })   // ascending order
db.collection.find().sort({ field: -1 })  // descending order



Limiting 

db.users.find().limit(3)

: প্রথম ৩ জন ইউজার

 Combine Sorting + Limiting

 db.users.find().sort({ age: -1 }).limit(2)

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

db.collection.updateOne(
  { filter },
  { $unset: { fieldName: "" } }
) মান হিসেবে খালি string ("") বা যেকোনো কিছু দিতে পারো, MongoDB শুধু key দেখেই বুঝে নেয় যে এটা ডিলিট করতে হবে।


db.collection.find({ fieldName: { $exists: true } }) $exists হল একটি query operator যা কোনো ফিল্ড ডকুমেন্টে আছে কিনা তা চেক করতে ব্যবহৃত হয়।


db.users.find({
  age: { $exists: true, $gte: 23 }
})
📌 অর্থ: age আছে, এবং সেটা ২৩ বা তার বেশি।














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


cd "C:/Users/abdul/Downloads/mongosh-2.5.6-win32-x64/mongosh-2.5.6-win32-x64/bin"
./mongosh.exe

📚 **উপকারি রিসোর্স:**
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [MongoDB University (Free Courses)](https://university.mongodb.com/)
