import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
from geopy.distance import geodesic

# Google Drive API認証情報を読み込む
SERVICE_ACCOUNT_FILE = '796149587765-hvdm2lr210hgahkvk9cuu8nogjicbaef.apps.googleusercontent.com'  # 認証JSONファイルのパス
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

# Streamlitアプリのタイトル
st.title("Google Driveから加盟店データを取得して検索")

# 認証のセットアップ
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build('drive', 'v3', credentials=credentials)

# Google Driveからエクセルファイルをダウンロード
file_id = '115050716719602225845'  # ファイルIDをここに設定
request = service.files().get_media(fileId=file_id)
file_data = io.BytesIO()
downloader = MediaIoBaseDownload(file_data, request)
done = False
while not done:
    status, done = downloader.next_chunk()

# エクセルデータをPandasで読み込む
file_data.seek(0)
加盟店_data = pd.read_excel(file_data)

# 検索処理
st.write("最寄り駅を入力して、10km圏内の加盟店を検索します。")
station_name = st.text_input("最寄り駅名を入力してください（「駅」は省略可能です）:")

if station_name:
    # (ここにOpenCageや地図関連の処理を追記する)
    st.write(加盟店_data)  # 読み込んだデータの表示（デバッグ用）
else:
    st.write("駅名を入力してください。")
