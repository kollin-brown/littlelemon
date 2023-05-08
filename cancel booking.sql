DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `CancelBooking`(IN Booking_ID INT)
BEGIN

DELETE FROM Bookings
WHERE BookingID = Booking_ID;

SELECT CONCAT("Booking ", Booking_ID, " cancelled") AS "Confirmation";

END$$
DELIMITER ;
