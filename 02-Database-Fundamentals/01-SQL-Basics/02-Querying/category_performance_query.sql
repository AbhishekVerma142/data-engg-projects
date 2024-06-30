-- YOUR CODE HERE
select *, case when revenue > 1000 then 'High' when revenue > 500 then 'Medium' else 'Low' end revenue_category from (
select name,sum(amount) revenue from public.category c
left join film_category fc on fc.category_id =c.category_id
left join public.film f on f.film_id = fc.film_id
left join inventory i on i.film_id = fc.film_id
left join rental r on r.inventory_id = i.inventory_id
left join payment p on p.rental_id =r.rental_id
group by 1 order by 2 desc) as data
