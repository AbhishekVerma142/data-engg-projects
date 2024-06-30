-- YOUR CODE HERE
with rental_info as (
select customer_id, AVG(EXTRACT(EPOCH from (r.return_date - r.rental_date)) / 86400) avg_duration
from public.rental r
group by 1
),
cust_info as (
SELECT first_name, last_name, customer_id
FROM public.customer c
),
overall_avg as (
select avg(avg_duration) as avg_duration
from rental_info
)
select first_name, last_name, round(ri.avg_duration, 2) avg_duration,
ntile(4) over (order by ri.avg_duration) quartile
from rental_info ri
join cust_info ci on ci.customer_id = ri.customer_id
cross join overall_avg oa
where ri.avg_duration > oa.avg_duration
order by ri.avg_duration desc;
