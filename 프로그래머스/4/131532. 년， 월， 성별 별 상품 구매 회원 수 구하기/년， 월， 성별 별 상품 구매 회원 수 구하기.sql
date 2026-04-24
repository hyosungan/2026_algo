with user as (select * from user_info where gender is not null)

select year(SALES_DATE) as YEAR,month(SALES_DATE) as MONTH ,gender as GENDER,count(DISTINCT o.USER_ID) as USERS
from user u join online_sale o on u.user_id=o.user_id
group by YEAR,MONTH,gender
order by YEAR,MONTH,gender