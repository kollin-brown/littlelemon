connection = con_pool.get_connection()
cursor = connection.cursor(buffered=True)
upcoming_bookings_stmt = """
SELECT Bookings.BookingID,
CONCAT(Bookings.GuestFirstName, " ", Bookings.GuestLastName) AS Guest,
Bookings.BookingSlot,
Employees.Name, Employees.Role
FROM Bookings
JOIN Employees ON Bookings.EmployeeID = Employees.EmployeeID
ORDER BY BookingSlot
LIMIT 3;"""
cursor.execute(upcoming_bookings_stmt)
rows = cursor.fetchall()
print("Upcoming bookings:")
for row in rows:
    print(f"Booking slot: {row[2]}")
    print(f"  Guest name: {row[1]}")
    print(f"  Assigned to: {row[3]}[{row[4]}]")
connection.close()
