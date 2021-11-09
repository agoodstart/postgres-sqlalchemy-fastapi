CREATE TABLE regions
(
	region_id smallserial PRIMARY KEY,
	region_name varchar(30) UNIQUE NOT NULL
);