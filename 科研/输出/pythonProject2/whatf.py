import pandas as pd
import pickle as pkl

with open("D:\python\pycharm\project\pythonProject2\sample_instances.pkl", "rb") as f:
    object = pkl.load(f,encoding='utf8')

df = pd.DataFrame(object)
df.to_csv(r'D:\python\pycharm\project\pythonProject2\新建 Microsoft Excel 工作表.csv')
