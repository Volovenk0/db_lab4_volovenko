-- 3.1 Вивести кількість продажів книг за жанром
select genre, sum(sales.approximate_sales_in_millions) as total_sales_in_millions 
	from book join sales 
		on book.num_sale_id = sales.num_sale_id
group by book.genre
order by total_sales_in_millions desc;

-- 3.2 Вивести топ 5 авторів за кількістю продажів книг
select author.author_name, sum(sales.approximate_sales_in_millions) as total_sales_in_millions 
	from author join book 
		on author.author_name = book.author_name
			join sales 
				on book.num_sale_id = sales.num_sale_id
group by author.author_name
order by total_sales_in_millions desc
limit 5;

-- 3.3 Вивести кількість продажів книг за мовою оригіналу
select book.original_language, sum(sales.approximate_sales_in_millions) as total_sales_in_millions
	from book join sales
		on book.num_sale_id = sales.num_sale_id
group by book.original_language
order by total_sales_in_millions desc; 