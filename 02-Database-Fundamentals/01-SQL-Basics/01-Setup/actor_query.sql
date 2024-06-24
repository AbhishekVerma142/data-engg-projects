-- YOUR CODE HERE
select actor_id, count(film_id) total_films from public.film_actor f group by actor_id having count(film_id) > 5  order by 2 desc;
