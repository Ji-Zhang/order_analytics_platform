SELECT 
    c.customer_id, 
    c.customer_name, 
    COUNT(o.order_id) AS pending_order_count
FROM 
    operations.customers c
INNER JOIN 
    operations.orders o
ON 
    c.customer_id = o.customer_id
WHERE 
    o.status = 'PENDING'
GROUP BY 
    c.customer_id, c.customer_name
ORDER BY 
    pending_order_count DESC
LIMIT 3;