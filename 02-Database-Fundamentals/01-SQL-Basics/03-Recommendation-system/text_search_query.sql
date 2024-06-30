-- YOUR CODE HERE
select title, ts_rank(to_tsvector(description), to_tsquery('Cat')) as rank
from film
where to_tsvector(description) @@ to_tsquery('Cat')
order by rank desc;
