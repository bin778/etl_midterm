import pandas as pd
import os

import pandas as pd
from sqlalchemy import create_engine, inspect

from dotenv import load_dotenv
import os
load_dotenv()

path1 = '../dataset/'

merged_data = {
    'pressure': [],
    'rate': [],
    'sound': []
}

dir1 = os.listdir(path1)
for dt in dir1:
    if dt == '.ipynb_checkpoints': continue
    dataType = dt
    path2 = os.path.join(path1, dataType)

    if os.path.isdir(path2) and dataType in merged_data:
        for fi in os.listdir(path2):
            if fi == '.ipynb_checkpoints': continue
            filePath = os.path.join(path2, fi)
            try:
                fileData = pd.read_csv(filePath)
                merged_data[dt].append(fileData)
                print(f"Loaded: {filePath}")
            except Exception as e:
                print(f"Error loading {filePath}: {e}")

pressureData = pd.concat(merged_data['pressure'], ignore_index=True)
rateData = pd.concat(merged_data['rate'], ignore_index=True)
soundData = pd.concat(merged_data['sound'], ignore_index=True)

mysql_user = os.getenv('SQLUSER')
mysql_password = os.getenv('PW')
mysql_host = os.getenv('HOST')
mysql_port = int(os.getenv('PORT'))
mysql_database = os.getenv('DBNAME')

mysql_engine = create_engine(f'mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database}')
pressureTableName = 'fmd_trend_analysis_blood_pressure'
rateTableName = 'fmd_trend_analysis_heart_rate'
soundTableName = 'fmd_trend_analysis_heart_sound'

pressureData.to_sql(name = pressureTableName, con = mysql_engine, if_exists='replace', index=False)
rateData.to_sql(name = rateTableName, con = mysql_engine, if_exists='replace', index=False)
soundData.to_sql(name = soundTableName, con = mysql_engine, if_exists='replace', index=False)

selectSQL = """
select
	A.id,
	A.memb_id,
	A.device_desc,
	A.fullname,
	A.systolic,
	A.diastolic,
	A.hr,
	B.heart_rate,
	C.bpm,
	C.position,
	A.get_time,
	A.create_dttm
from fmd_trend_analysis_blood_pressure A
join fmd_trend_analysis_heart_rate B on A.id = B.id
join fmd_trend_analysis_heart_sound C on A.id = C.id
order by id;
"""

selectData = pd.read_sql_query(sql=selectSQL, con=mysql_engine)
selectTableName = 'fmd_heart_summary'
selectData.to_sql(name=selectTableName, con = mysql_engine, if_exists='replace', index=False)
