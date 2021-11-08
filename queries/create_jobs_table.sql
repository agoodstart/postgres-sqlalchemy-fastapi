CREATE TABLE IF NOT EXISTS jobs
(
	job_id smallserial PRIMARY KEY,
	job_title VARCHAR(50),
	min_salary NUMERIC(7, 2),
	max_salary NUMERIC (7, 2)
);