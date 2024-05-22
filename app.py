from flask import Flask

import helper

app = Flask(__name__)


@app.route('/')
def index():
  """Returns the HTML content for the index page.

  This function generates the HTML content for the index page of the Adopt a Pet application.
  It includes a heading, a brief description, and links to browse different animal categories.

  Returns:
      str: The HTML content for the index page.
  """
  return '''<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>'''


@app.route('/animals/<pet_type>')
def animals(pet_type):
  """
  Returns a list of animals of the specified pet type.

  Args:
      pet_type (str): The type of pet.

  Returns:
      str: A formatted HTML string containing a list of animals of the specified pet type.
  """  
  content_list = helper.pets[pet_type]
  content_items = ''.join([f"<li><a href='/animals/{pet_type}/{content_list.index(item)}'>{item['name']}</a></li>" for item in content_list])
  return f'''<h1>List of {pet_type}:</h1>
  <ul>
    {content_items}
  </ul>
  '''




@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  """Get information about a pet.

  Args:
      pet_type (str): The type of pet.
      pet_id (int): The ID of the pet.

  Returns:
      str: HTML content containing information about the pet.
  """
  content_list = helper.pets[pet_type]
  pet_url = content_list[pet_id]['url']
  return f'''<h1>List of {pet_type}:</h1>
  <p> Name: {content_list[pet_id]['name']}</p>
  <p> Age: {content_list[pet_id]['age']}</p>
  <p> Breed: {content_list[pet_id]['breed']}</p>
  <p> Description: {content_list[pet_id]['description']}</p>
  <img src="{pet_url}" alt="{content_list[pet_id]['name']}">
'''


app.run(debug=True, host="0.0.0.0")
