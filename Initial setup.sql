show databases;
#1 create database
create database lms;
#2 create tables
use lms;
create table Librarian(username varchar(255),passwd varchar(255),name varchar(255), primary key(username));
select * from Librarian;
create table Books(id varchar(255),title varchar(255),authour varchar(255),isbn varchar(255),publish_year int,stat varchar(255),primary key(id));
select * from Books;
create table Members(id varchar(255),username varchar(255),passwd varchar(255),m_name varchar(255),email varchar(255),membership_date date,primary key(id));
select * from Members;
create table Borrow(id varchar(255),book_id varchar(255),member_id varchar(255), borrow_date date, return_date date,primary key(id),foreign key(book_id) references Books(id),foreign key(member_id) references Members(id)) ;
select * from Borrow;

create table Deleted_Books(id varchar(255),title varchar(255),authour varchar(255),isbn varchar(255),publish_year int,stat varchar(255),primary key(id));
create table Deleted_Members(id varchar(255),username varchar(255),passwd varchar(255),m_name varchar(255),email varchar(255),membership_date date,primary key(id));


INSERT INTO Librarian (username, passwd, name) VALUES
('lib1', 'password123', 'John Doe'),
('lib2', 'password456', 'Jane Smith'),
('lib3', 'password789', 'Michael Johnson');

INSERT INTO Books (id, title, authour, isbn, publish_year, stat) VALUES
('B001', 'The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 1925, 'available'),
('B002', 'To Kill a Mockingbird', 'Harper Lee', '9780061120084', 1960, 'borrowed'),
('B003', '1984', 'George Orwell', '9780451524935', 1949, 'available'),
('B004', 'Moby-Dick', 'Herman Melville', '9781503280786', 1851, 'available'),
('B005', 'Pride and Prejudice', 'Jane Austen', '9781503290563', 1813, 'borrowed');

INSERT INTO Members (id, username, passwd, m_name, email, membership_date) VALUES
('M001', 'member1', 'pass123', 'Alice Brown', 'alice@example.com', '2022-05-14'),
('M002', 'member2', 'pass456', 'Bob White', 'bob@example.com', '2022-07-20'),
('M003', 'member3', 'pass789', 'Charlie Green', 'charlie@example.com', '2023-01-12');

INSERT INTO Borrow (id, book_id, member_id, borrow_date, return_date) VALUES
('BR003', 'B001', 'M003', '2024-09-20', '2024-10-05'),
('BR004', 'B003', 'M001', '2024-09-25', '2024-10-10'),
('BR005', 'B004', 'M002', '2024-09-28', '2024-10-12'),
('BR006', 'B002', 'M003', '2024-10-05', '2024-10-19'),
('BR007', 'B001', 'M002', '2024-10-07', '2024-10-21'),
('BR008', 'B005', 'M001', '2024-10-08', '2024-10-22'),
('BR009', 'B004', 'M003', '2024-10-06', '2024-10-20');

#3 create library admin user and give it database access
create user 'library_admin'@'localhost' identified by 'Abcd@1234';
grant all privileges on lms.* to 'library_admin'@'localhost';

#4 create user roles librarian and member
create user 'librarian'@'localhost' identified by 'Abcd@1234';
create user 'member'@'localhost' identified by 'Abcd@1234';

#5 give previllages to librarians and members
grant select, update, delete, insert on lms.Books to 'librarian'@'localhost';
grant select, update, delete, insert on lms.Members to 'librarian'@'localhost';
grant select, update, delete, insert on lms.Deleted_Books to 'librarian'@'localhost';
grant select, update, delete, insert on lms.Deleted_Members to 'librarian'@'localhost';

grant select, update, delete, insert on lms.Borrow to 'librarian'@'localhost';


grant select on lms.Books to 'member'@'localhost';
grant select, update, delete, insert on lms.Borrow to 'member'@'localhost';




#6 API setup

#7 UI setup
    