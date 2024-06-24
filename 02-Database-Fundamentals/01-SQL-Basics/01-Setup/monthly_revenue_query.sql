-- YOUR CODE HERE
select date_part('month',payment_date) as month, sum(amount) monthly_revenue from public.payment where date_part('year', payment_date) = 2022 group by 1 order by 1;
