import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, CD, User
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, date
from flask_mail import Mail, Message

