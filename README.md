cloudcomputingH2
================

Cloud Computing Homework 2: Docker and Web Services

### Spirit Animal Generator with a Street Perspective

#### Usage
Enter http://127.0.0.1:8080/spirit?animals= into your browser, adding an animal to the end of the url as the GET parameter (*i.e. http://127.0.0.1:8080/spirit?animals=Bear*)
A JSON object is returned, containing a spiritanimal.info description and urbandictionary.com meaning and examples for the animal.

##### The GET parameter options are:
- *Bear*
- *Butterfly*
- *Cat*
- *Coyote*
- *Crow*
- *Deer*
- *Dolphin*
- *Dragonfly*
- *Fox*
- *Frog*
- *Hawk*
- *Horse*
- *Hummingbird*
- *Lion*
- *Owl*
- *Panda*
- *Sheep*
- *Snake*
- *Spider*
- *Tiger*
- *Turtle*
- *Wolf*
- *Whale*
- *Panther*

#### Example
*Url Input:* 

`http://127.0.0.1:8080/spirit?animals=Coyote`

*Browser Output:*
`{"Coyote": {"urban_example": "\nJuan 1: Did you make it across with a coyote?\rJuan 2: No acrossed on my own this time.\n", "urban_meaning": "\nA person who smuggles immigrants into America and they come from any given country for a small fee to cross into the United States. They make very good money doing it. (Average per person $1200)\n", "spirit_description": "The coyote totem is strikingly paradoxical and is hard to categorize. Its a teacher of hidden wisdom with a sense of humor, so the messages of the coyote spirit animal may paradoxically appear in the form of a joke or trickery. Dont be tricked by the foolish appearances. The spirit of the coyote may remind you to not take things too seriously and bring more balance between wisdom and playfulness."}}`

#### Package Requirements
[Requests](http://docs.python-requests.org/en/latest/)

*A simple HTTP library for Python*

`pip install requests`


[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)

*A Python screen-scraping library*

`pip install beautifulsoup4`

#### Possible Future Work
1. Dynamic HTML/Javascript user interface with images.
2. More choices of spirit animals.
3. Multiple Urban Dictionary meanings/examples.
4. Pull data from Youtube/Google/Wikipedia.
5. Ability to save output or send through email.