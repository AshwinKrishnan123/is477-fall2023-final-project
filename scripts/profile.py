import pandas as pd
from ydata_profiling import ProfileReport

filename= 'data/turkish+music+emotion.zip'

df = pd.read_csv(filename)

profile = ProfileReport(df, title="Profiling Report", minimal=True) 
#resulting file >100 mb, cannot upload to GitHub
profile.to_file("profiling/report.html")