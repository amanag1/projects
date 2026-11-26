import argparse
from pathlib import Path
import pandas as pd

def report(src, out):
    df = pd.read_csv(src) if Path(src).suffix.lower()=='.csv' else pd.read_excel(src)
    profile=pd.DataFrame({'column':df.columns,'dtype':df.dtypes.astype(str),'missing':df.isna().sum().values,'unique':df.nunique().values})
    numeric=df.select_dtypes('number')
    summary=numeric.describe().T.reset_index() if len(numeric.columns) else pd.DataFrame({'note':['No numeric columns']})
    with pd.ExcelWriter(out,engine='openpyxl') as w:
        df.to_excel(w,index=False,sheet_name='Data');profile.to_excel(w,index=False,sheet_name='Profile');summary.to_excel(w,index=False,sheet_name='Summary')
        for ws in w.book.worksheets:
            ws.freeze_panes='A2';ws.auto_filter.ref=ws.dimensions
            for col in ws.columns: ws.column_dimensions[col[0].column_letter].width=min(max(max(len(str(c.value or '')) for c in col)+2,12),45)
    return out
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('input');p.add_argument('-o','--output',default='report.xlsx');a=p.parse_args();print(report(a.input,a.output)