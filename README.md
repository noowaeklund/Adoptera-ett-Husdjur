# Adoptera ett husdjur

Welcome to the "Adoptera ett husdjur" project! This project, related to the course "webbserverprogrammering 1", was built using the "Flask" framework. This is the first project and it's intended to utilize practices in preparation for this project by getting familiarity with the following concepts:

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## Installation

Follow these steps to install the project locally:


```bash
git clone https://github.com/noowaeklund/Adoptera-ett-husdjur.git
cd Adoptera-ett-husdjur
# Install necessary dependencies
pip install -r requirements.txt
```

## Usage


Here's how you can get started with using the project. Follow the instructions below and refer to the provided code examples for clarity.

Running the Application

1. Ensure you have cloned the repository and installed the necessary dependencies as mentioned in the Installation section.
2. Start the Flask application by running the following command in your terminal:
   python app.py
3. Open your web browser and navigate to http://127.0.0.1:5000 to view the application.


Example Usage
Below are some code snippets to demonstrate how the application works.


Accessing the Home Page
The home page lists the types of pets available for adoption. Navigate to http://127.0.0.1:5000 or http://127.0.0.1:5000/animals.

@app.route('/animals')
@app.route('/')
def index():
    """Returns the HTML content for the index page."""
    return '''<h1>Adopt a Pet!</h1>
    <p>Browse through the links below to find your new furry friend:</p>
    <ul>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
    </ul>'''



Viewing a List of Pets
To view a list of pets of a specific type (e.g., cats), navigate to http://127.0.0.1:5000/animals/cats.

@app.route('/animals/<pet_type>')
def animals(pet_type):
    """Returns a list of animals of the specified pet type."""
    content_list = helper.pets[pet_type]
    content_items = ''.join([f"<li><a href='/animals/{pet_type}/{content_list.index(item)}'>{item['name']}</a></li>" for item in content_list])
    return f'''<h1>List of {pet_type}:</h1>
    <ul>
      {content_items}
    </ul>
    '''


Viewing Pet Details
To view detailed information about a specific pet, navigate to http://127.0.0.1:5000/animals/cats/0 (replace cats and 0 with the appropriate pet type and ID).

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    """Get information about a pet."""
    content_list = helper.pets[pet_type]
    pet_url = content_list[pet_id]['url']
    return f'''<h1>Details of {content_list[pet_id]['name']}:</h1>
    <p> Name: {content_list[pet_id]['name']}</p>
    <p> Age: {content_list[pet_id]['age']}</p>
    <p> Breed: {content_list[pet_id]['breed']}</p>
    <p> Description: {content_list[pet_id]['description']}</p>
    <img src="{pet_url}" alt="{content_list[pet_id]['name']}">
    '''


By following these instructions, you can easily set up and interact with the "Adoptera ett husdjur" application. Feel free to explore and extend the functionality as needed.



## Features
- Browse through a wide variety of pets available for adoption
- Filter pets based on species, age, and location
- View detailed information about each pet, including their biography and adoption requirements
- Contact the pet owner or adoption agency directly for more information or to arrange a meeting

## License

This project is licensed under [MIT](LICENSE). For more details, see the `LICENSE` file.

## Contact

Noowa Eklund - [noowa.eklund@elev.ga.ntig.se](noowa.eklund@elev.ga.ntig.se) 

Project Link: [https://github.com/noowaeklund/Adoptera-ett-Husdjur](https://github.com/noowaeklund/Adoptera-ett-Husdjur)

## Acknowledgments

- Thanks to those whose code was utilized
- Inspiration sources
- Additional acknowledgments


