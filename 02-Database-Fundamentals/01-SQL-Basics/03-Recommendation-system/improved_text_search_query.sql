--- YOUR CODE HERE
select title, ts_rank_cd(to_tsvector(description), to_tsquery('Cat & Dog')) AS rank
from film
where to_tsvector(description) @@ to_tsquery('Cat & Dog')
order by rank desc;
