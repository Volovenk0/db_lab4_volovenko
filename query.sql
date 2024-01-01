-- 3.1 Вивести жанри книг за спаданням їх рейтингу
select max(book.rating) as max_rating, genre.genre_name 
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
group by genre.genre_name
order by max_rating desc;

-- 3.2 Вивести топ 5 авторів за рейтингом книг
select author.author_name, max(book.rating) as max_rating
	from author join book_author
		on author.author_id = book_author.author_id
			join book
				on book_author.book_id = book.book_id
group by author.author_name
order by max_rating desc
limit 5;

-- 3.3 Вивести жанри, назву та ціну книг з рейтингом більше 4.5
select book.book_name, genre.genre_name, book.price, book.rating 
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
where book.rating > 4.5;
