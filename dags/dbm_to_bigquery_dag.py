###########################################################################
#
#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################
#
#  This code generated (see starthinker/scripts for possible source):
#    - Command: "python starthinker_ui/manage.py airflow"
#
###########################################################################

'''
--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer ( recommended ):

    From Release: pip install starthinker
    From Open Source: pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory ( if pushing local code changes ):

    source install/deploy.sh
    4) Composer Menu
    l) Install All

--------------------------------------------------------------

  If any recipe task has "auth" set to "user" add user credentials:

    1. Ensure an RECIPE['setup']['auth']['user'] = [User Credentials JSON]

  OR

    1. Visit Airflow UI > Admin > Connections.
    2. Add an Entry called "starthinker_user", fill in the following fields. Last step paste JSON from authentication.
      - Conn Type: Google Cloud Platform
      - Project: Get from https://github.com/google/starthinker/blob/master/tutorials/cloud_project.md
      - Keyfile JSON: Get from: https://github.com/google/starthinker/blob/master/tutorials/deploy_commandline.md#optional-setup-user-credentials

--------------------------------------------------------------

  If any recipe task has "auth" set to "service" add service credentials:

    1. Ensure an RECIPE['setup']['auth']['service'] = [Service Credentials JSON]

  OR

    1. Visit Airflow UI > Admin > Connections.
    2. Add an Entry called "starthinker_service", fill in the following fields. Last step paste JSON from authentication.
      - Conn Type: Google Cloud Platform
      - Project: Get from https://github.com/google/starthinker/blob/master/tutorials/cloud_project.md
      - Keyfile JSON: Get from: https://github.com/google/starthinker/blob/master/tutorials/cloud_service.md

--------------------------------------------------------------

DV360 Report To BigQuery

Move existing DV360 reports into a BigQuery table.



  - Specify either report name or report id to move a report.
  - A schema is recommended, if not provided it will be guessed.
  - The most recent valid file will be moved to the table.



--------------------------------------------------------------

This StarThinker DAG can be extended with any additional tasks from the following sources:
  - https://google.github.io/starthinker/
  - https://github.com/google/starthinker/tree/master/dags

'''

from starthinker.airflow.factory import DAG_Factory

INPUTS = {
  'auth_read':'user',  # Credentials used for reading data.
  'auth_write':'service',  # Authorization used for writing data.
  'dbm_report_id':'',  # DV360 report ID given in UI, not needed if name used.
  'dbm_report_name':'',  # Name of report, not needed if ID used.
  'dbm_dataset':'',  # Existing BigQuery dataset.
  'dbm_table':'',  # Table to create from this report.
  'dbm_schema':'',  # Schema provided in JSON list format or empty value to auto detect.
  'is_incremental_load':False,  # Clear data in destination table during this report's time period, then append report data to destination table.
}

RECIPE = {
  'tasks':[
    {
      'dbm':{
        'auth':{'field':{'name':'auth_read','kind':'authentication','order':0,'default':'user','description':'Credentials used for reading data.'}},
        'report':{
          'report_id':{'field':{'name':'dbm_report_id','kind':'integer','order':2,'default':'','description':'DV360 report ID given in UI, not needed if name used.'}},
          'name':{'field':{'name':'dbm_report_name','kind':'string','order':3,'default':'','description':'Name of report, not needed if ID used.'}}
        },
        'out':{
          'bigquery':{
            'auth':{'field':{'name':'auth_write','kind':'authentication','order':1,'default':'service','description':'Authorization used for writing data.'}},
            'dataset':{'field':{'name':'dbm_dataset','kind':'string','order':4,'default':'','description':'Existing BigQuery dataset.'}},
            'table':{'field':{'name':'dbm_table','kind':'string','order':5,'default':'','description':'Table to create from this report.'}},
            'schema':{'field':{'name':'dbm_schema','kind':'json','order':6,'description':'Schema provided in JSON list format or empty value to auto detect.'}},
            'header':True,
            'is_incremental_load':{'field':{'name':'is_incremental_load','kind':'boolean','order':7,'default':False,'description':"Clear data in destination table during this report's time period, then append report data to destination table."}}
          }
        }
      }
    }
  ]
}

dag_maker = DAG_Factory('dbm_to_bigquery', RECIPE, INPUTS)
dag = dag_maker.generate()

if __name__ == "__main__":
  dag_maker.print_commandline()
