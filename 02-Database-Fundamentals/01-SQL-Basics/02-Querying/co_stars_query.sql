-- YOUR CODE HERE
with actor_dets as (
select fa.actor_id, concat(a.first_name,' ',a.last_name) full_name, fa.film_id
from public.actor a
join public.film_actor fa on a.actor_id = fa.actor_id
),
actor_pairs as (
select af1.full_name actor1, af2.full_name actor2, count(af1.film_id) films_together
from actor_dets af1
join actor_dets af2 on af1.film_id = af2.film_id
where af1.actor_id < af2.actor_id
group by 1,2
)
select actor1, actor2, films_together
from actor_pairs where films_together > 3
order by films_together DESC, actor1, actor2;
