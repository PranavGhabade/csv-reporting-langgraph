import pandas as pd

from state import GraphState
from utils.csv_loader import load_csv


def profiler_node(state: GraphState):

    print("\n===== PROFILER NODE =====")

    # Load CSV
    df = load_csv(state["csv_path"])

    # Detect datetime columns
    for column in df.select_dtypes(include=["object"]).columns:

        try:

            converted = pd.to_datetime(
                df[column],
                errors="coerce"
            )

            # Convert only if at least 80% of the values are valid dates
            if converted.notna().sum() >= len(df) * 0.8:
                df[column] = converted

        except Exception:
            pass

    # Group columns by datatype
    column_groups = {

        "numerical":
        df.select_dtypes(include="number").columns.tolist(),

        "categorical":
        df.select_dtypes(include="object").columns.tolist(),

        "datetime":
        df.select_dtypes(include="datetime").columns.tolist(),

        "boolean":
        df.select_dtypes(include="bool").columns.tolist()

    }

    # Data quality metrics
    missing_values = df.isnull().sum().to_dict()

    missing_percentage = (
        (df.isnull().sum() / len(df)) * 100
    ).round(2).to_dict()

    duplicate_rows = int(df.duplicated().sum())

    # Data preview
    sample_records = df.head(5).to_dict(orient="records")

    random_records = (
        df.sample(
            min(5, len(df)),
            random_state=42
        )
        .to_dict(orient="records")
    )

    # Build profile
    profile = {

        "dataset_info": {

            "rows": len(df),

            "columns": len(df.columns),

            "duplicate_rows": duplicate_rows

        },

        "schema": {

            "column_names": list(df.columns),

            "data_types": df.dtypes.astype(str).to_dict()

        },

        "data_quality": {

            "missing_values": missing_values,

            "missing_percentage": missing_percentage

        },

        "column_groups": column_groups,

        "sample_records": sample_records,

        "random_records": random_records

    }

    print("Profiling Complete.")

    return {

        "dataframe": df,

        "profile": profile

    }


