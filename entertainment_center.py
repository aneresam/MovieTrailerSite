import movie,fresh_tomatoes

matian = movie.Movie('The Martian','A man was left on the Martian', 'http://t2.gstatic.com/images?q=tbn:ANd9GcTkKPZ7EIOafEsemyn6zTIDeGYthKC_Okgxi1eX6diuOT3xKWXQ','https://www.youtube.com/watch?v=ej3ioOneTy8')
bourne_identity = movie.Movie('Bourne Identity','A man who cannot remember his past','http://www.gstatic.com/tv/thumb/movieposters/28900/p28900_p_v7_aa.jpg','https://www.youtube.com/watch?v=FpKaB5dvQ4g')
bourne_supremacy = movie.Movie('Bourne Supremacy', 'This man\'s wife got killed','http://www.gstatic.com/tv/thumb/dvdboxart/34579/p34579_d_v7_aa.jpg','https://www.youtube.com/watch?v=Y-HqyyfBbSo')
bourne_ultimatum = movie.Movie('Bourne Ultimatum', 'The third story', 'http://www.gstatic.com/tv/thumb/dvdboxart/166270/p166270_d_v7_aa.jpg', 'https://www.youtube.com/watch?v=ZT2ZxjUjSo0')

# Create a list to store the movies
matt_damon_list = [matian,bourne_identity,bourne_supremacy,bourne_ultimatum]

# Create page to show the list of movies.
fresh_tomatoes.open_movies_page(matt_damon_list)
