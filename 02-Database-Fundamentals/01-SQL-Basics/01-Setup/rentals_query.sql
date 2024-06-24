-- YOUR CODE HERE
select title, c.name category_name,count(r.rental_id) rental_count
from public.film fl
left join public.film_category fc on fl.film_id = fc.film_id
left join public.category c on c.category_id =fc.category_id
left join public.inventory i on i.film_id =fl.film_id
left join public.rental r on r.inventory_id = i.inventory_id group by 1,2 order by 3 desc;
