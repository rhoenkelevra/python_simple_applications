import mysql.connector as mydb


class UserDAO:
    
    # 初期化メソッド
    def __init__(self):
        # ログイン状態管理用変数
        self.__login_user = 0
    
    
    # ログイン状態取得用プロパティ
    @property
    def login_user(self):
        return self.__login_user
    
    
    # ログイン判定を行うメソッド
    def login(self, search1, search2):
        # 成否管理変数
        success = False
        
        # コネクションの作成
        conn = mydb.connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="login_sample"
        )
        
        # カーソルの作成
        cur = conn.cursor()
        
        data = (search1, search2)
        
        # SQL文の実行
        cur.execute("SELECT * FROM user WHERE id = %s AND pass = %s", data)
        
        # 実行結果を取得
        rows = cur.fetchall()
        
        # 成否の判断
        if cur.rowcount == 1:
            print(f"ようこそ {rows[0][2]} さん。")
            success = True
            self.__login_user = rows[0][0]
        else:
            print("ログイン失敗しました。")
        
        # カーソルの切断
        cur.close()
        
        # コネクションの切断
        conn.close()
        
        return success
    
    
    # ログアウトを行うメソッド
    def logout(self):
        self.__login_user = 0
        print("ログアウトしました。")
    
    
    # 新規ユーザ登録を行うメソッド
    def add_user(selef, data1, data2, data3):
        # コネクションの作成
        conn = mydb.connect(
            host="localhost",
            port="3306",
            user="root",
            password="pass",
            database="login_sample"
        )
        
        # カーソルの作成
        cur = conn.cursor()
        
        data = (data1, data2, data3)
        
        # SQL文の実行
        cur.execute("INSERT INTO user(id, name, pass, d_flg) values(%s, %s, %s, 0)", data)
        
        # 重複判断
        if cur.rowcount > 0:
            dup = True
            
        # コミット
        conn.commit()
        
        # カーソルの切断
        cur.close()
        
        # コネクションの切断
        conn.close()
        
        return dup
    
    
