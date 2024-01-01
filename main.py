import psycopg2
from tabulate import tabulate

db_params = {
    'host': 'localhost',
    'database': 'db_lab3',
    'user': 'postgres',
    'password': 'postgres',
    'port': '5432'
}

query_1 = '''
select max(book.rating) as max_rating, genre.genre_name 
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
group by genre.genre_name
order by max_rating desc;
'''

query_2 = '''
select author.author_name, max(book.rating) as max_rating
	from author join book_author
		on author.author_id = book_author.author_id
			join book
				on book_author.book_id = book.book_id
group by author.author_name
order by max_rating desc
limit 5;
'''

query_3 = '''
select genre.genre_name, count(book.book_id) as book_count
	from book join book_genre
		on book.book_id = book_genre.book_id
			join genre
				on book_genre.genre_id = genre.genre_id
where book.price < 12
group by genre.genre_name
order by book_count desc;
'''

def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def print_query_results(query, result, cursor):
    print(f"\nQuery: {query}\n")
    headers = [desc[0] for desc in cursor.description]
    print(tabulate(result, headers, tablefmt="pretty"))

def main():
    connection = psycopg2.connect(
        user=db_params['user'],
        password=db_params['password'],
        dbname=db_params['database'],
        host=db_params['host'],
        port=db_params['port']
    )

    with connection.cursor() as cursor:
        result_1 = execute_query(cursor, query_1)
        print_query_results(query_1, result_1, cursor)

        result_2 = execute_query(cursor, query_2)
        print_query_results(query_2, result_2, cursor)

        result_3 = execute_query(cursor, query_3)
        print_query_results(query_3, result_3, cursor)

if __name__ == '__main__':
    main()
