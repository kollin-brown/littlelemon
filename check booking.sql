DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `CheckBooking`(IN Booking_Date varchar(20), IN Table_Number INT)
BEGIN
	DECLARE Table_Status VARCHAR(20) DEFAULT NULL;
    
    SELECT BookingID
    INTO Table_Status
    FROM Bookings
    WHERE BookingDate = Booking_Date AND TableNumber = Table_Number;
    
    SELECT
		CASE 
			WHEN Table_Status IS NOT NULL 
				THEN CONCAT('Table ', Table_Number, ' is already booked') 
			ELSE CONCAT('Table ', Table_Number, ' is available for booking')
		END 'Booking Status';

END$$
DELIMITER ;
