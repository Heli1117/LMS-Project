CREATE DATABASE lms;
USE lms;
CREATE TABLE admins(
   admin_id INT AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(100) NOT NULL,
   password VARCHAR(50));

DROP Table librariens
   
CREATE TABLE librarians(
   librarian_id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
   username VARCHAR(100) NOT NULL,
   password VARCHAR(50),
   created_by_admin_id INT,
   FOREIGN KEY(created_by_admin_id)REFERENCES admins(admin_id)
);

CREATE TABLE books(
   book_id INT AUTO_INCREMENT PRIMARY KEY,
   title VARCHAR(100),
   author VARCHAR(100),
   isbn VARCHAR(50),
   section VARCHAR(50),
   stock_count INT ,
   status VARCHAR(50)
);

CREATE Table members(
   member_id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(100),
   email VARCHAR(50),
   registered_by_librarian_id INT,
   FOREIGN KEY(registered_by_librarian_id)REFERENCES librarians(librarian_id)

);


CREATE Table transactions(
   trasaction_id INT AUTO_INCREMENT PRIMARY KEY,
   book_id INT,
   member_id INT,
   librarian_id INT,
   issue_date DATE,
   return_date DATE,
   FOREIGN KEY(book_id)REFERENCES books(book_id),
   FOREIGN KEY(member_id)REFERENCES members(member_id),
   FOREIGN KEY(librarian_id)REFERENCES librarians(librarian_id)
);
SELECT TABLE_NAME,CONSTRAINT_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE `REFERENCED_TABLE_NAME`="librariens";


