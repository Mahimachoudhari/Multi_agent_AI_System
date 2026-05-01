import streamlit as st
from agents import research_agent, planner_agent, writer_agent
from logger import log_data
from workflow import create_workflow

st.set_page_config(
    page_title="Multi-Agent AI System",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Report Generator (Gemini)")

topic = st.text_input("Enter topic")


if st.button("Generate Report"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Researching..."):
            research = research_agent(topic)
            log_data("Research Agent", research)

        st.subheader("Research Output")
        st.write(research)

        with st.spinner("Planning structure..."):
            outline = planner_agent(research)
            log_data("Planner Agent", outline)

        st.subheader("Report Outline")
        st.write(outline)

        with st.spinner("Writing final report..."):
            report = writer_agent(outline)
            log_data("Writer Agent", report)

        st.subheader("Final Report")
        st.write(report)

        st.subheader("Workflow Visualization")
        workflow = create_workflow()
        st.graphviz_chart(workflow)