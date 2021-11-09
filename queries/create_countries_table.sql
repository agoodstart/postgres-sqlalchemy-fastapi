CREATE TABLE IF NOT EXISTS countries
(
	country_id CHAR(2),
	country_name VARCHAR(100),
	region_id smallserial NOT NULL,
	FOREIGN KEY (region_id) REFERENCES regions(region_id) ON DELETE CASCADE
);

ALTER TABLE countries ADD PRIMARY KEY(country_id);