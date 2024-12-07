use project;
show tables;
select * from customer;
select count(*) from customer;
desc customer;

# filtering some columns using with limit-----
select * from customer order by customer_id desc limit 10;
select * from customer order by customer_id asc limit 10;
select distinct(age) from customer order by age desc limit 5 offset 0 ;


#filterind data order by customer id------
#find the first_name and last_name orderby customer_id? 
select customer_id,first_name,last_name from customer order by customer_id;
select customer_id,age,gender from customer;

# find the average salary for bet----
select  customer_id,salary,Total_Number_of_Bets, round(Salary/Total_Number_of_Bets) as avg_salary_for_bet from customer;

#descriptive analysis----
select avg(Age) ,min(Age),max(age),max(Age)-min(Age) as range_age,stddev(Age) as std_deviation,variance(Age) as variance from customer;
select avg(salary) ,min(Salary),max(Salary),max(Salary)-min(Salary) as range_salary,stddev(Salary) as std_deviation,variance(Salary) as var_sal from customer;
select avg(Total_Amount_Wagered) ,min(Total_Amount_Wagered),max(Total_Amount_Wagered),max(Total_Amount_Wagered)-min(Total_Amount_Wagered) as range_total_amount_wagered,stddev(Total_Amount_Wagered) as std_deviation,variance(Total_Amount_Wagered)as varinace_total_amount_wagerd from customer;
select avg(Average_Amount_of_Bonuses_Received) ,min(Average_Amount_of_Bonuses_Received),max(Average_Amount_of_Bonuses_Received),max(Average_Amount_of_Bonuses_Received)-min(Average_Amount_of_Bonuses_Received) as range_avg_amount_box,stddev(Average_Amount_of_Bonuses_Received) as std_deviation,variance(Average_Amount_of_Bonuses_Received) as var_avg_amo_bonuses_received from customer;
select avg(Number_of_Bonuses_Received) ,min(Number_of_Bonuses_Received),max(Number_of_Bonuses_Received),max(Number_of_Bonuses_Received)-min(Number_of_Bonuses_Received) as range_no_of_bonuses_received,stddev(Number_of_Bonuses_Received) as std_deviation,variance(Number_of_Bonuses_Received) as var_no_bonuses_received from customer;
select avg(Total_Number_of_Bets) ,min(Total_Number_of_Bets),max(Total_Number_of_Bets),max(Total_Number_of_Bets)-min(Total_Number_of_Bets) as range_total_no_pf_bets,stddev(Total_Number_of_Bets) as std_deviation,variance(Total_Number_of_Bets)as variance_total_no_bets from customer;

#skewness for all numerical columns----
select(sum(power(age-(select avg(age)from customer),3))/(count(*)* power((select  stddev(age)from customer),3)))as skewness
from customer;
select(sum(power(salary-(select avg(salary)from customer),3))/(count(*)* power((select  stddev(salary)from customer),3)))as skewness
from customer;
select(sum(power(Total_Amount_Wagered-(select avg(Total_Amount_Wagered)from customer),3))/(count(*)* power((select  stddev(Total_Amount_Wagered)from customer),3)))as skewness
from customer;
select(sum(power(Number_of_Bonuses_Received-(select avg(Number_of_Bonuses_Received) from customer),3))/(count(*)* power((select  stddev(Number_of_Bonuses_Received)from customer),3)))as skewness
from customer;
select(sum(power(Average_Amount_of_Bonuses_Received-(select avg(Average_Amount_of_Bonuses_Received) from customer),3))/(count(*)* power((select  stddev(Average_Amount_of_Bonuses_Received)from customer),3)))as skewness
from customer;
select(sum(power(Total_Number_of_Bets-(select avg(Total_Number_of_Bets) from customer),3))/(count(*)* power((select  stddev(Total_Number_of_Bets)from customer),3)))as skewness
from customer;

