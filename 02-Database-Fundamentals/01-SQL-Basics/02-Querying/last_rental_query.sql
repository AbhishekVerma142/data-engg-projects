-- YOUR CODE HERE
with cust as(
select distinct customer_id, concat(first_name,' ', last_name) full_name,c.last_update,
case when cast(last_update as date) >= cast(last_update as date) - interval '6 months' and c.active= 0 then 'Active' else 'Inactive' end status
from customer c)
select full_name, max(rental_date) last_rental_date,status
from rental r
left join cust on cust.customer_id = r.customer_id
where cast(r.rental_date as date) >= cast(r.rental_date as date) - interval '3 months'  group by 1,3 order by max(r.rental_date)
