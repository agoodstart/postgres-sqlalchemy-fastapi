CREATE TABLE IF NOT EXISTS departments
(
	department_id smallserial PRIMARY KEY,
	department_name VARCHAR(50),
	location_id smallserial,
	FOREIGN KEY (location_id) REFERENCES locations(location_id) ON DELETE CASCADE
);