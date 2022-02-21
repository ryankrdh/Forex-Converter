### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

1. Python can be used to develop the backend part of a web application. Javascript can be used to develop both the backend and the front end of the application.
2. Python uses indentation to define code blocks while javascript uses curly braces.
3. Python does not need to state var or let to create variables.

python example:

> x = 5

javascript example:

> const x = 5;  
> let x = 5;

4.  Python variable names are conventionally done in **snake_case** while javascript is done in **camelCase**

<br>

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

1st method:

> dict[letter] = dict.get(letter, 0)

2nd method:

> dict.setdefault('c', 0)

  <br>

- What is a unit test?

  A way of testing a small piece of code that can be isolated in a system.

  <br>

- What is an integration test?

  A way of testing multiple individual modules as a group.

  <br>

- What is the role of web application framework, like Flask?

  Main role of Flask is to allow us developers to build up web applications without having to write low-level codes.

  <br>

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  It's easier to recognize for users or viewers with accessibility issues. Easier search engine crawling due to simplicity. Also it is hard for users/developers to remember or type in url.

  <br>

- How do you collect data from a URL placeholder parameter using Flask?

- How do you collect data from the query string using Flask?

- How do you collect data from the body of the request using Flask?

- What is a cookie and what kinds of things are they commonly used for?

- What is the session object in Flask?

- What does Flask's `jsonify()` do?
