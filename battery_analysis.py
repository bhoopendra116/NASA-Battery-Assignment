import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


dataset_path = r"D:\Bhoopendra_Singh_NASA_Battery_Assignment\cleaned_dataset\metadata.csv" 
data = pd.read_csv(dataset_path)


print("Dataset Columns:", data.columns)
print("Dataset Info:")
print(data.info())
print("First few rows of the dataset:")
print(data.head())


selected_data = data[['test_id', 'Re', 'Rct']] 


selected_data = selected_data.dropna(subset=['Re', 'Rct'])


selected_data['Re'] = pd.to_numeric(selected_data['Re'], errors='coerce')
selected_data['Rct'] = pd.to_numeric(selected_data['Rct'], errors='coerce')




fig1 = px.line(
    selected_data,
    x='test_id',
    y='Re',
    title='Electrolyte Resistance (Re) Over Test Cycles',
    labels={'test_id': 'Test ID', 'Re': 'Electrolyte Resistance (Ohms)'},
    template='plotly_dark'
)
fig1.show()


fig2 = px.line(
    selected_data,
    x='test_id',
    y='Rct',
    title='Charge Transfer Resistance (Rct) Over Test Cycles',
    labels={'test_id': 'Test ID', 'Rct': 'Charge Transfer Resistance (Ohms)'},
    template='plotly_dark'
)
fig2.show()


fig_combined = go.Figure()


fig_combined.add_trace(go.Scatter(
    x=selected_data['test_id'],
    y=selected_data['Re'],
    mode='lines',
    name='Electrolyte Resistance (Re)'
))


fig_combined.add_trace(go.Scatter(
    x=selected_data['test_id'],
    y=selected_data['Rct'],
    mode='lines',
    name='Charge Transfer Resistance (Rct)'
))


fig_combined.update_layout(
    title='Battery Parameters Over Test Cycles',
    xaxis_title='Test ID',
    yaxis_title='Resistance (Ohms)',
    template='plotly_dark',
    legend_title='Parameters'
)
fig_combined.show()