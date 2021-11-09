CREATE TABLE IF NOT EXISTS employees
(
	employee_id smallserial PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	email VARCHAR(255) UNIQUE,
	phone_number VARCHAR(15),
	hire_date DATE NOT NULL,
	job_id smallserial,
	salary NUMERIC(7, 2) NOT NULL,
	manager_id smallserial,
	department_id smallserial,
	FOREIGN KEY (job_id) REFERENCES jobs(job_id),
	FOREIGN KEY (department_id) REFERENCES departments(department_id),
	FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
);

ALTER TABLE employees ALTER COLUMN manager_id DROP NOT NULL;