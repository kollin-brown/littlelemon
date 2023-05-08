DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddValidBooking`(IN Booking_date VARCHAR(20), IN Table_Number INT)
BEGIN
	DECLARE Status VARCHAR(20);
    
    START TRANSACTION;
    
    SELECT BookingID 
    INTO Status
    FROM Bookings
    WHERE BookingDate = Booking_Date AND TableNumber = Table_Number;
    
    INSERT INTO Bookings(BookingDate, TableNumber)
    VALUES(Booking_Date, Table_Number);
    
    IF Status IS NOT NULL 
		THEN 
			ROLLBACK; SELECT CONCAT('Table ', Table_Number, ' is already booked - Booking Cancelled') AS 'Booking Status'; 
		ELSE 
			COMMIT; SELECT CONCAT('Table ', Table_Number, ' is available for booking - Booking...') AS 'Booking Status'; 
		END IF;
END$$
DELIMITER ;
