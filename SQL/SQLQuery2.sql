SELECT
    Customer_Name,
    SUM(Sales) AS TotalSales,
    ROW_NUMBER() OVER (ORDER BY SUM(Sales) DESC) AS RowNum
FROM Superstore_clean
GROUP BY Customer_Name;