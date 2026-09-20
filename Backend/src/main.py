from db_connection import get_connection
conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM admins")
rows=cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("DELETE FROM librarians WHERE librarian_id='201'")

cursor.close()
conn.close() 

from admin_repository import(
    add_librarian,
    get_all_librarians,
    get_one_librarians,
    delete_librarian
    
)
# add_librarian(
#    "201","abcd","pqr","xyz","101")

from book_repository import(
    add_book,
    get_all_books,
    get_one_book,
    update_stock,
    delete_book
)
from librarion_repository import(
    add_member,
    get_all_members,
    get_one_members,
    update_email,
    delete_member
)

from transaction_repository import(
    add_transaction,
    get_all_trasactions,
    get_one_trasactions,
    update_book,
    delete_transaction
)