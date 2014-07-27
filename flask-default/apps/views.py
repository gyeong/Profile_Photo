#-*- coding: utf-8 -*-
from flask import render_template, Flask, request
from apps import app

import urllib 
from bs4 import BeautifulSoup

from flaskext import wtf
from flaskext.wtf import Form, TextField, TextAreaField, \
SubmitField, validators, ValidationError

class ContactForm(Form):
	name = TextField("Name", [validators.Required("Please enter your name")])
	email = TextField("Email", [validators.Required("Please enter your email address"), \
				validators.Email("Please enter valid email address")])
	subject = TextField("Subject", [validators.Required("Please enter a subject")])
	message = TextAreaField("Message", [validators.Required("Please enter a message")])
	submit = SubmitField("Send")

@app.route('/')
@app.route('/index', methods=["GET","POST"])
def index():
	return render_template('index.html')


@app.route('/mju', methods=["GET","POST"])
def mju():
	get = request.args['input_h']
	url = "http://www.mju.ac.kr/mbs/mjukr/jsp/board/list.jsp?qt=&boardId=11294&listType=01&id=mjukr_050101000000&column=TITLE&search=" +get+ "&x=0&y=0"


	htmltext = urllib.urlopen(url).read()

	soup = BeautifulSoup(htmltext,from_encoding="urf-8")

	authors = [ ]
	for tag in soup.select(".subject "):
		authors.append(tag.get_text())

	return render_template('result.html',  text = authors)

	#for author in authors:
	#	print author




