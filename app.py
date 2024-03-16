import subprocess
from flask import Flask,  render_template_string

app = Flask(__name__)
html="""
<html>
</html>
"""
# render_template_string(html)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/slit')
def about():
    subprocess.call(['streamlit', 'run', 'app.py'])

