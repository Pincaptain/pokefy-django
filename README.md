# Pokefy

Pokefy is a very simple flutter application for displaying pokemon data obtained from wikidata.

  - Get a list of all the pokemon
  - See detailed informations on wikidata based on the selected pokemon
  - Have fun

### Tech

Pokefy uses a number of open source projects to work properly:

* [Django](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Visual Studio Code](https://code.visualstudio.com/) - a code editor redefined and optimized for building and debugging modern web and cloud applications.
* [Flutter](https://flutter.dev/) - is Google's UI toolkit for crafting beautiful, natively compiled applications for mobile, web, and desktop from a single codebase.

### Installation - Django

Pokefy requires [Python](https://www.python.org/) 3.8 and [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) to work.

Begin by cloning the pokefy-django repository and installing the pipenv requirements.

```sh
> mkdir pokefy
> git clone https://github.com/Pincaptain/pokefy-django.git
> cd pokefy-django
> pipenv install
```

Find your local IP address in order to run the django application locally (https://lifehacker.com/how-to-find-your-local-and-external-ip-address-5833108)

Run the django app locally by navigating to the pokefy-django folder and executing the following line

```sh
> python manage.py runserver your-local-ip-address:80
```

Now you can open up your browser and enter your-local-ip-address and check the API of the web app.

### Installation - Flutter

Due to the fact that I have not deployed my web app you will need to rebuild the whole flutter app after changing the local ip address so instead here is a short video of what the application does.

https://youtu.be/4jbQAbPNdvo

License
----

MIT

**Free Software, Hell Yeah!**