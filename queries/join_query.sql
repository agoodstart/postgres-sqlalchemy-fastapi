WITH ceiled_salaries AS (
	SELECT CEILING(salary / 10000) * 10000 AS ceiled_salary 
	FROM employees
)
SELECT 
	emp.first_name AS first_name,
	emp.last_name AS last_name,
	CEILING(emp.salary / 10000) * 10000 AS ceiled_salary,
	jobs.job_title AS job_title,
	man.first_name || ' ' || man.last_name AS manager_full_name,
	departments.department_name AS department_name,
	locations.city || ', ' || countries.country_name || ', ' || regions.region_name AS current_location,
	(
		SELECT COUNT(ceiled_salary)
		FROM ceiled_salaries
		GROUP BY ceiled_salary
		HAVING ceiled_salary = (CEILING(emp.salary / 10000) * 10000)
	) AS salary_count
FROM 
	employees emp
	LEFT JOIN employees man ON emp.manager_id = man.employee_id
	INNER JOIN jobs ON jobs.job_id = emp.job_id
	INNER JOIN departments ON departments.department_id = emp.department_id
	INNER JOIN locations ON locations.location_id = departments.location_id
	INNER JOIN countries ON countries.country_id = locations.country_id
	INNER JOIN regions ON regions.region_id = countries.region_id
ORDER BY
	ceiled_salary DESC;