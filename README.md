## HTTP lab with `requests`

Use the requests library to interact with two APIs:    
* [api.adviceslip.com](https://api.adviceslip.com/)
  * Request 50 different advice slips.
  * Are there any duplicates? 
  * If so, what is the most frequent and how many times does it appear?    
* [detectlanguage.com](https://detectlanguage.com/documentation)
  * Provides an API that takes a POST requests with a sample of text 
    and returns a prediction of the language in which that text is written
  * Requires an API key (check Slack).
  * Submit each of the language samples in `main.py` in a POST request.
  * Of this list of samples, what language appears the most often 
    and which samples are in that language?    

<hr>
Other notes:

* You can change the code however you'd like, but you should be able to complete the lab by filling in only the sections marked `[FILL IN HERE]`.
* Throughout the lab, the `requests` [docs](http://docs.python-requests.org/en/master/) may be helpful.
* The language sample strings must be passed to the `requests` get method as an argument to the `params` parameter.    
   Eg:
   ```r = requests.get("<url>", params="q=Hello+world")```
