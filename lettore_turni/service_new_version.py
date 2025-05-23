import pdfplumber
import pandas as pd

file_name = input("Inserire il nome del file che si vuole convertire ")

all_table_data = []


with pdfplumber.open (f"{file_name}.pdf") as pdf :
     pages = pdf.pages
     
     tables = pages[1].extract_tables()
     table_header = tables[0]
     #table_header[0].insert(0, "index")
     
     for page in pdf.pages :
         pages_table = page.extract_tables()
         #print(pages_table)
            
         try :
            table_data = pages_table[1:]
            #print(table_data)
         except Exception as Err :
            print(Err)
         
         for data in table_data :
            df = pd.DataFrame(data, columns=table_header[0])
            
            with pd.ExcelWriter("turni.ext", mode='a', if_sheet_exists="new", engine='openpyxl') as file_excel :
                df.to_excel("turni.xlsx", index=True, engine='openpyxl')
            #print(df)
            all_table_data.append(df)
     print(all_table_data)
"""            
completed_df = pd.concat(all_table_data, ignore_index=True)
completed_df.to_excel("turni.xlsx", index=True)
"""