
import pandas as pd
import numpy as np
from io import BytesIO

def load_and_clean(files):
    dfs = [pd.read_csv(f, encoding="latin-1", sep=";") for f in files]

    def verifier_uniques_id(*dfs):
        results = {}
        for i, df in enumerate(dfs):
            name = f"DataFrame_{i+1}"
            if 'Identifiant CNR' in df.columns:
                results[name] = df['Identifiant CNR'].is_unique
            else:
                results[name] = False
        return results

    def garder_lignes_plus_completes(df, subset):
        df['_nb_na'] = df[subset].isna().sum(axis=1)
        df = df.sort_values(by='_nb_na')
        df = df.drop_duplicates(subset=subset, keep='first')
        return df.drop(columns=['_nb_na'])

    # Exemple de nettoyage de base
    merged_df = pd.concat(dfs, ignore_index=True)
    subset_cols = [col for col in merged_df.columns if 'Identifiant' in col]
    cleaned_df = garder_lignes_plus_completes(merged_df, subset=subset_cols)

    # Convertir en fichiers pour téléchargement
    merge_io = BytesIO()
    clean_io = BytesIO()
    merged_df.to_csv(merge_io, sep=";", index=False)
    cleaned_df.to_csv(clean_io, sep=";", index=False)
    merge_io.seek(0)
    clean_io.seek(0)

    return merge_io, clean_io, cleaned_df.head(100).to_html(classes='table table-bordered')
