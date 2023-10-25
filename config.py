config = {
    'user': 'marlonoloo',
    'password': 'm4r10n!#',
    'host': 'fpl.mysql.database.azure.com',
    'database': 'fpl',
    'ssl_ca': 'app/credentials/DigiCertGlobalRootCA.crt.pem',
}

db_uri = f'''mysql+mysqlconnector://{config['user']}:{config['password']}@
{config['host']}/{config['database']}?ssl_ca={config['ssl_ca']}'''
