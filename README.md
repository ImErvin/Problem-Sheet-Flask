# Problem-Sheet: *Flask*
Answers to the **Flask Problem Sheet** for *Data Representation and Querying*.

**Steps**
  1. Create a git repository for this problem sheet, and make a commit after completing each
    question.
  2. Go to the flask website, copy and paste the Flask is Fun example script into a file called
    hello.py. Run the script, and open the URL for the web server in your browser.
  3. Create a subdirectory called static, and create a file called index.html in it. Copy and
    paste the Bootstrap basic template into index.html [1]. Fix the CSS and JS links, rerun
    the python script and access index.html from your browser.
  4. Read the Routing section of the Flask documentation [3]. Add a route at /name that
    responds with the text: “Your name is”. Add a variable to the end of the route called
    name and have it appended to the end of the response.
  5. Add a form to index.html with a single text box with id name and with the method
    GET. Set the form action to ”/name” Add a submit button. In hello.py, change the
    ”/name” route to accept the name variable as a URL encoded GET variable. Run the
    server and test.
  6. Change the form in the previous question to perform an AJAX call. Instead of having
    the page refresh when the Submit button is clicked, have it perform the AJAX call and
    output the result to a disabled textarea in index.html.
  7. Replace the GET method of the previous question with the POST method.
  
**References**
  >[1] Bootstrap. Bootstrap: Getting started. </br>
  >[2] Armin Ronacher. Flask (a python microframework).</br>
  >[3] Armin Ronacher. Flask quickstart: Routing.</br>
