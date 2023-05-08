DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetMaxQuantity`()
SELECT MAX(Quantity) AS `Max Quantity in Order`
FROM Orders$$
DELIMITER ;
