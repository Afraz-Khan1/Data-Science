from flask import Flask,request,jsonify,render_template,redirect,url_for # render_template used to run html file means putting values on html tags at the time of result.
# App → API request → API responds with JSON data. this is called working with API. using http requests like POST, PUT(update), DELETE etc and getting answer from api usually in json.

app=Flask(__name__)

items=[{"id":1,"name":"Item 1","description":"This is item 1"},
       {"id":2,"name":"Item 2","description":"This is item 2"}]

#home
@app.route("/")
def home():
   return "Welcome To The Basic 'TO-DO' List App"

# GET: retriving all data request from the app using http request get and api convey the request to database and return data in json format.
@app.route("/items",methods=["GET"])                                   # if we dont write any method it is understood to be GET method.
def get_items():                                                           #Client → HTTP GET → API route → data → JSON response
   return jsonify(items)                                               #That’s exactly working with an API.


# GET: retriving specific item
@app.route("/items/<int:item_id>")
def get_item(item_id):
   # making a generator expression to search for the item of mathcing id and using next func to start the generator working. 
   item=next((item for item in items if item["id"]==item_id),None)
   if item==None:
      return jsonify({"Error":"Item of matching id was not found"})
   return jsonify(item)

# POST: create or add an item
@app.route("/create_item",methods=["GET","POST"])
def add_item():
   if request.method=="GET":
      return render_template('create_item.html')
   
   items.append({"id":request.form["id"],
   "name":request.form["name"],
   "description":request.form["description"]})

   return redirect(url_for('get_items')) # get_items func name should be used here rather then /items

# PUT: update existing item
# to use put and delete you need to download postman and select the task like put and delete you can give new data with same id to be updated in post man as browser dont have request of put and delete so for these method use download post man
@app.route("/items/<int:item_id>",methods=["PUT"])
def update_item(item_id):
   
   
   item=next((item for item in items if item["id"]==item_id),None) # generator expression.
   if item==None:
      return jsonify({"RESULT":"item of same if was not found"}) # ok so in json sample file i have written a dictionary. that is the body of input means when you give data to update it will be given in such style in post man thats why it is needed.
   item["name"]=request.json.get["name",item["name"]] # replace the list item[name] value of matched id with current client provided json item[name] value in json sample file.
   item["description"]=request.json.get["description",item["description"]]

   return jsonify(items)



# Delete: to delete a item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
   global items                                         # global is needed to update the items data if no global use it create a copy of changes .
   items=[item for item in items if item["id"]!=item_id] # list comprehension . and != item_id will only add the items whos id dont match in items removing the item whos id matched
   return jsonify({"Result: Item was Deleted Succesfully"})


if __name__=="__main__":
   app.run(debug=True) 