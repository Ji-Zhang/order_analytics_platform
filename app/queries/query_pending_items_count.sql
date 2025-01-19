SELECT 
    o.delivery_date, 
    COUNT(oi.order_item_id) AS item_count
FROM 
    operations.order_items oi
INNER JOIN 
    operations.orders o
ON 
    oi.order_id = o.order_id
WHERE 
    o.status = 'PENDING'
GROUP BY 
    o.delivery_date
ORDER BY 
    o.delivery_date;