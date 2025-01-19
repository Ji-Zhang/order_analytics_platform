SELECT 
    delivery_date, 
    COUNT(*) AS open_order_count
FROM 
    operations.orders
WHERE 
    status <> 'COMPLETED'
GROUP BY 
    delivery_date
ORDER BY 
    open_order_count DESC
LIMIT 3;