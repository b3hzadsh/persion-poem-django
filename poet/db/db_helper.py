import sqlite3
import os.path


def init_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "ganj.s3db")
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    return (con, cursor)


def dispose_db(con, cursor):
    cursor.close()
    con.close()

def get_all_poetries():
    """
    here we get all poetries from db to show in home page
    """
    (con, cursor) = init_db()
    cursor.execute("SELECT * FROM poet ;")
    rows = cursor.fetchall()
    for row in rows:
        yield row
    dispose_db(con, cursor)

def get_all_verses_of_a_poem(poem_id):
    (con, cursor) = init_db()
    cursor.execute(f"SELECT * FROM verse WHERE poem_id ={poem_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    return result


def get_poems_title(poem_id):
    (con, cursor) = init_db()
    cursor.execute(f"SELECT * FROM poem WHERE id ={poem_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    return result

def get_all_works_of_a_poet(poet_id):
    """
    get all books of one poet
    """
    (con, cursor) = init_db()
    cursor.execute(f"SELECT * FROM cat WHERE poet_id ={poet_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    return result[1:]

def get_poet_info(poet_id):
    """
    get description string of one poet
    """
    (con, cursor) = init_db()
    cursor.execute(f"SELECT description,name FROM poet WHERE id ={poet_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    # print('it is get all desc result')
    # print(result)
    return result


def get_all_titles_of_a_work(cat_id):
    (con, cursor) = init_db()
    cursor.execute(f"SELECT * FROM poem WHERE cat_id ={cat_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    return result

def get_book_name_by_cat_id(cat_id):
    """
    take an id and return the name of that book
    """
    (con, cursor) = init_db()
    cursor.execute(f"SELECT * FROM cat WHERE id ={cat_id};")
    result = cursor.fetchall()
    dispose_db(con, cursor)
    return result[0][2]


# def get_all_verses_of_a_poem(poem_id):
#     (con, cursor) = init_db()
#     cursor.execute(f"SELECT * FROM verse WHERE poem_id ={poem_id};")
#     result = cursor.fetchall()
#     dispose_db(con, cursor)
#     return result




resul = get_all_verses_of_a_poem(1199)
print(resul)
# gg = get_poems_title()
# print(next(gg))
# print(next(gg))
# Create your views here.


def get_poem():
    id = 1119
    (con, cursor) = init_db()
    while id < 1296:
        cursor.execute(f"SELECT * FROM poem WHERE id ={id};")
        id += 1
        result = cursor.fetchall()
        yield result
    dispose_db(con, cursor)
