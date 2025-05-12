from flask import Flask, render_template, jsonify, redirect, url_for, session, request, flash
import csv
from functools import wraps
from datetime import datetime, timedelta 
from werkzeug.urls import url_quote 
from google.cloud import bigquery
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Set the environment variable for the service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account-key.json"

@app.route('/influencer_performance')
def dashboard():
    print(session.get('authenticated'))
    if not session.get('authenticated'):        
        return redirect(url_for('new_template'))
    print('wallace')
    return render_template('influencer_performance.html') 

@app.route('/influencer_performance/<influencer_code>')
def influencer_performance(influencer_code):
    if not session.get('authenticated'):
        return redirect(url_for('new_template'))
    start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('influencer_performance.html', influencer_code=influencer_code, start_date=start_date, end_date=end_date)

@app.route('/')
def new_template():
    session['authenticated'] = False
    return render_template('influencer_dashboard.html')

def validate_login(influencer_code, password):
    client = bigquery.Client()
    query = """
        SELECT * FROM `hadronlink-61c5d.support.influencer_credentials`
        WHERE username = @username AND password = @password
    """
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("username", "STRING", influencer_code),
            bigquery.ScalarQueryParameter("password", "STRING", password),
        ]
    )
    query_job = client.query(query, job_config=job_config)
    results = query_job.result()

    if results.total_rows > 0:
        session['authenticated'] = True
        session['influencer_code'] = influencer_code
        return True
    return False

@app.route('/login', methods=['POST'])
def login():
    influencer_code = request.form['influencer-code']
    password = request.form['password']
    if validate_login(influencer_code, password):
        return redirect(url_for('influencer_performance', influencer_code=influencer_code))
    else:
        flash('Invalid influencer code or password')
        return redirect(url_for('new_template', error=1))
    
@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return '', 204

@app.route('/api/data')
def get_data():
    client = bigquery.Client()
    query = """
        SELECT * FROM `hadronlink-61c5d.product.influencer_performance`
    """
    query_job = client.query(query)
    results = query_job.result()

    data = [dict(row) for row in results]
    
    # Convert date objects to strings
    for row in data:
        row['date'] = row['date'].strftime('%Y-%m-%d')
    
    #print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


