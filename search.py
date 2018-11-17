import pandas as pd
import numpy as np
import pymysql

def search(company):
    
    host = "firstdatabase.c3cfb1e7meof.us-east-2.rds.amazonaws.com"
    port = 3306
    dbname="firstdatabase"
    user="agentO07"
    password=""

    conn = pymysql.connect(host=host, 
                           user=user,
                           port=port,
                           passwd=password, 
                           db=dbname,
                           cursorclass=pymysql.cursors.DictCursor)
    
    sql = "SELECT * FROM companies WHERE name IN (\'{0}\');".format(company)
    query = pd.read_sql(sql, conn)

    country, followers, industry, price = query.loc[0,'country'], query.loc[0,'followers'], query.loc[0,'industry'], query.loc[0,'price']

    sql = ("SELECT * FROM influencers " +
       "WHERE country IN (\'{0}\') AND " + 
             "industry IN (\'{1}\') AND " + 
             "followers >= {2} AND " +
             "price <= {3};").format(country, industry, followers, price)
    result = pd.read_sql(sql, conn)
    conn.close()

    if result.empty:
        ans = 'No search results'
    else:
        result = result.sort_values('price', axis=0, ascending=True)
        values = result.iloc[0].values
        ans = np.array2string(values)
    
    return ans
