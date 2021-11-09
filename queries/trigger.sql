CREATE TRIGGER insbef_salary_check
BEFORE INSERT ON employees
FOR EACH ROW EXECUTE PROCEDURE check_salary();