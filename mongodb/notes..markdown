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

 db.users.updateMany({fullTime:{$exists:false}},{$set:{fullTime:true}})
db.users.updateMany(
  { fullTime: { $exists: false } },  // Filter: documents where 'fullTime' field does NOT exist
  { $set: { fullTime: true } }       // Update: add 'fullTime' field and set it to true
)


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

students কালেকশনের মধ্যে যেসব ডকুমেন্টে registerdate ফিল্ড নাই,
 সেগুলো একসাথে ডিলিট করে দেবে।
db.students.deleteMany({ registerdate: { $exists: false } })


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



MongoDB Comparison Operators

// $eq => equal (সমান)
db.users.find({ age: { $eq: 25 } })
// যেসব ডকুমেন্টে age == 25, সেগুলো রিটার্ন করবে


// $ne => not equal (অসমান)
db.users.find({ age: { $ne: 25 } })
// যেসব ডকুমেন্টে age != 25, সেগুলো রিটার্ন করবে


// $gt => greater than (বড়)
db.users.find({ age: { $gt: 25 } })
// যেসব ডকুমেন্টে age > 25, সেগুলো রিটার্ন করবে


// $gte => greater than or equal (বড় বা সমান)
db.users.find({ age: { $gte: 25 } })
// যেসব ডকুমেন্টে age >= 25, সেগুলো রিটার্ন করবে


// $lt => less than (ছোট)
db.users.find({ age: { $lt: 25 } })
// যেসব ডকুমেন্টে age < 25, সেগুলো রিটার্ন করবে


// $lte => less than or equal (ছোট বা সমান)
db.users.find({ age: { $lte: 25 } })
// যেসব ডকুমেন্টে age <= 25, সেগুলো রিটার্ন করবে


// $in => value exists in array (একাধিক মানের মধ্যে আছে)
db.users.find({ age: { $in: [22, 25, 30] } })
// age যদি 22, 25 বা 30 হয়, এমন ডেটা দেখাবে


// $nin => value not in array (একাধিক মানের মধ্যে নেই)
db.users.find({ age: { $nin: [22, 25, 30] } })
// age যদি 22, 25, 30 না হয়, এমন ডেটা দেখাবে

$eq: সমান

$ne: সমান না

$gt: বড়

$gte: বড় বা সমান

$lt: ছোট

$lte: ছোট বা সমান

$in: নির্দিষ্ট মানগুলোর মধ্যে

$nin: নির্দিষ্ট মানগুলোর বাইরে

MongoDB Logical Operators (লজিক্যাল অপারেটর)

$and	সবগুলো শর্ত পূরণ করতে হবে
db.students.find({
  $and: [
    { age: { $gt: 18 } },
    { marks: { $gt: 80 } }
  ]
})
// ✅ English: Students older than 18 AND marks > 80
// ✅ বাংলা: যাদের বয়স ১৮-এর বেশি এবং মার্কস ৮০-এর বেশি


$or	যেকোনো একটি শর্ত পূরণ হলেই হবে

db.students.find({
  $or: [
    { age: 18 },
    { marks: { $gt: 80 } }
  ]
})
// ✅ English: Students aged 18 OR marks > 80
// ✅ বাংলা: যাদের বয়স ১৮ অথবা মার্কস ৮০-এর বেশি

$not	কোনো শর্তের বিপরীত (NOT) মান
db.students.find({
  age: { $not: { $gt: 18 } }
})
// ✅ English: Age NOT greater than 18
// ✅ বাংলা: যাদের বয়স ১৮-এর বেশি নয় (<= 18)


$nor	সব শর্তই মিথ্যা হতে হবে
db.students.find({
  $nor: [
    { age: 18 },
    { marks: 85 }
  ]
})
// ✅ English: Age is not 18 AND marks is not 85
// ✅ বাংলা: বয়স ১৮ নয় এবং মার্কস ৮৫ নয় এমন ছাত্ররা



## 📌 নোটস

- MongoDB shell ব্যবহার করলে প্রতিটি কমান্ডের শেষে `;` না দিলেও চলে।
- `insertOne`, `find`, `updateOne` ইত্যাদি মেথডগুলো `db.collectionName.method()` ফরম্যাটে ব্যবহার হয়।

---

MongoDB Index Example with Comment (English + Bangla)

// Create an index on the "name" field (ascending order)
db.users.createIndex({ name: 1 })

// 🔍 এটি "name" ফিল্ডের উপর ইনডেক্স তৈরি করবে যাতে name দিয়ে দ্রুত সার্চ করা যায়।


 2. Single Field Index (Descending)
// Create an index on the "age" field (descending order)
db.users.createIndex({ age: -1 })

// 🔍 এটি age ফিল্ডে descending (বড় থেকে ছোট) ইনডেক্স তৈরি করবে,
// যেন বয়স অনুযায়ী descending ভাবে sort করা সহজ হয়।


 Compound Index

 // Create index on both "name" and "age" fields
db.users.createIndex({ name: 1, age: -1 })

// 🔍 compound index: প্রথমে name দিয়ে এবং তারপর age দিয়ে ইনডেক্স কাজ করবে।


Multikey Index (Array field)

// Suppose each user has an array of skills
db.users.createIndex({ skills: 1 })

// 🔍 skills যদি একটি অ্যারে হয় (["Java", "Python"]), এটি ইনডেক্স হয়ে যাবে multikey index হিসাবে।


Text Index (Full-text Search)

// Create a text index on a field "bio"
db.users.createIndex({ bio: "text" })

// 🔍 bio ফিল্ডে text search (যেমন: $text operator) করার জন্য text index দরকার।

 Hashed Index

 // Create a hashed index on user_id (useful for sharding)
db.users.createIndex({ user_id: "hashed" })

// 🔍 hashed index শার্ডিং করার জন্য ব্যবহার হয়,
// যেখানে ডেটা সমভাবে বিভক্ত করতে হয়।

 Wildcard Index
 // Create wildcard index on all sub-fields of documents
db.users.createIndex({ "$**": 1 })

// 🔍 ডায়নামিক বা অপরিচিত ফিল্ডেও ইনডেক্স করা যায়, বিশেষ করে যেসব ডেটার স্ট্রাকচার ভিন্ন।


 Show All Indexes
 db.users.getIndexes()

// 🔍 এই কমান্ড দিয়ে আপনি দেখতে পারবেন, কোন কোন ইনডেক্স তৈরি করা হয়েছে।

❌ Drop Index

// Drop index by name
db.users.dropIndex("name_1")

// 🔍 name_1 হল ইনডেক্সের নাম, যেটা আপনি getIndexes() দিয়ে দেখে নিতে পারেন।


❌ Drop All Indexes
db.users.dropIndexes()

// 🔍 এটা দিয়ে সব ইনডেক্স মুছে যাবে, শুধু _id ইনডেক্স ছাড়া।



Performance Tip:
js
Copy
Edit
db.users.find({ name: "Anu" }).explain("executionStats")

// 🔍 explain("executionStats") দিয়ে দেখা যায়, কোয়েরি ইনডেক্স ব্যবহার করেছে কিনা।










cd "C:/Users/abdul/Downloads/mongosh-2.5.6-win32-x64/mongosh-2.5.6-win32-x64/bin"
./mongosh.exe

📚 **উপকারি রিসোর্স:**
- [MongoDB Documentation](https://www.mongodb.com/docs/)
- [MongoDB University (Free Courses)](https://university.mongodb.com/)
