import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
import pandas as pd
import re
from pyspark import SparkContext
from pyspark.conf import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import Row
import os
from pyspark.sql.functions import date_format
from pyspark.sql import functions as F
import datetime
from pyspark.sql.types import StringType
from pyspark.sql.functions import *
from pyspark.sql.types import *
import json
import boto3
import pandas as pd
from io import StringIO
import botocore.exceptions
from botocore.exceptions import ClientError
import threading
import concurrent.futures
import time

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
sc.setCheckpointDir("s3://gotskillsdev-bucket-satish-001/sparkCheckPointDirectory/")


class GotskillTest:

    def __init_(self):
        pass

    def isfile_s3(self, bucket, key) -> bool:
        s3_client = boto3.client("s3")
        result = s3_client.list_objects_v2(Bucket=bucket, Prefix=f'{key}/')

        if 'Contents' in result:
            return 0
        else:
            return 1
        return

    def get_secret(self):

        secret_name = "sec-gotskills-rds-mysql-gotskills-instance-dev-03"
        region_name = "us-east-1"

        # Create a Secrets Manager client
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                raise e
        else:
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                return secret
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                return secret
        return

    def equivalent_type(self, f):
        if f == 'datetime64[ns]':
            return TimestampType()
        elif f == 'int64':
            return LongType()
        elif f == 'int32':
            return IntegerType()
        elif f == 'float64':
            return DoubleType()
        elif f == 'float32':
            return FloatType()
        else:
            return StringType()

    def define_structure(self, string, format_type):
        try:
            typo = self.equivalent_type(format_type)
        except:
            typo = StringType()
        return StructField(string, typo)

    # Given pandas dataframe, it will return a spark's dataframe.
    def pandas_to_spark(self, pandas_df, spark):
        columns = list(pandas_df.columns)
        types = list(pandas_df.dtypes)
        struct_list = []
        for column, typo in zip(columns, types):
            struct_list.append(self.define_structure(column, typo))
        p_schema = StructType(struct_list)
        return spark.createDataFrame(pandas_df, p_schema)

    def get_InduReportal(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')
        InduReportal = spark.sql(
            "select Response ,InduvarNum,Section from ( select respid as Response,substr(variable,instr(variable,'_')+1) as InduvarNum,case when variable like '%InduReportal%' then Value end as Section from SourceTab where variable like '%InduReportal%' and Value is not null) innr where Section is not null")

        return InduReportal

    def get_CatgReportal(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')
        CatgReportal = spark.sql(
            "select Response,CatvarNum, Category from (select respid as Response,substr(variable,instr(variable,'_')+1) as CatvarNum, case when variable like '%CatHeadReportal%' then Value end as Category from SourceTab where variable like '%CatHeadReportal%' and  Value is not null) innr where Category is not null")
        return CatgReportal

    def get_GridReportalInfo(self, spark, pDF):

        pDF.createOrReplaceTempView('SourceTab')
        GridReportalInfo = spark.sql(
            "select * from (select Response,varNum,case when Section like '%<%' then substr(Section,0,instr(Section,'<span')-1) else  Section end as skill,case when Section like '%<%' then substr(Section,instr(Section,'>')+1,instr(Section,'</span')- instr(Section,'>')-1) else '' end as Sub_Category from (select respid as Response,variable as variable, substr(variable,9,instr(variable,'GridReportal_')-9) as varNum, case when variable like '%Skillset%GridReportal%' then Value end as Section from SourceTab where variable like '%Skillset%GridReportal%' and Value is not null)innr)a where Skill  is not null")
        # GridReportalInfo=spark.sql("select respid as Response,variable as variable, substr(variable,9,instr(variable,'GridReportal_')-9) as varNum, case when variable like '%Skillset%GridReportal%' then Value end as Section from SourceTab where variable like '%Skillset%GridReportal%'")
        # GridReportalInfo=spark.sql("select respid as Response,variable as variable,Value  from SourceTab where variable like '%Skillset%GridReportal%' and value is not null")
        return GridReportalInfo

    def get_SkillSet1Grid(self, spark, pDF):

        pDF.createOrReplaceTempView('SourceTab')
        SkillSet1Grid = spark.sql(
            "select Response,SkillsetGridVarNum,cast(`Proficiency level` as integer) as `Proficiency level` from (SELECT respid as Response,variable,instr(variable,'_')+1 as pos,substr(variable,instr(variable,'_')+1) as SkillsetGridVarNum,case when variable like '%Skillset%Grid_%' then  value end as `Proficiency level` FROM SourceTab where variable like '%Skillset%Grid_%' and value is not null and   variable Not like '%Skillset%GridReportal%' and value <> 'NaN') innr where `Proficiency level` is not null")

        return SkillSet1Grid

    def get_qSkillsetHIddenInfo(self, spark, pDF):

        SkillSet1Grid = spark.sql(
            "select num,variable,Response,SkillsetGridVarNum,cast(`Proficiency level` as integer) as `Proficiency level` from (SELECT regexp_extract(variable,'[0-9]+',0) as num, respid as Response,variable,instr(variable,'_')+1 as pos,substr(variable,instr(variable,'_')+1) as SkillsetGridVarNum,case when variable like '%Skillset%Grid_%' then  value end as `Proficiency level` FROM SourceTab where variable like '%Skillset%Grid_%' and value is not null and   variable Not like '%Skillset%GridReportal%' and value <> 'NaN') innr where `Proficiency level` is not null")
        qSkillsetHIddenInfo = spark.sql(
            "select distinct Response,variable,Num ,QskillVarNum, skill_active_flag from (select respid as Response,variable,regexp_extract(variable,'[0-9]+',0)as Num,substr(variable,instr(variable,'_')+1) as QskillVarNum,case when variable like '%qSkillset%Hidden%' then Value end as skill_active_flag from SourceTab where Value is not null and variable like '%qSkillset%Hidden%' and Value <> 'NaN' ) innr where skill_active_flag is not null")
        SkillSet1Grid.createOrReplaceTempView('SkSetGrid')
        qSkillsetHIddenInfo.createOrReplaceTempView('HInfo')
        HiddenInfo = spark.sql(
            "select distinct h.skill_active_flag, sk.Response from SkSetGrid sk inner join HInfo h on sk.Response=h.Response and sk.num=h.num and sk.SkillsetGridVarNum=h.QskillVarNum")
        return HiddenInfo

    def get_Qfmo(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')
        QFMN = spark.sql(
            "select Response , qFMNO from (select respid as Response,case when variable like '%qFMNO%' then Value end as qFMNO from SourceTab) innr where qFMNO is not null")

        return QFMN

    def get_Timestamp(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')
        TimestampDF = spark.sql(
            "select Response,Timestamp from (select respid as Response,case when variable like '%StartTimeAlt_2%' then Value end as Timestamp from SourceTab) innr where Timestamp is not null")

        return TimestampDF

    def get_Guild(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')
        GuildDF = spark.sql(
            "select Response , Guild from (select respid as Response,case when variable like '%qguild%' then Value end as Guild from SourceTab) innr where Guild is not null")

        return GuildDF

    def get_qSingleRepoPortal(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')

        qSingleRepo = spark.sql(
            "SELECT variable,regexp_extract(variable,'[0-9]+',0) as num,value, respid as Response FROM SourceTab where variable like '%qSingleReportal_%' and value is not null  and value <> 'NaN'")
        return qSingleRepo

    def get_qSingleResponse(self, spark, pDF):
        pDF.createOrReplaceTempView('SourceTab')

        qSingleRepo = spark.sql(
            "SELECT variable,regexp_extract(variable,'[0-9]+',0) as num,value, respid as Response FROM SourceTab where variable like '%qSingleReportal_%' and value is not null  and value <> 'NaN'")
        qSingleResponse = spark.sql(
            "select variable,regexp_extract(variable,'[0-9]+',0) as num,value, respid as Response FROM SourceTab where variable like '%qSingleResponse_%' and value is not null  and value <> 'NaN'")

        qSingleRepo.createOrReplaceTempView('qSingleInfo')
        qSingleResponse.createOrReplaceTempView('qSingleResponse')

        qSingleResponseDF = spark.sql(
            "select rs.Response,rs.value from qSingleResponse rs inner join qSingleInfo qi on rs.Response=qi.Response and rs.num=qi.num ")
        return qSingleResponseDF

    def chageExtn(self, bucket, outputfolder, key):
        try:
            s3.Object(bucket, f"{outputfolder}/{newfile}.csv").copy_from(CopySource=f'{bucket}/{key}')
            return 0
        except botocore.exceptions.ClientError as e:
            print(e.response['Error']['Code'])
            return 1
        return

    def tableCheckInDB(self, url, userName, password):
        connection_mysql = {
            "url": url,
            "dbtable": "information_schema.columns",
            "user": userName,
            "password": password

        }
        tableDF = glueContext.create_dynamic_frame.from_options(connection_type="mysql",
                                                                connection_options=connection_mysql)

        tableMetaDataDF = tableDF.toDF()
        return tableMetaDataDF

    def WriteToTable(self, DF, tableName, url, username, password):
        print(type(DF))
        DynamicDF = DynamicFrame.fromDF(DF, glueContext, "openresult")
        connection_mysql_options = {
            "url": url,
            "dbtable": tableName,
            "user": username,
            "password": password}

        Output = glueContext.write_from_options(frame_or_dfc=DynamicDF, connection_type="mysql",
                                                connection_options=connection_mysql_options,
                                                transformation_ctx="Output")

    def dropTable(self, spark, tableName, openfileName):
        spark.catalog.dropTempView(f"{openfileName}_InduRepo")
        spark.catalog.dropTempView(f"{openfileName}_CatgRepo")
        spark.catalog.dropTempView(f"{openfileName}_GridRepo")
        spark.catalog.dropTempView(f"{openfileName}_sk1Grid")
        spark.catalog.dropTempView(f"{openfileName}_QSkillsetHddn")
        spark.catalog.dropTempView(f"{openfileName}_QfmoTemp")
        spark.catalog.dropTempView(f"{openfileName}_TempTimestamp")
        spark.catalog.dropTempView(f"{openfileName}_TempQGuild")
        spark.catalog.dropTempView(f"{openfileName}_qSingleRepo")
        spark.catalog.dropTempView(f"{openfileName}_qSingleResponse")
        spark.catalog.dropTempView(f"{openfileName}_orgnl")
        spark.catalog.dropTempView(f"{openfileName}_SurveyOpenOldData")
        spark.catalog.dropTempView(f"{openfileName}_SurveyOpenNewdata")
        spark.catalog.dropTempView(f"{openfileName}_oldSurveyOpenDF")
        spark.catalog.dropTempView(f"{surveyFileName}_SurveyResultOldData")
        spark.catalog.dropTempView(f"{surveyFileName}_SurveyResultNewData")

    def main(self, fileName, Tab1, Tab2, bucname, oldFilePrefix, spark, glueContext, url, username, password):
        openfileName = Tab1
        surveyFileName = Tab2
        FileName = fileName
        text = spark.read.format('csv').options(header='true', inferSchema='true').load(FileName)
        pDF = text.toPandas().dropna(axis=1, how='all')
        p = pDF.melt(id_vars=['responseid', 'respid'])
        OrgDF = self.pandas_to_spark(p, spark)
        InduReportalDF = self.get_InduReportal(spark, OrgDF)
        InduReportalDF.createOrReplaceTempView(f"{openfileName}_InduRepo")

        CatgReportalDF = self.get_CatgReportal(spark, OrgDF)
        CatgReportalDF.createOrReplaceTempView(f"{openfileName}_CatgRepo")

        GridReportalInfoDF = self.get_GridReportalInfo(spark, OrgDF)
        GridReportalInfoDF.createOrReplaceTempView(f"{openfileName}_GridRepo")

        SkillSet1GridDF = self.get_SkillSet1Grid(spark, OrgDF)
        SkillSet1GridDF.createOrReplaceTempView(f"{openfileName}_sk1Grid")

        qSkillsetHIddenDF = self.get_qSkillsetHIddenInfo(spark, OrgDF)
        qSkillsetHIddenDF.createOrReplaceTempView(f"{openfileName}_QSkillsetHddn")

        QfmoDF = self.get_Qfmo(spark, OrgDF)
        QfmoDF.createOrReplaceTempView(f"{openfileName}_QfmoTemp")

        TempTimestampDF = self.get_Timestamp(spark, OrgDF)
        TempTimestampDF.createOrReplaceTempView(f"{openfileName}_TempTimestamp")

        get_GuildDF = self.get_Guild(spark, OrgDF)
        get_GuildDF.createOrReplaceTempView(f"{openfileName}_TempQGuild")

        qSingleRepo = self.get_qSingleRepoPortal(spark, OrgDF)
        qSingleRepo.createOrReplaceTempView(f"{openfileName}_qSingleRepo")

        qSingleRepo1 = self.get_qSingleResponse(spark, OrgDF)
        qSingleRepo1.createOrReplaceTempView(f"{openfileName}_qSingleResponse")

        Orgdf = spark.sql(
            f"SELECT distinct innr.Response,innr.Timestamp, 'Self Reported' as Source,innr.Guild,innr.QFMNO,innr.Section,innr.Category,innr.Sub_Category,innr.skill,innr.`Proficiency level`, case when `Proficiency level` = 1 then 'None' when `Proficiency level` = 2 then 'Beginner' when `Proficiency level` = 3 then 'Intermediate' when  `Proficiency level` = 4 then 'Advanced' end as `Proficiency level_Desc`,'Y' as most_recent_flag,'Guild Defined' as survey_question_type from ( SELECT c.Response,t.Timestamp,'Self Reported' as source,g.Guild,qFMNO,i.Section,c.Category,sk.Sub_Category,sk.skill,sg.`Proficiency level` FROM {openfileName}_CatgRepo c inner join {openfileName}_InduRepo i on c.Response=i.Response and c.CatvarNum=i.InduvarNum inner join {openfileName}_GridRepo sk on i.Response=sk.Response and c.CatvarNum=sk.varNum and c.Response=sk.Response and i.InduvarNum=sk.varNum inner join {openfileName}_sk1Grid sg on c.Response=sg.Response inner join {openfileName}_QfmoTemp q on c.Response=q.Response inner join {openfileName}_TempTimestamp t on c.Response=t.Response inner join {openfileName}_TempQGuild g on  c.Response=g.Response order by Section)innr")

        Orgdf.createOrReplaceTempView(f"{openfileName}_orgnl")

        SurveyOpenExist = self.isfile_s3(bucname, f'{oldFilePrefix}/{openfileName}')
        SurveyResultExist = self.isfile_s3(bucname, f'{oldFilePrefix}/{surveyFileName}')

        if SurveyOpenExist == 0 and SurveyResultExist == 0:

            #################For Survey Open##############################
            SurveyOpenOld = spark.read.format('csv').options(header='true', inferSchema='true').load(
                f's3://{bucname}/{oldFilePrefix}/{openfileName}')
            SurveyOpenOld.createOrReplaceTempView(f"{openfileName}_SurveyOpenOldData")
            surveyOpenDF = spark.sql(
                f"select distinct  innr.Response as response_id,innr.Timestamp as timestamp,innr.Guild as guild,innr.QFMNO as fmno,qrep.value as open_question_text, qi.value as response from {openfileName}_orgnl innr inner join  {openfileName}_qSingleRepo qrep on innr.Response=qrep.Response inner join {openfileName}_qSingleResponse qi on qrep.Response=qi.Response").coalesce(
                1)
            surveyOpenDF.createOrReplaceTempView(f"{openfileName}_SurveyOpenNewdata")
            surveyOpenNewDF = spark.sql(
                f"select response_id, fmno from {openfileName}_SurveyOpenNewdata nw where not EXISTS (select 1 from {openfileName}_SurveyOpenOldData od where od.response_id=nw.response_id)")

            self.WriteToTable(surveyOpenNewDF, openfileName, url, username, password)
            surveyOpenNewDF.createOrReplaceTempView(f"{openfileName}_oldSurveyOpenDF")
            spark.sql(f"select distinct  response_id from {openfileName}_oldSurveyOpenDF").coalesce(1).write.option(
                "header", "true").mode("append").csv(f"s3://{bucname}/{oldFilePrefix}/{openfileName}")

            #################For Survey Result##############################
            SurveyResultOld = spark.read.format('csv').options(header='true', inferSchema='true').load(
                f's3://{bucname}/{oldFilePrefix}/{surveyFileName}')
            print('old', SurveyResultOld.printSchema())
            SurveyResultOld.createOrReplaceTempView(f"{surveyFileName}_SurveyResultOldData")
            surveyResultsDF = spark.sql(
                f"select distinct innr.Response as response_id,innr.Timestamp as timestamp,innr.Guild as guild,innr.QFMNO as fmno,innr.Section as Section,innr.Category as Category,innr.Sub_Category as Sub_Category,innr.skill as Skill,innr.`Proficiency level` as proficiency_level, `Proficiency level_Desc` as proficiency_level_desc,skill_active_flag as skill_active_flag,most_recent_flag as most_recent_flag,survey_question_type as survey_question_type from {openfileName}_orgnl innr inner join {openfileName}_QSkillsetHddn h on innr.Response=h.Response").coalesce(
                1)

            print('new', surveyResultsDF.printSchema())
            surveyResultsDF.createOrReplaceTempView(f"{surveyFileName}_SurveyResultNewData")

            surveyResultsNewDF = spark.sql(
                f"select response_id, fmno from {surveyFileName}_SurveyResultNewData nw where not EXISTS (select 1 from {surveyFileName}_SurveyResultOldData od where od.response_id=nw.response_id)")

            surveyResultsNewDF.show()
            self.WriteToTable(surveyResultsNewDF, surveyFileName, url, username, password)

            ######Writing Current Result to Old directory ###########
            surveyResultsNewDF.createOrReplaceTempView(f"{surveyFileName}_oldSurveyResultsDF")
            spark.sql(f"select distinct  response_id from {surveyFileName}_oldSurveyResultsDF").coalesce(
                1).write.option("header", "true").mode("append").csv(f"s3://{bucname}/{oldFilePrefix}/{surveyFileName}")




        else:
            print('false')
            surveyResultsDF = spark.sql(
                f"select response_id, fmno from (select distinct innr.Response as response_id,innr.Timestamp as timestamp,innr.Guild as guild,innr.QFMNO as fmno,innr.Section as Section,innr.Category as Category,innr.Sub_Category as Sub_Category,innr.skill as Skill,innr.`Proficiency level` as proficiency_level, `Proficiency level_Desc` as proficiency_level_desc,skill_active_flag as skill_active_flag,most_recent_flag as most_recent_flag,survey_question_type as survey_question_type from {openfileName}_orgnl innr inner join {openfileName}_QSkillsetHddn h on innr.Response=h.Response) A").coalesce(
                1)
            surveyResultsDF.createOrReplaceTempView(f"{surveyFileName}_SurveyResultNewData")

            surveyOpenDF = spark.sql(
                f"select response_id, fmno from (select distinct  innr.Response as response_id,innr.Timestamp as timestamp,innr.Guild as guild,innr.QFMNO as fmno,qrep.value as open_question_text, qi.value as response from {openfileName}_orgnl innr inner join  {openfileName}_qSingleRepo qrep on innr.Response=qrep.Response inner join {openfileName}_qSingleResponse qi on qrep.Response=qi.Response) B").coalesce(
                1)
            surveyOpenDF.createOrReplaceTempView(f"{openfileName}_SurveyOpenNewdata")

            self.WriteToTable(surveyResultsDF, surveyFileName, url, username, password)
            self.WriteToTable(surveyOpenDF, openfileName, url, username, password)

            spark.sql(f"select distinct  response_id from {surveyFileName}_SurveyResultNewData").coalesce(
                1).write.option("header", "true").mode("append").csv(f"s3://{bucname}/{oldFilePrefix}/{surveyFileName}")
            spark.sql(f"select distinct  response_id from {openfileName}_SurveyOpenNewdata").coalesce(1).write.option(
                "header", "true").mode("append").csv(f"s3://{bucname}/{oldFilePrefix}/{openfileName}")

            spark.catalog.dropTempView(f"{surveyFileName}_SurveyResultNewData")
            spark.catalog.dropTempView(f"{openfileName}_SurveyOpenNewdata")


## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3 = boto3.resource('s3')
s3_client = boto3.client("s3")
dictTableList = {}
chkTable = {}
obj = GotskillTest()
bucname = 'gotskillsdev-bucket-satish-001'
prefix = 'gotskillssuryveydatatxtfiles/GotSkills_'
oldFilePrefix = 'gotskillsoldfiles'
writeLocPrefix = 'gotskillssuryveydatanew'
my_bucket = s3.Bucket(bucname)

#### convert the file to csv to s3 location
for object_summary in my_bucket.objects.filter(Prefix=prefix):
    print('object_summary', object_summary)
    if object_summary.key != f'{prefix}/':
        fl = object_summary.key[0:object_summary.key.rfind('.')]
        newfile = fl[fl.rfind('/') + 1:]
        print('new', object_summary.key)
        obj.chageExtn(bucname, writeLocPrefix, object_summary.key)

for object_summary in my_bucket.objects.filter(Prefix=writeLocPrefix):
    if object_summary.key != f'{writeLocPrefix}/':
        filename = object_summary.key
        print('ac', filename)
        ofileName = filename[filename.rfind('/') + 1:]
        print('ofile', ofileName)
        actualFileName = ofileName[ofileName.rfind('/') + 1:]
        # removePrefix=actualFileName[actualFileName.rfind('_'):]
        FileNameWithoutExtention = ofileName[0:ofileName.rfind('.')]
        openfileName = FileNameWithoutExtention[FileNameWithoutExtention.find('_') + 1:] + '_SurveyOpen'
        surveyFileName = FileNameWithoutExtention[FileNameWithoutExtention.find('_') + 1:] + '_SurveyResults'
        print(actualFileName, openfileName, surveyFileName)
        dictTableList[f's3://{bucname}/{filename}'] = [openfileName, surveyFileName]

# obj.main()
print('dict', dictTableList)

# secret=json.loads(obj.get_secret())
url = "jdbc:mysql://database-1.cpqwxlesrczu.us-east-1.rds.amazonaws.com:3306/mydatabase"
userName = "admin"
password = "satishpassword#123"
schemaName = "mydatabase"

df = obj.tableCheckInDB(url, userName, password)
print(df.take(1))
df.createOrReplaceTempView("tableMetadata")
for i in dictTableList.items():
    if i[1] != list() and len(i[1]) == 2:
        print(len(i[1]))
        print(i[1][0], i[1][1])
        OpenResultTable = i[1][0]
        SurveyResultTable = i[1][1]
        print('tab', OpenResultTable)
        print('rslt', SurveyResultTable)
        TableExistDF = spark.sql(
            f"select distinct count(distinct table_name) as isTable from tableMetadata where table_name in ('{OpenResultTable}','{SurveyResultTable}') and table_schema='{schemaName}'")
        TableExistDF.show()
        cnt = TableExistDF.rdd.map(lambda x: x[0]).collect()
        if cnt[0] == 2:
            print(cnt, cnt)
            chkTable[i[0]] = [OpenResultTable, SurveyResultTable]
print("###RESULT##########################")
print('ITems', chkTable)
# for item in chkTable.items():
#    print(item[0],item[1][0],item[1][1])
#    obj.main(item[0],item[1][0],item[1][1],bucname,oldFilePrefix,spark,glueContext,url,userName,password)
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = [executor.submit(obj.main(), item[0], item[1][0], item[1][1], bucname, oldFilePrefix, spark, glueContext, url, userName, password) for item in chkTable.items()]
    spark.stop()
    job.commit()
