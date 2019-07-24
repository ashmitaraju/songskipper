from app import app
from flask import Flask, render_template, url_for, redirect
from app.utils import read_data
import json

@app.route('/')
def index():

    data = read_data()
    current = data['yeh_jawaani_audio_full_moviepy.wav']
    return render_template('index.html', timings=json.dumps(current))