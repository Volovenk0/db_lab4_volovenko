CREATE TABLE Author
(
  gender VARCHAR(6) NOT NULL,
  author_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (author_name)
);

CREATE TABLE Sales
(
  num_sale_id INT NOT NULL,
  approximate_sales_in_millions INT NOT NULL,
  PRIMARY KEY (num_sale_id)
);

CREATE TABLE Book
(
  book_name VARCHAR(100) NOT NULL,
  original_language VARCHAR(20) NOT NULL,
  genre VARCHAR(100) NOT NULL,
  year_of_fist_publishing INT NOT NULL,
  author_name VARCHAR(100) NOT NULL,
  num_sale_id INT NOT NULL,
  PRIMARY KEY (book_name),
  FOREIGN KEY (author_name) REFERENCES Author(author_name),
  FOREIGN KEY (num_sale_id) REFERENCES Sales(num_sale_id)
);