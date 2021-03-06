USE master;

CREATE DATABASE SGB;

USE SGB;

CREATE TABLE LOG_ADM(
	Adm_User VARCHAR(100) PRIMARY KEY,
	Password_Adm VARCHAR(100)
);

CREATE TABLE CLIENT(
	cpf VARCHAR(100) PRIMARY KEY,
	Name_Client VARCHAR(100),
	Phone_Number VARCHAR(20)
);

CREATE TABLE BOOKS(
	ID INT PRIMARY KEY IDENTITY,
	Title VARCHAR(100),
	Author Varchar(200),
	Publisher VARCHAR(50),
	Number_Pages INT,
	Genre VARCHAR(50),
	Publication_Date DATE,
	Quantity_Book INT
);

CREATE TABLE LOAN(
	Cod INT PRIMARY KEY IDENTITY,
	cpf VARCHAR(100) FOREIGN KEY (cpf) REFERENCES CLIENT,
	loan_date DATE,
	devolution_date DATE,
	status_loan VARCHAR(10)
);

CREATE TABLE ITEM(
	Cod INT FOREIGN KEY (Cod) REFERENCES LOAN,
	Id  INT FOREIGN KEY (ID) REFERENCES BOOKS,
);




