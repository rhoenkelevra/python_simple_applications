from module.user_dao import UserDAO

# UserDAOインスタンスの生成
ud = UserDAO()
# トップメニューでの利用者操作管理変数
inp = "0"

# アプリケーション始動
print("-" * 7, "アプリケーションへようこそ", "-" * 7)

# 無限ループ
while True:
    # トップメニュー
    print("\n"+"-" * 7, "トップメニュー", "-" * 7)
    
    # ログイン状態の有無で出力内容変更
    if ud.login_user == 0:
        inp = input("1:ログイン　2:新規ユーザ登録　0:終了->")
    else:
        inp = input("1:ログアウト　2:検索　0:終了->")
    
    # 0と入力されたらプログラム終了
    if inp == "0":
        break
    
    # 1と入力されたら
    if inp == "1":
        if ud.login_user == 0:
            print("\n"+"-" * 7, "ログイン", "-" * 7)
            user_id = input("ユーザID（メールアドレス）を入力->")
            user_pass = input("パスワードを入力->")
            ud.login(user_id, user_pass)
        else:
            print("\n"+"-" * 7, "ログアウト", "-" * 7)
            ud.logout()
    elif inp == "2":
        if ud.login_user == 0:
            print("\n"+"-" * 7, "新規ユーザ登録", "-" * 7)
            user_id = input("ユーザID（メールアドレス）を入力->")
            user_name = input("名前を入力->")
            user_pass = input("パスワードを入力->")
            ud.add_user(user_id, user_name, user_pass)
        else:
            print("\n"+"-" * 7, "検索", "-" * 7)
            print("*" * 7, "未実装", "*" * 7)
