import pdfplumber
import pandas as pd
import os

input_path = r"C:\n8n\input\agsk-test.pdf"
output_path = r"C:\n8n\output\converted_output.xlsx"

with pdfplumber.open(input_path) as pdf:
    all_tables = []
    for page in pdf.pages:
        table = page.extract_table()
        if table:
            df = pd.DataFrame(table[1:], columns=table[0])
            all_tables.append(df)

    if all_tables:
        final_df = pd.concat(all_tables, ignore_index=True)
        final_df.to_excel(output_path, index=False)
        print("Успешно сохранено:", output_path)
    else:
        print("⚠️ Таблиц не найдено")
