SELECT 
    delivery_date, 
    status, 
    COUNT(*) AS open_order_count
FROM 
    operations.orders
WHERE 
    status <> 'COMPLETED'
GROUP BY 
    delivery_date, 
    status
ORDER BY 
    delivery_date;