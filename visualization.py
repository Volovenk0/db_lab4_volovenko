import psycopg2
import matplotlib.pyplot as plt

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

def plot_bar_chart(labels, values, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'lightpink', 'bisque', 'lightsteelblue', 'mediumaquamarine', 'salmon']
    ax.bar(labels, values, color=colors)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.3)
    plt.show()


def plot_pie_chart(labels, sizes, title):
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'plum']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    plt.title(title)
    plt.show()

def plot_line_chart(x, y, xlabel, ylabel, title):
    plt.plot(x, y, marker='o', color='orchid')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def main():
    connection = psycopg2.connect(
        user=db_params['user'],
        password=db_params['password'],
        dbname=db_params['database'],
        host=db_params['host'],
        port=db_params['port']
    )

    with connection.cursor() as cursor:
        # Запит 1: Візуалізація – стовпчикова діаграма
        result_1 = execute_query(cursor, query_1)
        genres = [row[0] for row in result_1]
        total_sales = [row[1] for row in result_1]
        plot_bar_chart(genres, total_sales, 'Жанр', 'Сума продаж, млн $', 'Продажі книг за жанром')

        # Запит 2: Візуалізація – кругова діаграма
        result_2 = execute_query(cursor, query_2)
        authors = [row[0] for row in result_2]
        total_sales_authors = [row[1] for row in result_2]
        plot_pie_chart(authors, total_sales_authors, 'Топ 5 авторів за кількістю проданих книг')

        # Запит 3: Візуалізація – графік залежності
        result_3 = execute_query(cursor, query_3)
        languages = [row[0] for row in result_3]
        total_sales_languages = [row[1] for row in result_3]
        plot_line_chart(languages, total_sales_languages, 'Мова оригіналу', 'Сума продаж, млн $', 'Продажі книг за мовою оригіналу')

if __name__ == '__main__':
    main()
