## intent:findRestaurantsByCity
<!-- what is my balance -->   <!-- no entity -->
<!-- - how much do I have on my [savings](source_account) --> <!-- entity "source_account" has value "savings" --> 
- hello looking for [restaurants](restaurants:res_syn) located at [city](city:locations)
- please look for [restaurants](restaurants:res_syn) located at [city](city:locations)
- show [restaurants](restaurants:res_syn) located at [city](city:locations)

## intent:bye
- good bye
- bye bye
- see your around
- tye tye

## intent:greet
- hey
- hello
- good morning
- good evening
- sup
- whatsup

## synonym:find_syn
- show
- find
- look

## synonym:locations
- new york
- san francisco
- atlanta
- bonn
- cologne
- frankfurt
- dortmund
- dusseldorf

## synonym:greet_ways
- greetings
- how are you
- whats up
- how are you doing
- how is it going
- good afternoon
- good day
- good night
- are you there
- morning
- how are things going
- are you around
- are you around?

## synonym:res_syn
- restaurants
- places to eat
- where to eat  

## synonym:savings   <!-- synonyms, method 2 -->
- pink pig

## regex:zipcode
- [0-9]{5}

## lookup:currencies   <!-- lookup table list -->
- Yen
- USD
- Euro

<!--## lookup:additional_currencies   no list to specify lookup table file 
path/to/currencies.txt -->