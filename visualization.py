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

def plot_bar_chart(ax, labels, values, xlabel, ylabel, title):
    colors = ['skyblue', 'lightcoral', 'lightgreen', 'plum', 'lightpink', 'bisque', 'lightsteelblue', 'mediumaquamarine', 'salmon']
    ax.bar(labels, values, color=colors)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha='right')

def plot_pie_chart(ax, labels, sizes, title):
    colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'plum']
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors)
    ax.set_title(title)

def plot_line_chart(ax, x, y, xlabel, ylabel, title):
    ax.plot(x, y, marker='o', color='orchid')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(range(len(x)))
    ax.set_xticklabels(x, rotation=45, ha='right')

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
        genres = [row[1] for row in result_1]
        ratings = [row[0] for row in result_1]

        # Запит 2: Візуалізація – кругова діаграма
        result_2 = execute_query(cursor, query_2)
        authors = [row[0] for row in result_2]
        ratings_authors = [row[1] for row in result_2]

        # Запит 3: Візуалізація – графік залежності
        result_3 = execute_query(cursor, query_3)
        genres_prices = [row[0] for row in result_3]
        book_counts = [row[1] for row in result_3]

        fig, axs = plt.subplots(1, 3, figsize=(15, 5))

        plot_bar_chart(axs[0], genres, ratings, 'Genre', 'Rating', 'Book Ratings by Genre')
        plot_pie_chart(axs[1], authors, ratings_authors, 'Top 5 Authors by Book Rating')
        plot_line_chart(axs[2], genres_prices, book_counts, 'Genre', 'Book Count', 'Book Counts by Genre (Price < $12)')

        plt.subplots_adjust(wspace=0.5)
        plt.show()

if __name__ == '__main__':
    main()
