import plotly.graph_objects as go
import plotly.express as px

# Since mermaid is not working, create a Flask auth architecture diagram using Plotly
# Create a network-like visualization showing the Flask authentication flow

# Define the nodes and their positions
nodes = {
    'Browser/User': (0, 5),
    'Templates': (0, 4),
    'Flask Routes': (0, 3),
    'Login Route': (-2, 2),
    'Register Route': (0, 2),
    'Dashboard Route': (2, 2),
    'LoginForm': (-2, 1),
    'RegForm': (0, 1),
    'Auth Check': (2, 1),
    'Flask-Login': (0, 0),
    'Password Hash': (-1, 0),
    'User Model': (0, -1),
    'SQLite DB': (0, -2)
}

# Create edges (connections)
edges = [
    ('Browser/User', 'Templates'),
    ('Templates', 'Flask Routes'),
    ('Flask Routes', 'Login Route'),
    ('Flask Routes', 'Register Route'),
    ('Flask Routes', 'Dashboard Route'),
    ('Login Route', 'LoginForm'),
    ('Register Route', 'RegForm'),
    ('Dashboard Route', 'Auth Check'),
    ('LoginForm', 'Flask-Login'),
    ('RegForm', 'Password Hash'),
    ('Auth Check', 'Flask-Login'),
    ('Flask-Login', 'User Model'),
    ('Password Hash', 'User Model'),
    ('User Model', 'SQLite DB')
]

# Create the figure
fig = go.Figure()

# Add edges
for start, end in edges:
    x0, y0 = nodes[start]
    x1, y1 = nodes[end]
    fig.add_trace(go.Scatter(
        x=[x0, x1], y=[y0, y1],
        mode='lines',
        line=dict(color='#333333', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))

# Add nodes with colors based on layer
colors = {
    'Browser/User': '#1FB8CD',
    'Templates': '#DB4545', 
    'Flask Routes': '#2E8B57',
    'Login Route': '#5D878F',
    'Register Route': '#5D878F', 
    'Dashboard Route': '#5D878F',
    'LoginForm': '#D2BA4C',
    'RegForm': '#D2BA4C',
    'Auth Check': '#B4413C',
    'Flask-Login': '#964325',
    'Password Hash': '#944454',
    'User Model': '#13343B',
    'SQLite DB': '#DB4545'
}

# Add nodes
for node, (x, y) in nodes.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode='markers+text',
        marker=dict(
            size=40,
            color=colors.get(node, '#1FB8CD'),
            line=dict(width=2, color='white')
        ),
        text=node.replace(' ', '<br>'),
        textposition='middle center',
        textfont=dict(size=10, color='white'),
        showlegend=False,
        hoverinfo='text',
        hovertext=node
    ))

# Update layout
fig.update_layout(
    title="Flask Auth Architecture",
    showlegend=False,
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Save as both PNG and SVG
fig.write_image('flask_auth_chart.png')
fig.write_image('flask_auth_chart.svg', format='svg')

print("Flask authentication architecture chart saved as PNG and SVG")