#kurtosis for all numerical columns----
select ((sum(power(age-(select avg(age)from customer),4))/(count(*)*power((select stddev(age)from customer),4)))-3)as kurtosis 
from customer;
select ((sum(power(salary-(select avg(salary) from customer),4))/(count(*)*power((select stddev(salary)from customer),4)))-3)as kurtosis
from customer;
select ((sum(power(Total_Amount_Wagered-(select avg(Total_Amount_Wagered)from customer),4))/(count(*)*power((select stddev(Total_Amount_Wagered)from customer),4)))-3)as kurtosis
from customer;
select ((sum(power(Number_of_Bonuses_Received-(select avg(Number_of_Bonuses_Received)from customer),4))/(count(*)*power((select stddev(Number_of_Bonuses_Received)from customer),4)))-3)as kurtosis
from customer;
select ((sum(power(Average_Amount_of_Bonuses_Received-(select avg(Average_Amount_of_Bonuses_Received)from customer),4))/(count(*)*power((select stddev(Average_Amount_of_Bonuses_Received)from customer),4)))-3)as kurtosis
from customer;
select ((sum(power(Total_Number_of_Bets-(select avg(Total_Number_of_Bets)from customer),4))/(count(*)*power((select stddev(Total_Number_of_Bets)from customer),4)))-3)as kurtosis
from customer;


# finding null values-----
select * from customer 
where 
age is null
or
salary is null
or
Total_Amount_Wagered is null
or
Average_Amount_of_Bonuses_Received is null
or
Total_Number_of_Bets is null
or
Number_of_Bonuses_Received is null;


#finding no of distinct countries--------
select count(distinct country) from customer;

#finding the no of countries
select country,count(*) from customer group by country;


#aggregate functions for salary----
#find the total salary for all customers----
select sum(salary) as total_salary_amount from customer;
#find the total salary for all customers for each country----
select country,sum(salary)as total_amount from customer group by country;
#find the distinct no.of bet_type_preferences for each country -----
select country,count(distinct Bet_Type_Preference) from customer group by country;

#finding the no of male and female customers by age
SELECT age, COUNT(gender)as male_customers FROM customer WHERE gender ='male' GROUP BY age;
SELECT age, COUNT(gender)as female_customers FROM customer WHERE gender ='female' GROUP BY age;

# finding the age where the greater than avg age----
select * from customer where age >(select avg(age) from customer);

#removing the low age and replace with avg age-----
#update and set----
# min age removing----
SET @avg_age = (SELECT AVG(age) FROM customer);
UPDATE customer
SET age = @avg_age
WHERE age <=15;

#filtering data with order by asc and desc----
select * from customer order by age asc,salary desc ;

#find the data which salary greater than 50000 and bonuses_received greater than 15----
select customer_id,age,salary,Number_of_Bonuses_Received from customer where salary >50000 and Number_of_Bonuses_Received>15  order by salary ;

# find the data where countries are india and nepal----
select * from customer where country='india' or country= 'nepal' order by age;
SELECT country, COUNT(*) AS customer_count
FROM customer
WHERE age > 18  
GROUP BY country HAVING COUNT(*) > 10;
select country,sum(salary),count(*) as cust_count from customer where age >=30 group by country having count(*) >10;


#finding the distinct bet_type_preference and  total salary from bet_type_preference-----
SELECT Bet_Type_Preference, COUNT(Bet_Type_Preference) AS preference_count, SUM(salary) AS total_salary FROM customer GROUP BY Bet_Type_Preference;
select country,max(salary) from customer group by country limit 10;

# finding the data where salary greater than 50000-----
select customer_id,salary from customer where salary > 50000 order by salary;

#finding the data and count where customer_id greater than 1 and less than 2----
select customer_id,salary from customer where customer_id >1 order by salary;
select customer_id,salary from customer where customer_id <2 order by salary;
select customer_id,count(*) from customer where customer_id >1 group by customer_id;

# find the distinct customer_id from the table----
select distinct customer_id from customer;
select distinct customer_id, first_name,last_name from customer;


#find the male customers that  age bw 20 and 25----- 
select count(*) from customer where age between 20 and 25 and gender='male';

#find the cus_id,gender, the data where salary between 40000 ans 50000----
select customer_id,Gender,Average_Amount_of_Bonuses_Received from customer where salary between 40000 and 50000;

#find the count of distinct country where between a and d---- 
select distinct country from customer where country between 'a' and 'd';

