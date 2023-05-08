connection = con_pool.get_connection()
cursor = connection.cursor()

# drop BasicSalesReport procedure if exists
drop_salesreport_procedure = """
DROP PROCEDURE IF EXISTS BasicSalesReport;
"""
cursor.execute(drop_salesreport_procedure)

create_salesreport_procedure = """
CREATE PROCEDURE BasicSalesReport()
BEGIN
SELECT SUM(BillAmount) AS Total_sales,
AVG(BillAmount) AS Average_bill,
MAX(BillAmount) AS Max_bill,
MIN(BillAmount) AS Min_bil
FROM Orders;
END;
"""
cursor.execute(create_salesreport_procedure)
sales_report = cursor.callproc("BasicSalesReport")
print("Basic sales report")
for result in cursor.stored_results():
    rows = result.fetchall()
    for row in rows:
        print(f"Total Sales: {row[0]}, Average bill: {row[1]}, Max bill: {row[2]}, Min bill: {row[3]}")
    
connection.close()


