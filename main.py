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
select genre, sum(sales.approximate_sales_in_millions) as total_sales_in_millions 
	from book join sales 
		on book.num_sale_id = sales.num_sale_id
    group by book.genre
    order by total_sales_in_millions desc;
'''

query_2 = '''
select author.author_name, sum(sales.approximate_sales_in_millions) as total_sales_in_millions 
	from author join book 
		on author.author_name = book.author_name
			join sales 
				on book.num_sale_id = sales.num_sale_id
group by author.author_name
order by total_sales_in_millions desc
limit 5;
'''

query_3 = '''
select book.original_language, sum(sales.approximate_sales_in_millions) as total_sales_in_millions
	from book join sales
		on book.num_sale_id = sales.num_sale_id
group by book.original_language
order by total_sales_in_millions desc; 
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