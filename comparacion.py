import pandas as pd

informe_manual = pd.read_excel("your route")
informe_manual.to_csv("your route")
#informe_automatizado = pd.read_csv("./datos/informe_automatizado.csv")
#print(informe_automatizado)

data_informe_sebas = pd.read_csv(
         "your_route/informe_automatizado.csv",
         index_col=26,
         dtype={"Ad id.": "str"},
         )
data_informe_extraccion = pd.read_csv(
         "your_route/informe_manual.csv",
         index_col=28,
         encoding="utf-8",
         dtype={"Ad id.": "str"},
         )

df_informe_sebas = pd.DataFrame(data=data_informe_sebas)
df_informe_extraccion = pd.DataFrame(data=data_informe_extraccion)
print(df_informe_sebas)
print(df_informe_extraccion)
df_informe_extraccion_depurado = df_informe_extraccion[
        df_informe_extraccion["Impressions"] != 0
        ]
df_informe_extraccion_depurado_sin_na = df_informe_extraccion_depurado.dropna()

datos_a_comparar = ["Fiber", "25-100", "SALES FIBER", "SALES 25-100", "Credit Check"]

for datos in datos_a_comparar:
    columna_a_comparar_df1 = df_informe_extraccion_depurado_sin_na[[datos]].astype(int)
    columna_a_comparar_df2 = df_informe_sebas[[datos]]

    df_merged = pd.merge(
            columna_a_comparar_df1,
            columna_a_comparar_df2,
            on="Ad id.",
            suffixes=("_name1", "_name2"),
            )

    df_merged["diferencias"] = (
            df_merged[f"{datos}_name1"] != df_merged[f"{datos}_name2"]
            )
    conteo_diferencias = df_merged["diferencias"].sum()

    df_merged.to_excel(
             f"your_route/comparacion_{datos}.xlsx"
             )

    print(df_merged)
    print(
            "\n============================================================================================"
            )
    print(
            f"\n                              Numero total de diferencias: {conteo_diferencias}\n"
            )
    print(
            "============================================================================================\n"
            )

key = input("Press Key to continue...")
if key != "":
    print(":)") 
