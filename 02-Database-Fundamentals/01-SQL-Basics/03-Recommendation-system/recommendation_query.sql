-- YOUR CODE HERE
with cte as(
select title,to_tsvector(description) vector
from film
where title = 'APOCALYPSE FLAMINGOS'
)
select film.title
from cte, film
where to_tsvector(description) @@ to_tsquery(array_to_string(tsvector_to_array(cte.vector), ' | '))
and film.title != 'APOCALYPSE FLAMINGOS'
