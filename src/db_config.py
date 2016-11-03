DATABASE = "db_name"
ROLE = "db_user"
PASSWORD = "db_password"

TABLE = "table_name"
COLS = ["col1", "col2"]
QUERY = "SELECT {cols} FROM {table}".format(cols=", ".join(COLS), table=TABLE)

