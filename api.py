import requests
from flask import Flask, render_template
from manager import fetch_projects_within_radius, fetch_recently_updated_projects

app = Flask(__name__)
 
@app.route('/')
def base():
   """
   base page
   """
   return render_template("index.html")

@app.route('/projects', methods=['POST'])
def projects(request):
   """
   this is beyond sloppy.
   request data is lat & long
   call manager methods
   """
   if request.data.get('latitude') and request.data.get('longitude'):
      projects = fetch_projects_within_radius() # TODO
   else:
      projects = fetch_recently_updated_projects() # TODO

   # TODO load `projects` arrs into json, then return json data
   pass
 
if __name__ == '__main__':
   app.run(debug=False, host='0.0.0.0')

