from db_connection import get_connection
#----------------- Manage Librariens---------------

# create

class add_librarian:
     def __init__(self,librarian_id,name,username,password, created_by_admin_id ):
         conn = get_connection() 
         cursor = conn.cursor() 
    
         cursor.execute("USE lms")
  
         cursor.execute( 
             "INSERT INTO librarians(librarian_id,name,username,password, created_by_admin_id )\
             VALUES (%s, %s, %s, %s, %s)", 
             (librarian_id,name,username,password, created_by_admin_id ) 
         ) 
  
         conn.commit() 
         cursor.close() 
         conn.close() 
         print(f"Added librarian: {name}")
   
    

# ---------- READ (all) ---------- 

def get_all_librarians():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM librarians") 
    rows = cursor.fetchall()
   
    cursor.close() 
    conn.close() 
    return rows

# ---------- READ (one) ---------- 

def get_one_librarians():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM librarians") 
    rows = cursor.fetchone()
   
    cursor.close() 
    conn.close() 
    return rows

# ---------- DELETE ---------- 
def delete_librarian(librarian_id): 
    conn = get_db_connection() 
    cursor = conn.cursor() 
  
    cursor.execute("USE lms")
    cursor.execute("DELETE FROM librarians WHERE id = %s", (librarian_id,)) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Deleted librarian {librarian_id}") 

# --------------------Manage stocks------------------

