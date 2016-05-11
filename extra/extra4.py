import asyncio
import concurrent.futures
import requests
from urllib import request
from urllib import parse
import json
import sys
####
# 初期値設定
####
# APIアクセスキー
keyid     = "6393a011e901efaab0f687d241341a24"
url1="http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
url2="http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
# メニュー
menu_name = u"ハンバーグ"
menu_name1 = u"チーズケーキ"
#文字コード
encoding = 'utf-8'
 
####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name.encode(encoding) ),
  ( "hit_per_page" ,3)
]

query1 = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name1.encode(encoding) ),
  ( "hit_per_page" ,3)
]

url1+="?{0}".format(parse.urlencode( query ) )
url2+="?{0}".format(parse.urlencode( query1 ) )
####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
    if isinstance( data, str ) or isinstance( data, unicode ) :
        return True
    else :
        return False


def analysis(data):
    if "error" in data :
        if "message" in data :
            print (u"{0}".format( data["message"] ))
        else :
            print (u"データ取得に失敗しました。")
            sys.exit()

    # ヒット件数取得
    total_hit_count = None
    if "total_hit_count" in data["response"] :
        total_hit_count = data["response"]["total_hit_count"]

    #ページごとの件数を取得
    hit_per_page = None
    if "hit_per_page" in data["response"] :
        hit_per_page = data["response"]["hit_per_page"]
 
    # ヒット件数が0以下、または、ヒット件数がなかったら終了
    if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
       print (u"指定した内容ではヒットしませんでした。")
       sys.exit()

    # ヒット件数表示
    print ("{0}件ヒットしました。".format( total_hit_count ))
    print ("----")

    # 出力件数
    disp_count = 0
 
    # 応援口コミデータ取得
    for i in range( hit_per_page ) :
        photo = data["response"]["{0}".format(i)]["photo"]
        line                 = []
        id                   = ""
        name                 = ""
        mname                = ""
        comment              = ""
        shop_url             = ""
 
        # 店舗番号
        if "shop_id" in photo and is_str( photo["shop_id"] ) :
            id = photo["shop_id"]
        line.append( id )
 
        # 店舗名
        if "shop_name" in photo and is_str( photo["shop_name"] ) :
            name = photo["shop_name"]
        line.append( name )
 
        # メニュー名
        if "menu_name" in photo and is_str( photo["menu_name"] ) :
            mname = photo["menu_name"]
        line.append( mname )
 
        # コメント
        if "comment" in photo and is_str( photo["comment"] ) :
            comment = photo["comment"]
        line.append( comment )

        #URL
        if "shop_url"in photo and is_str( photo["shop_url"]):
            shop_url=photo["shop_url"]
        line.append( shop_url)
        # タブ区切りで出力
        print ("\t".join( line ))
        disp_count += 1
 
    # 出力件数を表示して終了
    print ("----")
    print (u"{0}件出力しました。".format( disp_count ))
async def queue_execution(arg_urls, callback, parallel=2):
    loop = asyncio.get_event_loop()
    queue = asyncio.Queue()

    for u in arg_urls:
        queue.put_nowait(u)
        print (u)

    async def fetch(q):
        while not q.empty():
            u = await q.get()
            future = loop.run_in_executor(None, requests.get, u)
            future.add_done_callback(callback)
            result=requests.get(u)
            data=json.loads(result.text)
            analysis(data)
            await future

    tasks = [fetch(queue) for i in range(parallel)]
    return await asyncio.wait(tasks)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    results = []
    def store_result(f):
        results.append(f.result())
    loop.run_until_complete(queue_execution([url1,url2], store_result))  

