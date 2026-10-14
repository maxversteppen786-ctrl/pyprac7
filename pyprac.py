#Practical no.7 : Regular Expressions and
Multithreading

Part A — Regular Expressions
Q1. Write a Python program to check whether a given
string contains a specific pattern using Regular
Expressions.
Code
import re
text = input(&quot;Enter a String: &quot;)
pattern = input(&quot;Enter Pattern to Search: &quot;)
result = re.search(pattern, text)
if result:
print(&quot;Pattern Found&quot;)
else:
print(&quot;Pattern Not Found&quot;)
Sample Output
Enter a String: Python Programming
Enter Pattern to Search: Python
Pattern Found

Q2. Write a Python program to find all occurrences of a
word in a given string using Regular Expressions.
Code
import re

text = &quot;Python is easy. Python is powerful. Python is popular.&quot;
pattern = &quot;Python&quot;
matches = re.findall(pattern, text)
print(&quot;Occurrences:&quot;, matches)
print(&quot;Number of Occurrences:&quot;, len(matches))
Output
Occurrences: [&#39;Python&#39;, &#39;Python&#39;, &#39;Python&#39;]
Number of Occurrences: 3

#Q3. Write a Python program to validate a mobile number
using Regular Expressions.
Code
import re
mobile = input(&quot;Enter Mobile Number: &quot;)
pattern = r&quot;^[6-9][0-9]{9}$&quot;
if re.fullmatch(pattern, mobile):
print(&quot;Valid Mobile Number&quot;)
else:
print(&quot;Invalid Mobile Number&quot;)
Sample Output
Enter Mobile Number: 9876543210
Valid Mobile Number

#Q4. Write a Python program to validate an email address
using Regular Expressions.
Code
import re

email = input(&quot;Enter Email Address: &quot;)
pattern = r&quot;^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$&quot;
if re.fullmatch(pattern, email):
print(&quot;Valid Email Address&quot;)
else:
print(&quot;Invalid Email Address&quot;)

#Q5. Write a Python program to extract all numbers from a
given string using Regular Expressions.
Code
import re
text = &quot;I have 10 apples, 25 oranges and 15 bananas.&quot;
numbers = re.findall(r&quot;\d+&quot;, text)
print(&quot;Numbers Found:&quot;, numbers)
Output
Numbers Found: [&#39;10&#39;, &#39;25&#39;, &#39;15&#39;]

#Q6. Write a Python program to replace multiple spaces in
a string with a single space using Regular Expressions.
Code
import re
text = &quot;Python is a programming language.&quot;
result = re.sub(r&quot;\s+&quot;, &quot; &quot;, text)
print(result)
Output

Python is a programming language.

Part B — Multithreading
#Q7. Write a Python program to create and execute a
thread.
Code
import threading
def display():
for i in range(1, 6):
print(&quot;Thread:&quot;, i)
t = threading.Thread(target=display)
t.start()
t.join()
print(&quot;Main Program Completed&quot;)

#Q8. Write a Python program to create multiple threads
and demonstrate their execution.
Code
import threading
def task(name):
for i in range(1, 4):
print(name, &quot;:&quot;, i)
t1 = threading.Thread(target=task, args=(&quot;Thread 1&quot;,))
t2 = threading.Thread(target=task, args=(&quot;Thread 2&quot;,))
t1.start()
t2.start()

t1.join()
t2.join()
print(&quot;All Threads Completed&quot;)
Note: The order of output from the two threads may vary because they execute concurrently.

Part C — Thread Synchronization
Q9. Write a Python program to demonstrate a race
condition when multiple threads access a shared
variable.
Code
import threading
counter = 0
def increment():
global counter
for i in range(100000):
counter += 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(&quot;Final Counter:&quot;, counter)
Purpose: This program demonstrates multiple threads working on the same shared resource.

#Q10. Write a Python program to synchronize access to a
shared resource using Lock.
Code
import threading
counter = 0
lock = threading.Lock()
def increment():
global counter
for i in range(100000):
with lock:
counter += 1
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start()
t2.start()
t1.join()
t2.join()
print(&quot;Final Counter:&quot;, counter)
Expected Output
Final Counter: 200000
Here, Lock ensures that only one thread modifies the shared variable at a time.

#Q11. Write a Python program to demonstrate thread
synchronization using Lock while accessing a shared
bank account.
Code

import threading
balance = 1000
lock = threading.Lock()
def withdraw(amount, name):
global balance
with lock:
if balance &gt;= amount:
print(name, &quot;is withdrawing&quot;, amount)
balance -= amount
print(&quot;Remaining Balance:&quot;, balance)
else:
print(name, &quot;cannot withdraw&quot;, amount)
print(&quot;Insufficient Balance&quot;)
t1 = threading.Thread(
target=withdraw,
args=(700, &quot;Thread 1&quot;)
)
t2 = threading.Thread(
target=withdraw,
args=(500, &quot;Thread 2&quot;)
)
t1.start()
t2.start()
t1.join()
t2.join()
print(&quot;Final Balance:&quot;, balance)
This is a good real-world example of synchronization.

Part D — Priority Queue with
Multithreading
Q12. Write a Python program to create a Priority Queue
and insert elements with different priorities.
Code
from queue import PriorityQueue
pq = PriorityQueue()
pq.put((3, &quot;Low Priority&quot;))
pq.put((1, &quot;High Priority&quot;))
pq.put((2, &quot;Medium Priority&quot;))
while not pq.empty():
priority, task = pq.get()
print(&quot;Priority:&quot;, priority, &quot;Task:&quot;, task)
Output
Priority: 1 Task: High Priority
Priority: 2 Task: Medium Priority
Priority: 3 Task: Low Priority
Important: In Python&#39;s PriorityQueue, a smaller priority number is processed first.

#Q13. Write a Python program to demonstrate Priority
Queue behavior using multiple threads.
Code
import threading
from queue import PriorityQueue
pq = PriorityQueue()

def add_tasks():
pq.put((3, &quot;Task C&quot;))
pq.put((1, &quot;Task A&quot;))
pq.put((2, &quot;Task B&quot;))
def process_tasks():
while not pq.empty():
priority, task = pq.get()
print(
&quot;Processing:&quot;,
task,
&quot;Priority:&quot;,
priority
)
t1 = threading.Thread(target=add_tasks)
t2 = threading.Thread(target=process_tasks)
t1.start()
t1.join()
t2.start()
t2.join()
print(&quot;All Tasks Completed&quot;)

#Q14. Write a Python program to implement a thread-safe
producer-consumer system using Queue.
Code
import threading
import queue
import time
q = queue.Queue()
def producer():
for i in range(1, 6):
print(&quot;Producing:&quot;, i)

q.put(i)
time.sleep(0.5)
def consumer():
for i in range(1, 6):
item = q.get()
print(&quot;Consuming:&quot;, item)
q.task_done()
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
print(&quot;Processing Completed&quot;)
This is useful for explaining how a queue can safely coordinate data between threads.

#Additional Practice
Q15. Write a Python program to validate a password
using Regular Expressions.
Conditions:
● Minimum 8 characters
● At least one uppercase letter
● At least one lowercase letter
● At least one digit
Code
import re

password = input(&quot;Enter Password: &quot;)
pattern = r&quot;^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$&quot;
if re.fullmatch(pattern, password):
print(&quot;Valid Password&quot;)
else:
print(&quot;Invalid Password&quot;)

#Q16. Write a Python program to extract dates from a
given text using Regular Expressions.
Code
import re
text = &quot;&quot;&quot;
Exam dates are 10-09-2026 and 25-09-2026.
The practical exam is on 05-10-2026.
&quot;&quot;&quot;
dates = re.findall(r&quot;\d{2}-\d{2}-\d{4}&quot;, text)
print(&quot;Dates Found:&quot;)
for date in dates:
print(date)
