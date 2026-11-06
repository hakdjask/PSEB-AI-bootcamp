CREATE DATABASE IF NOT EXISTS library; 

USE library; 

CREATE TABLE IF NOT EXISTS books(
	id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(200) NOT NULL,
    year INT,
    price DECIMAL(10, 2) NOT NULL
);

INSERT INTO books (id, title, author, year, price)
VALUES
    (1, 'Atomic Habits', 'James Clear', 2018, 1200.00),
    (2, 'The Alchemist', 'Paulo Coelho', 1988, 450.00),
    (3, '1984', 'George Orwell', 1949, 650.00),
    (4, 'Animal Farm', 'George Orwell', 1945, 350.00),
    (5, 'The Hobbit', 'J. R. R. Tolkien', 1937, 900.00),
    (6, 'Pride and Prejudice', 'Jane Austen', 1813, 500.00),
    (7, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 550.00),
    (8, 'Jane Eyre', 'Charlotte Bronte', 1847, 700.00);
    
-- Display books priced above 500

SELECT *
FROM books
WHERE price > 500;

-- Display all books sorted by price (highest first)

SELECT *
FROM books
ORDER BY price DESC;

-- Count the total number of books

SELECT COUNT(*) AS total_books
FROM books;

-- Update one book price and then displaying it

UPDATE books
SET price = 200.00
WHERE id = 2;

SELECT *
FROM books
WHERE id = 2;

COMMIT;