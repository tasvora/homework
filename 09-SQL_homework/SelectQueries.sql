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
select * from employees where extract(year from hire_date)='1986';

--3)List the manager of each department with the following information: 
--department number, department name, the manager's employee number, last name, first name, and start and end employment dates
SELECT departments.dept_no AS "Department Number", departments.dept_name AS "Department Name", employees.emp_no AS "Employee Number", 
employees.first_name AS "First Name", employees.last_name AS "Last Name", dept_manager.from_date AS "Emp Start Date", 
dept_manager.to_date AS "Emp To Date"
FROM employees 
inner join dept_manager
on employees.emp_no = dept_manager.emp_no
inner join departments 
on departments.dept_no =dept_manager.dept_no;
    

--4)List the department of each employee with the following information: 
--employee number, last name, first name, and department name.
SELECT employees.emp_no AS "Employee Number",  employees.last_name AS "Last Name", employees.first_name AS "First Name",
departments.dept_name AS "Department Name"
FROM employees 
inner join dept_emp
on employees.emp_no = dept_emp.emp_no
inner join departments 
on departments.dept_no =dept_emp.dept_no;

--5)List all employees whose first name is "Hercules" and last names begin with "B."
SELECT * from employees WHERE first_name='Hercules' and last_name LIKE 'B%';

--6)List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT employees.emp_no AS "Employee Number",  employees.last_name AS "Last Name", employees.first_name AS "First Name",
departments.dept_name AS "Department Name"
FROM employees 
inner join dept_emp
on employees.emp_no = dept_emp.emp_no
inner join departments 
on departments.dept_no =dept_emp.dept_no AND departments.dept_name ='Sales' ;

--7)List all employees in the Sales and Development departments, including their employee number, 
--last name, first name, and department name.
SELECT departments.dept_name AS "Department Name", 
employees.emp_no AS "Employee Number",  employees.last_name AS "Last Name", employees.first_name AS "First Name"
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


--Search your ID number.
SELECT departments.dept_name AS "Department Name", 
employees.emp_no AS "Employee Number",  employees.last_name AS "Last Name", employees.first_name AS "First Name"
FROM employees 
inner join dept_emp
on employees.emp_no = dept_emp.emp_no
inner join departments 
on departments.dept_no =dept_emp.dept_no AND employees.emp_no = '499942';


