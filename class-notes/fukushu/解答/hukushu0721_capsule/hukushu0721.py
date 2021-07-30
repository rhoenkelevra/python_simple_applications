from input_save import InputSave

data = input("データをひとつ入力してください。")
ins = InputSave(data)
print(f"入力したデータは：{ins.input_save}です。")
