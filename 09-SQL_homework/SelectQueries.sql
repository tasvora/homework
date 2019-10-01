select * from departments;
select * from employees;
select * from dept_emp;
select *  from dept_manager;
select * from salaries;
select * from titles;

--1)List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.emp_no AS "Employee Number",  
last_name AS "Last Name", first_name AS "First Name", gender, salary
from employees 
INNER JOIN salaries ON
employees.emp_no = salaries.emp_no;
--2)List employees who were hired in 1986.
select count(*) from employees where extract(year from hire_date)='1986';

--3)List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, 
employees.first_name, employees.last_name , employees.emp_no,  dept_manager.from_date, dept_manager.to_date
FROM employees 
inner join dept_manager
on employees.emp_no = dept_manager.emp_no
inner join departments 
on departments.dept_no =dept_manager.dept_no;
    

--4)List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT departments.dept_name, employees.emp_no,  employees.last_name, employees.first_name
FROM employees 
inner join dept_emp
on employees.emp_no = dept_emp.emp_no
inner join departments 
on departments.dept_no =dept_emp.dept_no;
--5)List all employees whose first name is "Hercules" and last names begin with "B."
SELECT count(*) from employees WHERE first_name='Hercules' and last_name LIKE 'B%';
--6)List all employees in the Sales department, including their employee number, last name, first name, and department name.
select * from employees where emp_no IN (
	SELECT emp_no from dept_emp WHERE dept_no IN(
		SELECT dept_no from departments where dept_name='Sales'
	)
)
--7)List all employees in the Sales and Development departments, including their employee number, 
--last name, first name, and department name.
select * from employees where emp_no IN (
	SELECT emp_no from dept_emp WHERE dept_no IN(
		SELECT dept_no from departments where dept_name IN('Sales','Development')
	)
)
SELECT departments.dept_name, employees.emp_no,  employees.last_name, employees.first_name
FROM employees 
inner join dept_emp
on employees.emp_no = dept_emp.emp_no
inner join departments 
on departments.dept_no =dept_emp.dept_no AND departments.dept_name IN('Sales','Development') ;

--8)In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT last_name, COUNT(last_name) AS "lastname count"
FROM employees
GROUP BY last_name
ORDER BY "lastname count" DESC;