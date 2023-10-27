config = {
    'user': '',
    'password': '',
    'host': '',
    'database': '',
    'ssl_ca': '',
}

db_uri = f'''mysql+mysqlconnector://{config['user']}:{config['password']}@
{config['host']}/{config['database']}?ssl_ca={config['ssl_ca']}'''
