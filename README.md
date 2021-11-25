Website deployed
https://alebrugsilva9.pythonanywhere.com/

IDEA
	The idea of the project was to create a simple front-end page just to show results, but also creating diferents types of troops, as many desired.
	The backend api receives how many troops is the whole army, and a list of different the different type of proof. Returning a JSON, with the name of the troop and how many they are. There is also a second api.

STRUCTURE
	FRONT
		The idea of the front was not too use any framework to be as simple as an HTML. This way it was used embedded js and css on the html file.
	BACK
		The backend was created in python using Flask, since Flask is the perfect framework for simple servers and can be easily implemented.
		In Python it was also used random library and json2html.
		The api returns a JSON /api and /api/pretty returns a table in a string.
		The api receives arguments by post, and the whole math is calculated in the backend.

PROCESS
	FRONT
		The page presents options to fill textfields and choose which type of troop you want in your army, also creating new textfields as you need more fields for troops. Also you can uncheck one troop if you don't a specific type of troop that was already written down.
	END
		After receiving the request, the data is treated (removing empty fields), then randomization using randint from python, using 1 as minimum, and maximum as the number total of troops minus the still remaining types of troops (this way every type will habe at least one troop), the last type of troop is set by the still maximum number possible to this type (filling the whole army).

FILES
To test offline if desired
front.html
style.css
api.py

Python 3.9.2
Flask 2.0.2