from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import os, requests, psycopg2, json
from lib.media_repository import MediaRepository
from lib.media import Media

app = Flask(__name__)

app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = psycopg2.connect(database="media", user="postgres", password="Password6", host="localhost", port="5432") 

media_repository = MediaRepository(conn)

@app.route("/")
def index():
    
    return render_template("index.html", name=session.get("name"))

@app.route('/edit')
def edit():
    image_id = request.args.get("image_id")
    image_url = request.args.get("image_url")
    creator = session.get("name")
    
    if image_id:
        session['media'] = int(image_id)
        print(session['media'])
        print(creator)
        conn = psycopg2.connect(database="media", 
                                user="postgres", 
                                password="password6", 
                                host="localhost", port="5432")
        media_repository = MediaRepository(conn)
        image = media_repository.find_one(creator, image_id)
        image_urll = image[1]
        media = image
        conn.commit()
        return render_template("edit.html", name=creator, image=image_urll, media=list(media))
    elif image_url:
        session['media'] = image_url
        return render_template("edit.html", name=creator, image=image_url)
    else:
        return "No image selected", 400
    
@app.route('/library')
def library():
    creator = session.get("name")
    media = []
    conn = psycopg2.connect(database="media", 
                            user="postgres", 
                            password="password6", 
                            host="localhost", port="5432")
    media_repository = MediaRepository(conn)
    media = media_repository.find_users_all(creator) # find all users saved images (could be any number)
    print(media)
    return render_template("library.html", name=creator, library=media)

@app.route('/save_media', methods=['GET', 'POST']) 
def save(): 
    
    creator = session.get("name")
    media_data = session.get('media')
    data = request.json
    rotation_degrees = data.get('rotation')
    brightness_value = int(data.get('brightness'))
    skew_numbers = data.get('skew')
    gradient = data.get('gradient')
    gradient_colors = data.get('gradient_colors')

    conn = psycopg2.connect(database="media", 
                            user="postgres", 
                            password="password6", 
                            host="localhost", port="5432")
    media_repository = MediaRepository(conn)
    
    if type(media_data) is int: # means we are re-editing image so update is required
        media_repository.update(media_data, rotation_degrees, brightness_value, skew_numbers, gradient, gradient_colors)
        conn.commit()
        conn.close()
        print("media updated")
    elif type(media_data) is str:
        new_media = Media(None, 
                          media_data, 
                          creator,
                          rotation_degrees, brightness_value, skew_numbers, gradient, gradient_colors)
        print(new_media.__dict__)
        media_repository.create(new_media)
        # media_repository.update(media_data["id"], rotation_degrees, brightness_value, skew_numbers, gradient, gradient_colors)
        conn.commit()
        conn.close() 
    else:
        return "No media loaded", 400
    return json.dumps({"status": "success", "rotation": rotation_degrees, "brightness": brightness_value}), 200

  
if __name__ == '__main__': 
    app.run(debug=True) 

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()

    return redirect("/")
