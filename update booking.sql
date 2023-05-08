DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `UpdateBooking`(IN Booking_ID INT, IN Booking_Date VARCHAR(20))
BEGIN

UPDATE Bookings
SET BookingDate = Booking_Date
WHERE BookingID = Booking_ID;

SELECT CONCAT("Booking ", Booking_ID, " Updated") AS "Confirmation";

END$$
DELIMITER ;
