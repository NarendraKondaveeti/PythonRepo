string.upper() :

String (str) ni return chestundi. String lo unna anni lowercase alphabet characters ni uppercase alphabet characters ga marchi kotha string ni return chestundi. Numbers, spaces, special characters ni marchadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.lower() :

String (str) ni return chestundi. String lo unna anni uppercase alphabet characters ni lowercase alphabet characters ga marchi kotha string ni return chestundi. Numbers, spaces, special characters ni marchadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.title() :

String (str) ni return chestundi. String lo unna prathi word first alphabet ni uppercase ga, migatha alphabets ni lowercase ga marchi kotha string ni return chestundi. Numbers, spaces, special characters ni marchadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.capitalize() :

String (str) ni return chestundi. String first alphabet ni uppercase ga, migatha alphabets anni lowercase ga marchi kotha string ni return chestundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.swapcase() :

String (str) ni return chestundi. String lo unna uppercase alphabet characters ni lowercase ga, lowercase alphabet characters ni uppercase ga marchi kotha string ni return chestundi. Numbers, spaces, special characters ni marchadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.strip() :

String (str) ni return chestundi. String beginning mariyu ending lo unna whitespace characters (spaces, tabs, new lines) ni remove chesi kotha string ni return chestundi. Middle lo unna spaces ni remove cheyyadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.strip(chars) :

String (str) ni return chestundi. String beginning mariyu ending lo unna specified characters ni remove chesi kotha string ni return chestundi. Middle lo unna characters ni remove cheyyadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.lstrip() :

String (str) ni return chestundi. String left side beginning lo unna whitespace characters ni remove chesi kotha string ni return chestundi. Right side whitespace ni remove cheyyadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.rstrip() :

String (str) ni return chestundi. String right side ending lo unna whitespace characters ni remove chesi kotha string ni return chestundi. Left side whitespace ni remove cheyyadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.replace(old, new) :

String (str) ni return chestundi. String lo unna old value ni new value tho replace chesi kotha string ni return chestundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.replace(old, new, count) :

String (str) ni return chestundi. String lo unna old value ni new value tho replace chesi kotha string ni return chestundi. count parameter iste, left nundi start chesi antha sarlu matrame replace chestundi. count ivvakapothe matching values anni replace chestundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.split() :

List ni return chestundi. String ni whitespace characters (spaces, tabs, new lines) daggara split chesi list ga return chestundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.split(separator) :

List ni return chestundi. String ni specified separator daggara split chesi list ga return chestundi. Separator output list lo undadu. Original string ni modify cheyyadu. Endukante strings immutable.

string.split(separator, maxsplit) :

List ni return chestundi. String ni specified separator daggara split chesi list ga return chestundi. maxsplit parameter iste antha sarlu matrame split chestundi. Migatha string last element ga untundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.rsplit() :

List ni return chestundi. split() lagaane work chestundi. Kani splitting right side nundi start chestundi. Original string ni modify cheyyadu. Endukante strings immutable.

string.join(iterable) :

String (str) ni return chestundi. Iterable (List, Tuple, Set...) lo unna string values madhya separator ni add chesi oka kotha string ni create chesi return chestundi. Iterable lo unna values anni strings ayyi undali.

string.find(value) :

Integer (int) ni return chestundi. String lo specified value first occurrence index ni search chesi return chestundi. Value dorakakapothe -1 return chestundi. Exception ivvadu. Original string ni modify cheyyadu.

string.find(value, start) :

Integer (int) ni return chestundi. Given start index nundi search start chesi first matching value index ni return chestundi. Value dorakakapothe -1 return chestundi.

string.find(value, start, end) :

Integer (int) ni return chestundi. Given start nundi end varaku search chesi first matching value index ni return chestundi. Value dorakakapothe -1 return chestundi.

string.rfind(value) :

Integer (int) ni return chestundi. String ni right side nundi search chesi last occurrence index ni return chestundi. Value dorakakapothe -1 return chestundi.

string.index(value) :

Integer (int) ni return chestundi. String lo specified value first occurrence index ni return chestundi. Value dorakakapothe ValueError exception vastundi.

string.rindex(value) :

Integer (int) ni return chestundi. String ni right side nundi search chesi last occurrence index ni return chestundi. Value dorakakapothe ValueError exception vastundi.

string.count(value) :

Integer (int) ni return chestundi. String lo specified value enni sarlu undo count chesi aa count ni return chestundi. Original string ni modify cheyyadu.

string.startswith(prefix) :

Boolean (True/False) value ni return chestundi. String beginning lo specified prefix unda leda ani check chestundi. Prefix match aithe True, lekapothe False return chestundi. Original string ni modify cheyyadu.

string.startswith(prefix, start) :

Boolean (True/False) value ni return chestundi. Given start index nundi string beginning ga consider chesi specified prefix unda leda ani check chestundi.

string.startswith(prefix, start, end) :

Boolean (True/False) value ni return chestundi. Given start nundi end varaku unna substring beginning lo specified prefix unda leda ani check chestundi.

string.endswith(suffix) :

Boolean (True/False) value ni return chestundi. String ending lo specified suffix unda leda ani check chestundi. Match aithe True, lekapothe False return chestundi.

string.isalpha() :

Boolean (True/False) value ni return chestundi. String lo alphabet characters matrame unnaya leda ani check chestundi. Numbers, spaces, special characters lo okkati unna False return chestundi. Alphabet letters matrame unte True return chestundi. Original string ni modify avvadu.

string.isdigit() :

Boolean (True/False) value ni return chestundi. String lo digits (0–9) matrame unnaya leda ani check chestundi. Letters, spaces, special characters, decimal point (.), minus (-) lo edaina unna False return chestundi.

string.isalnum() :

Boolean (True/False) value ni return chestundi. String lo alphabets mariyu digits matrame unnaya leda ani check chestundi. Spaces leka special characters unte False return chestundi.

string.isspace() :

Boolean (True/False) value ni return chestundi. String lo whitespace characters (spaces, tabs, new lines) matrame unnaya leda ani check chestundi. Vere character okkati unna False return chestundi. Empty string ki False return chestundi.

string.islower() :

Boolean (True/False) value ni return chestundi. String lo unna alphabet characters anni lowercase lo unnaya leda ani check chestundi. Numbers, spaces, special characters ni ignore chestundi. Alphabet letters anni lowercase lo unte True, oka uppercase alphabet unna False return chestundi.

string.isupper() :

Boolean (True/False) value ni return chestundi. String lo unna alphabet characters anni uppercase lo unnaya leda ani check chestundi. Numbers, spaces, special characters ni ignore chestundi. Alphabet letters anni uppercase lo unte True, oka lowercase alphabet unna False return chestundi.

string.istitle() :

Boolean (True/False) value ni return chestundi. String lo prathi word first alphabet uppercase lo, migatha alphabets lowercase lo unnaya leda ani check chestundi. Aa format follow aithe True, lekapothe False return chestundi. Original string ni modify cheyyadu.