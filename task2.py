
guest1_stmt = """
INSERT INTO Bookings(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES(8, "Anees", "Java", "18:00", 6);"""
guest2_stmt = """
INSERT INTO Bookings(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES(5, "Bald", "Vin", "19:00", 6);"""
guest3_stmt = """
INSERT INTO Bookings(TableNo, GuestFirstName, GuestLastName, BookingSlot, EmployeeID)
VALUES(12, "Jay", "Kon", "19:30", 6);"""
guests = [{"name": "Anees Java", "insert_stmt": guest1_stmt},
          {"name": "Bald Vin", "insert_stmt": guest2_stmt},
          {"name": "Jay Kon", "insert_stmt": guest3_stmt}]
connections = []
for guest in guests:
    try:
        print(f"Trying to get connection for {guest['name']}")
        connection = con_pool.get_connection()
        connections.append(connection)
        print(f"success")
        cursor = connection.cursor()
        cursor.execute(guest["insert_stmt"])
        connection.commit()
    except errors.PoolError as e:
        print(f"Got error while getting connection for {guest['name']}, {e}")
        print("Adding new connection to pool")
        new_con = MySQLConnection(**dbconfig)
        con_pool.add_connection(new_con)
        print(f"Added new connection to pool, tryin to get connection for {guest['name']}")
        connection = con_pool.get_connection()
        connections.append(connection)
        print(f"success")
        cursor = connection.cursor()
        cursor.execute(guest["insert_stmt"])
        connection.commit()
# close all connections
for connection in connections:
    connection.close()

