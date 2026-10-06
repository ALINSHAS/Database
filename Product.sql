USE shop;

-- CREATE TABLE Product (
--     pid INT PRIMARY KEY,
--     pname VARCHAR(20),
--     price INT
-- );

-- CREATE TABLE Order_details (
--     order_id INT PRIMARY KEY,
--     p_id INT,
--     quantity INT,
--     `date` DATE,
-- );

-- INSERT INTO Product (pid, pname, price)
-- VALUES
--     (1, 'prodA', 1000),
--     (2, 'prodB', 500),
--     (3, 'prodc', 250),
--     (4, 'prodD', 2000),
--     (5, 'prodE', 200);

-- INSERT INTO Order_details (order_id, p_id, quantity, `date`)
-- VALUES
--     (1, 2, 2, '2026-08-12'),
--     (2, 3, 1, '2026-08-13');

-- SELECT * FROM Product;
-- SELECT * FROM Order_details;

-- SELECT pname,price,order_id FROM Product INNER JOIN Order_details ON Product.pid=Order_details.p_id WHERE order_id=2;
