import os

import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

from carParser import status
from carParser import creds


def get_service_sacc():
    """
    Giving acces to service account
    carparser@level-poetry-362418.iam.gserviceaccount.com
    :return:
    """
    creds_json = os.path.dirname(__file__) + "/creds/sacc1.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


service = get_service_sacc()

# https://docs.google.com/spreadsheets/d/<xxx>/edit#gid=0
sheet_id = "12YBjeGwLfgNgmUDDOPJNybSG55Iu8BSCJZwXco7TZQs"


# reading table and changing local data
def change_data():
    sheet = service.spreadsheets()
    # reading some part of table, list 'carParser', block 'G2:I100' or your block of sheet
    resp = sheet.values().get(spreadsheetId=sheet_id, range="carParser!G2:I100").execute()
    # changing data in lists of dict resp
    for row in resp['values']:
        if row[0] and row[-1] != 'At Auction':
            if len(row) == 1:
                row.append('-')
                row.insert(2, status.check_status(vin=row[0]))
            elif len(row) == 2:
                row.insert(2, status.check_status(vin=row[0]))
            elif len(row) == 3:
                row[2] = status.check_status(vin=row[0])
    return resp['values']


# Updating values in the table
def app():
    service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range='carParser!G2:I100',
        valueInputOption='RAW',
        body=({'values': change_data()})).execute()
