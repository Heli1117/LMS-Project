from db_connection import get_connection
#-------------Manage members-----------
#-----create
class add_member:
     def __init__(self,member_id,name,email,registered_by_librarian):
         conn = get_connection() 
         cursor = conn.cursor() 
    
         cursor.execute("USE lms")
  
         cursor.execute( 
             "INSERT INTO members(member_id,name,email,registered_by_librarian)\
             VALUES (%s, %s, %s, %s)", 
             (member_id,name,email,registered_by_librarian) 
         ) 
  
         conn.commit() 
         cursor.close() 
         conn.close() 
         print(f"member: {name}")


# ---------- READ (all) ---------- 

def get_all_members():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM members") 
    rows = cursor.fetchall()
   
    cursor.close() 
    conn.close() 
    return rows
# ---------- READ (one) ---------- 

def get_one_members():
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
    
    cursor.execute("SELECT * FROM members") 
    rows = cursor.fetchone()
   
    cursor.close() 
    conn.close() 
    return rows

# ---------- UPDATE ----------
def update_email(member_id, new_email): 
    conn = get_connection() 
    cursor = conn.cursor() 
    
    cursor.execute("USE lms")
  
    cursor.execute( 
        "UPDATE members SET email = %s WHERE id = %s", 
        (new_email, member_id) 
    ) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Updated email {member_id}'s email to {new_email}") 

# ---------- DELETE ---------- 
def delete_member(member_id): 
    conn = get_connection() 
    cursor = conn.cursor() 
  
    cursor.execute("USE lms")
    cursor.execute("DELETE FROM members WHERE id = %s", (member_id,)) 
  
    conn.commit() 
    cursor.close() 
    conn.close() 
    print(f"Deleted member {member_id}") 