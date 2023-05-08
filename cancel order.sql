DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `CancelOrder`(IN ID int)
BEGIN
    DELETE FROM Orders WHERE OrderId = Id;
    SELECT CONCAT('Order ', Id, ' is cancelled') AS Confirmation; 
    
END$$
DELIMITER ;
