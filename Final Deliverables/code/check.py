import ibm_db
from dotenv import load_dotenv
import os


load_dotenv()


try:
    # conn = ibm_db.connect(os.getenv('CREDENTIALS'),'','')
    conn = ibm_db.connect(
        "DATABASE=bludb;HOSTNAME=764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=32536;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hmd83768;PWD=4WzDtnPyc6CW98X2", '', '')
except Exception as err:
     print("Exception occurs->", err)

def check_the_acc_info(user_email):
    sql = "SELECT * FROM donors WHERE user_email=?"
    stmt = ibm_db.prepare(conn,sql)
    ibm_db.bind_param(stmt,1,user_email)
    ibm_db.execute(stmt)
    donor_acc = ibm_db.fetch_assoc(stmt)

    user_sql = "SELECT * FROM users WHERE email=?"
    user_stmt = ibm_db.prepare(conn,user_sql)
    ibm_db.bind_param(user_stmt,1,user_email)
    ibm_db.execute(user_stmt)
    user_acc = ibm_db.fetch_assoc(user_stmt)

    result = ""
    if donor_acc and user_acc:
        result = 'donor-user-account'
    elif donor_acc:
        result = 'donor-account'
    elif user_acc:
        result = 'user-account'
    else:
        return False
    
    return result

