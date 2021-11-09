SELECT 
	emp.first_name AS "First Name" ,
	emp.last_name AS "Last Name",
	emp.salary AS "Salary",
	jobs.job_title AS "Job Title",
	man.first_name || ' ' || man.last_name AS "Current Manager",
	departments.department_name AS "Department",
	locations.city || ', ' || countries.country_name || ', ' || regions.region_name AS "Location"
FROM 
	employees emp
	LEFT JOIN employees man ON emp.manager_id = man.employee_id
	INNER JOIN jobs ON jobs.job_id = emp.job_id
	INNER JOIN departments ON departments.department_id = emp.department_id
	INNER JOIN locations ON locations.location_id = departments.location_id
	INNER JOIN countries ON countries.country_id = locations.country_id
	INNER JOIN regions ON regions.region_id = countries.region_id;