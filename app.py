

import duckdb

import streamlit as st

#answer = """
#"SELECT * FROM beverages
#CROSS JOIN food_items
#"""

#solution_df = duckdb.sql(answer).df()
con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)


with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins", "Groupby", "Windows Functions"),
        index=None,
        placeholder="Select a theme..."
    )
    st.write("You selected:", theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)


st.header("enter your code")
query = st.text_area(label="votre code SQL ici", key="user_input")

#if query:
#    result = duckdb.sql(query).df()
#    st.dataframe(result)
#
#    if len(result.columns) != len(solution_df.columns):
#        st.write("Some columns are missing")
#
#    try:
#        result = result[solution_df.columns]
#        st.dataframe(result.compare(solution_df))
#    except KeyError as e:
#        st.write("some columns are missing")
#
#        n_lines_difference = result.shape[0] - solution_df.shape[0]
#        if n_lines_difference != 0:
#            st.write(
#                f"result has a {n_lines_difference} lines difference with the solution_df"
#            )
#        st.dataframe(result.compare(solution_df))
#
#tab2, tab3 = st.tabs(["Tables", "Solution_df"])
#
#
#with tab2:
#    st.write("table: beverages")
#    st.dataframe(beverages)
#    st.write("table: food_items")
#    st.dataframe(food_items)
#    st.write("expected:")
#    st.dataframe(solution_df)
#
#with tab3:
#    st.write(answer)
