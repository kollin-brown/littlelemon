dbconfig = {"database": "little_lemon_db", "user": "root", "password": ""}
try:
  con_pool = MySQLConnectionPool(pool_name="pool_b", pool_size=2, **dbconfig)
  print(f"Connection pool is created with name {con_pool.pool_name}")
  print(f"The pool size is {con_pool.pool_size}")
except errors.Error as e:
  print(e.errno, e)
