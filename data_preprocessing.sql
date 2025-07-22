SELECT
    s.store_id,
    s.date,
    SUM(s.sales_amount) AS total_sales,
    AVG(w.temperature) AS avg_temp,
    COUNT(*) AS transaction_count
FROM sales s
JOIN weather w ON s.date = w.date
WHERE s.date BETWEEN '2022-10-01' AND '2023-02-01'
GROUP BY s.store_id, s.date
HAVING total_sales > 500 AND transaction_count > 10
ORDER BY s.date ASC;