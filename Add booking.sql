DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `AddBooking`(IN Booking_ID INT, IN Customer_ID INT, IN Booking_Date VARCHAR(20), IN Table_Number INT)
BEGIN

INSERT INTO Bookings(BookingID, CustomerID, BookingDate, TableNumber)
VALUES(Booking_ID, Customer_ID, Booking_Date , Table_Number);

SELECT "New Booking Added" AS "Confirmation";

END$$
DELIMITER ;
