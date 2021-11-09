CREATE TABLE IF NOT EXISTS locations
(
	location_id smallserial PRIMARY KEY,
	street_address VARCHAR(50),
	postal_code VARCHAR(10),
	city VARCHAR(100),
	state_province VARCHAR(25),
	country_id CHAR(2),
	FOREIGN KEY (country_id) REFERENCES countries(country_id) ON DELETE CASCADE
);