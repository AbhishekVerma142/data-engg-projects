-- YOUR CODE HERE
with weekly_rentals as (
select date_trunc('week', r.rental_date) as week_start, count(r.rental_id) as rentals
from public.rental r
where r.rental_date >= rental_date - interval '5 months'
group by date_trunc('week', r.rental_date)
),
moving_averages as (
select week_start, rentals, avg(rentals) over (order by week_start rows between 2 preceding and current row) as moving_avg_3weeks,
lag(rentals, 1) over (order by week_start) as previous_week_rentals
from weekly_rentals
),
deviations as (
select week_start, rentals, moving_avg_3weeks, previous_week_rentals, rentals - previous_week_rentals as difference,
rentals - moving_avg_3weeks as deviation_from_avg
from moving_averages
)
select week_start as week, rentals, moving_avg_3weeks, difference, deviation_from_avg
from deviations
order by week_start;
