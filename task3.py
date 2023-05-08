connection = con_pool.get_connection()
cursor = connection.cursor()
# Name and ID of LL manager
get_manager_stmt = """
SELECT EmployeeID, Name FROM Employees WHERE Role = "Manager";
"""
cursor.execute(get_manager_stmt)
rows = cursor.fetchall()
cols = cursor.column_names
for row in rows:
    print(f"Manager of Little Lemon is, {cols[0]}: {row[0]}, {cols[1]}: {row[1]}")
highest_salary_stmt ="""
SELECT Name, Role, Annual_Salary FROM Employees
ORDER BY Annual_Salary DESC
LIMIT 1;"""
cursor.execute(highest_salary_stmt)
rows = cursor.fetchall()
cols = cursor.column_names
for row in rows:
    print(f"Employee with highest salary is, {cols[0]}: {row[0]}, {cols[1]}: {row[1]}")

# Num of guests booked between 6:00 and 8:00
guests_18_20_stmt ="""
SELECT COUNT(BookingID) FROM Bookings AS Number_of_bookings
WHERE BookingSlot BETWEEN "18:00" AND "20:00";"""
cursor.execute(guests_18_20_stmt)
rows = cursor.fetchall()
cols = cursor.column_names
for row in rows:
    print(f"Number of bookings between 18:00 and 20:00 are:  {row[0]}")

bookings_waiting_stmt = """
SELECT Bookings.BookingID, CONCAT(GuestFirstName, " ", GuestLastName) AS Guest, BookingSlot
FROM Bookings
LEFT JOIN Orders ON Bookings.BookingID = Orders.BookingID
WHERE Orders.BookingID IS NULL
ORDER BY BookingSlot;"""
cursor.execute(bookings_waiting_stmt)
rows = cursor.fetchall()
print("Guests waiting for table:")
for row in rows:
    print(f" Guest {row[1]} with BookingID {row[0]} is waiting for timesot {row[2]} ")

connection.close()    
bookings_waiting_stmt = """
SELECT Bookings.BookingID, CONCAT(GuestFirstName, " ", GuestLastName) AS Guest, BookingSlot
FROM Bookings
LEFT JOIN Orders ON Bookings.BookingID = Orders.BookingID
WHERE Orders.BookingID IS NULL
ORDER BY BookingSlot;"""
cursor.execute(bookings_waiting_stmt)
rows = cursor.fetchall()
print("Guests waiting for table:")
for row in rows:
    print(f" Guest {row[1]} with BookingID {row[0]} is waiting for timesot {row[2]} ")

connection.close()    
