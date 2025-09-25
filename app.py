from flask import Flask, redirect, render_template, request, session, url_for
from flask_session import Session
import os, requests, psycopg2, json
from lib.media_repository import MediaRepository
from lib.media import Media

app = Flask(__name__)

app.config["SESSION_PERMENANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

conn = psycopg2.connect(database="media", user="postgres", password="password6", host="localhost", port="5432") 

media_repository = MediaRepository(conn)

# for media in media_repository.all():
#     print(media)
    
# create a cursor 
cur = conn.cursor() 
  
# if you already have any table or not id doesnt matter this  
# will create a products table for you. 
cur.execute( 
    '''CREATE TABLE IF NOT EXISTS products (id serial PRIMARY KEY, name varchar(100), price float);''') 
  
# Insert some data into the table 
cur.execute( 
    '''INSERT INTO products (name, price) VALUES ('Apple', 1.99), ('Orange', 0.99), ('Banana', 0.59);''') 
  
# commit the changes 
conn.commit() 



@app.route("/")
def index():
    # call = requests.get("https://api.unsplash.com/photos/0X6HTVHn_kg/statistics?client_id=hp-n5d8W2_nK0fG91scJv4G9dGCGlxF_7VKonhj0TX8")
    # data = call.json()
    conn = psycopg2.connect(database="media", 
                            user="postgres", 
                            password="password6", 
                            host="localhost", port="5432")
    # create a cursor 
    cur = conn.cursor() 
    
    # Select all products from the table 
    cur.execute('''SELECT * FROM products LIMIT 5''') 
  
    # Fetch the data 
    data = cur.fetchall() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
    return render_template("index.html", name=session.get("name"), data=data)

@app.route('/edit')
def edit():
    image_id = request.args.get("image_id")
    image_url = request.args.get("image_url")
    creator = session.get("name")
    session['media'] = image_id
    
    if image_id:
        session['media'] = image_id
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
# @app.route('/rotate_image', methods=['POST'])
# def rotate_image():
#     media_data = session.get('media')
#     if media_data:
#         media = Media(**media_data)
#     else:
#         return "No media loaded", 400
    
#     data = request.json
#     print(data)
#     rotation_degrees = int(data.get('rotation', 0))
#     media.apply_rotation(rotation_degrees)
    
#     session['media'] = media.__dict__
#     print(media.__dict__)
    
#     return json.dumps({"status": "success", "rotation": media.rotation}), 200

@app.route('/save_media', methods=['GET', 'POST']) 
def save(): 
    
    creator = session.get("name")
    media_data = session.get('media')
    print(media_data)
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
    if media_data:
        media_repository = MediaRepository(conn)
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
  
  
@app.route('/update', methods=['POST']) 
def update(): 
    conn = psycopg2.connect(database="media", 
                            user="postgres", 
                            password="password6", 
                            host="localhost", port="5432") 
  
    cur = conn.cursor() 
  
    # Get the data from the form 
    name = request.form['name'] 
    price = request.form['price'] 
    id = request.form['id'] 
  
    # Update the data in the table 
    cur.execute( 
        '''UPDATE products SET name=%s,\ 
        price=%s WHERE id=%s''', (name, price, id)) 
  
    # commit the changes 
    conn.commit() 
    return redirect(url_for('index')) 
  
  
@app.route('/delete', methods=['POST']) 
def delete(): 
    conn = psycopg2.connect(database="media", user="postgres", 
     password="password6", 
     host="localhost", port="5432") 
    
    cur = conn.cursor() 
  
    # Get the data from the form 
    id = request.form['id'] 
  
    # Delete the data from the table 
    cur.execute('''DELETE FROM products WHERE id=%s''', (id,)) 
  
    # commit the changes 
    conn.commit() 
  
    # close the cursor and connection 
    cur.close() 
    conn.close() 
  
    return redirect(url_for('index')) 
  
  
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