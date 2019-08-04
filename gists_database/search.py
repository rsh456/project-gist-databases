from .models import Gist

def search_gists(db_connection, **kwargs):
    cursor = None
    #if not '**kwargs' in locals():
        
    if 'github_id' in kwargs:
        params = [kwargs.get('github_id')]
        query="SELECT * FROM gists WHERE github_id LIKE ?"
        cursor=db_connection.execute(query,params)
    elif 'created_at' in kwargs:
        params = [kwargs.get('created_at')]
        cursor = db_connection.execute("SELECT * FROM gists WHERE datetime(created_at) == datetime(:created_at)", params)
    else:
        query="SELECT * FROM gists"
        cursor = db_connection.execute(query)
    t_gist = cursor.fetchall()
    v_lis =[]
    n=0
    for row in t_gist:
        v_gist=Gist(t_gist[n])    
        v_lis.append(v_gist)
        m=n+1
    return v_lis
