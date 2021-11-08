CREATE FUNCTION check_salary()
	RETURNS TRIGGER
	LANGUAGE PLPGSQL
AS $$
DECLARE
	mins NUMERIC(7, 2);
	maxs NUMERIC(7, 2);
BEGIN
	SELECT min_salary, max_salary
		into mins, maxs
	FROM jobs
	WHERE NEW.job_id = jobs.job_id;

	IF NOT NEW.salary BETWEEN mins AND maxs THEN
		RAISE EXCEPTION 'Salary not between salary constraints';
	END IF;
	RETURN NEW;
END;
$$