#using with in clause an find the customer age in bw 26 and 30------
select customer_id,age from customer where age in (26,30)order by customer_id ;
select customer_id,first_name,last_name,age,salary from customer where salary in(select salary from customer where age>30)order by customer_id;

#filtering the data where first_name _last_name starts like 'a' ----
select customer_id,first_name,last_name,age,salary from customer where first_name like 'a%';
select customer_id,first_name,last_name,age,salary from customer where last_name like '%a';

# maximum and minimum salary from country-----
select country,max(salary),min(salary) from customer group by country;

#total salary from each country above 1000000-----
SELECT country, SUM(salary) AS total_salary
FROM customer
GROUP BY country
HAVING sum(salary) > 1000000
order by country;

#max salary from each country above 50000----
SELECT country, max(salary) AS total_salary
FROM customer
GROUP BY country
HAVING max(salary) > 50000
order by country;

#maximum and minimum salary from country-----
select country,max(salary) as maxim_salary,min(salary) from customer group by country;
select customer_id,salary >max(salary)as second_highest_salary from customer;

SELECT customer_id, country,salary AS second_highest_salary
FROM customer
WHERE salary = (
    SELECT MAX(salary)
    FROM customer
    WHERE salary < (SELECT MAX(salary) FROM customer)group by country
);

#finding the second highest rank----
SELECT customer_id, country, salary AS second_highest_salary
FROM (
    SELECT customer_id, country, salary,
           ROW_NUMBER() OVER (PARTITION BY country ORDER BY salary DESC) AS row_rank
    FROM customer
) AS secong_highest
WHERE row_rank = 2;

#logical function using with case statemnt-----
#finding the who is master and beginner in bonus recieved
SELECT customer_id,total_Amount_Wagered,
    CASE 
        WHEN Number_of_Bonuses_Received <=15 THEN 'beginner'
        WHEN Number_of_Bonuses_Received >15 THEN 'master'
        ELSE 'learner'
    END AS consistency
FROM customer order by Total_Amount_Wagered;


#window functions -----
#select rank wise the salary and country
SELECT customer_id,Total_Amount_Wagered,Total_Number_of_Bets,Average_Amount_of_Bonuses_Received,salary,RANK() OVER (ORDER BY salary) AS rank_by_salary FROM customer;
SELECT customer_id,Total_Amount_Wagered,Average_Amount_of_Bonuses_Received,Number_of_Bonuses_Received,SUM(Salary) OVER (PARTITION BY salary) AS running_total FROM customer;
select customer_id,country,Bet_Type_Preference,salary,rank()over(partition by  Bet_Type_Preference order by salary desc)as rank_country from customer;


#finding the rank,row_no,dense_rank from country window functions using limit ------
select 
      customer_id,
      country,
      salary,
      age,
    rank()over(partition by country order by salary desc ) as rank_salary 
from customer limit 5; 

select 
    customer_id,
    salary,
    country,
    age,
    Bet_Type_Preference,
    Total_Amount_Wagered,rank()over(partition by bet_type_preference order by Total_Amount_Wagered)as rank_bet 
from customer;

#window functions  over()-----
select  
	customer_id,
	first_name,
	last_name,
	country,
	sum(salary)over() as total_salary 
from customer;

#window functions over(partition)-----
select 
     country,
     gender,
     salary,
     Bet_Type_Preference,
     sum(salary) over (partition by gender order by Bet_Type_Preference) as gender_type_salary 
from customer;

# finding the rank,row_no,dense_rank from customer_id window functions------
SELECT 
    customer_id,
    salary,
    country,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY salary desc) AS row_num,
    RANK() OVER (PARTITION BY customer_id ORDER BY salary DESC) AS rank_,
    DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY salary DESC) AS dense_rank_
FROM customer;

#finding the rank,row_no,dense_rank from country window functions------
SELECT 
    customer_id,
    age,
    salary,
    country,
    ROW_NUMBER() OVER (PARTITION BY country ORDER BY age desc) AS row_num,
    RANK() OVER (PARTITION BY country ORDER BY age DESC) AS rank_,
    DENSE_RANK() OVER (PARTITION BY country ORDER By age DESC) AS dense_rank_
FROM customer;

