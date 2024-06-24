import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object to insert record, create table
cursor = connection.cursor()

# Drop the existing table if it exists
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create the table
table_info = """
CREATE TABLE STUDENT (
    ID INTEGER PRIMARY KEY,
    roll_number INTEGER,
    name VARCHAR(50),
    enrollment_number INTEGER,
    attendance VARCHAR(10),
    marks REAL
);
"""
cursor.execute(table_info)

# Insert some records
records = [
    (303303320001, 'abhilash s', 'BJ5601', '70%', 57.50),
    (303303320002, 'aditya soni', 'BJ5602', '80%', 20.00),
    (303303320003, 'aadesh gaurkhede', 'BJ5603', '75%', 51.67),
    (303303320004, 'aanchal tikariha', 'BJ5604', '72%', 43.33),
    (303303320005, 'aastha soni', 'BJ5605', '77%', 41.33),
    (303303320006, 'abhinav shrivastava', 'BJ5606', '76%', 35.00),
    (303303320007, 'abhishek tiwari', 'BJ5607', '85%', 32.50),
    (303303320008, 'aditi badwaik', 'BJ5608', '90%', 39.67),
    (303303320009, 'akshat khandelwal', 'BJ5609', '55%', 31.67),
    (303303320010, 'akshat tiwari', 'BJ5610', '100%', 100.00),
    (303303320011, 'anay mishra', 'BJ5611', '77%', 11.00),
    (303303320012, 'aniket nagpure', 'BJ5612', '87%', 7.40),
    (303303320013, 'ankit ojha', 'BJ5613', '90%', 3.33),
    (303303320014, 'ashish chaubey', 'BJ5614', '99%', 23.44),
    (303303320015, 'atharwa kale', 'BJ5615', '71%', 74.88),
    (303303320016, 'bhavesh vishwakarma', 'BJ5616', '74%', 77.88),
    (303303320017, 'deeksha yadav', 'BJ5617', '79%', 67.32),
    (303303320018, 'diksha verma', 'BJ5618', '88%', 13.99),
    (303303320019, 'divyank verma', 'BJ5619', '66%', 14.88),
    (303303320020, 'garvit rathore', 'BJ5620', '87%', 29.00),
    (303303320021, 'gitanjali sahu', 'BJ5621', '78%', 22.88),
    (303303320022, 'deepesh kumar', 'BJ5622', '76%', 66.99),
    (303303320023, 'hemant sahu', 'BJ5623', '74%', 0.00),
    (303303320024, 'himani bisen', 'BJ5624', '79%', 71.56),
    (303303320025, 'jayesh manikpuri', 'BJ5625', '89%', 0.00),
    (303303320026, 'moulshree dubey', 'BJ5626', '99%', 42.76),
    (303303320027, 'muskan sahu', 'BJ5627', '95%', 67.44),
    (303303320028, 'prakriti verma', 'BJ5628', '94%', 0.00),
    (303303320029, 'priyanshu mazumdar', 'BJ5629', '92%', 71.67),
    (303303320030, 'sarthak pandey', 'BJ5630', '92%', 56.57),
    (303303320031, 'saurabh kumar', 'BJ5631', '73%', 0.00),
    (303303320032, 'shashank dewangan', 'BJ5632', '71%', 44.15),
    (303303320033, 'shivam chandak', 'BJ5633', '78%', 74.88),
    (303303320034, 'shruti dewangan', 'BJ5634', '99%', 40.83),
    (303303320035, 'shubham majumdar', 'BJ5635', '100%', 47.76),
    (303303320036, 'shubham soni', 'BJ5636', '80%', 71.67),
    (303303320037, 'siddharth sharma', 'BJ5637', '90%', 65.83),
    (303303320038, 'suvigya mishra', 'BJ5638', '55%', 70.00),
    (303303320039, 'swapn saket gupta', 'BJ5639', '99%', 35.83),
    (303303320040, 'tanushri roy', 'BJ5640', '73%', 0.00),
    (303303320041, 'umaraman singh', 'BJ5641', '66%', 25.00),
    (303303320042, 'vaibhav wadetwar', 'BJ5642', '65%', 57.99),
    (303303320043, 'vibhuti sharma', 'BJ5643', '62%', 56.77),
    (303303320044, 'vivek verma', 'BJ5644', '72%', 43.77),
    (303303320045, 'yashraj dewangan', 'BJ5645', '80%', 30.00),
    (303303320046, 'lavanya sharma', 'BJ5646', '90%', 45.88),
    (303303320047, 'akhilesh sharma', 'BJ5647', '55%', 0.00),
    (303303320048, 'aman pradeep thakur', 'BJ5648', '99%', 33.33),
    (303303320049, 'lokesh kumar sondhiya', 'BJ5649', '73%', 24.88),
    (303303320050, 'yashraj singh chanana', 'BJ5650', '66%', 42.88),
    (303303320051, 'yashraj singh', 'BJ5651', '65%', 0.00),
    (303303320052, 'anish kumar', 'BJ5652', '62%', 50.65),
    (303303320053, 'sandeep singh', 'BJ5653', '72%', 50.50)
]

cursor.executemany('''INSERT INTO STUDENT (roll_number, name, enrollment_number, attendance, marks) VALUES (?, ?, ?, ?, ?)''', records)

# Display all the records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
