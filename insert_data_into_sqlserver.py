# solution to use in aws lambda 


    server = '' 
    database = '' 
    username = '' 
    password = '' 
    con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    print(con)
    cursor = con.cursor()
    
    sql_Delete_query = f"""Delete from database  where start_time >='{hour_date_time}' """
    
    print(sql_Delete_query)
    cursor.execute(sql_Delete_query)
    con.commit()
    
    
    # creating column list for insertion
    cols = " , ".join([str(i) for i in dataset.columns.tolist()])
  
    for i,row in dataset.iterrows():
        sql = "INSERT INTO database (" +cols + ") VALUES (" + "?,"*(len(row)-1) + "?)"

        cursor.execute(sql, tuple(row))
    
        # the connection is not autocommitted by default, so we must commit to save our changes
        con.commit()
    #close the connection    
    cursor.close()
