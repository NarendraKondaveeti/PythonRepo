dict.get(key) : Object (Value / None) ni return chestundi. Dictionary lo specified key unda leda ani check chestundi. Key unte aa key yokka value ni return chestundi. Key lekapothe None return chestundi. KeyError exception ivvadu. Original dictionary modify avvadu.

dict.get(key, default) : Object (Value / Default Value) ni return chestundi. Dictionary lo specified key unte aa value ni return chestundi. Key lekapothe manam ichina default value ni return chestundi. KeyError exception ivvadu. Original dictionary modify avvadu.

dict.keys() :Dictionary View Object ni return chestundi. Dictionary lo unna anni keys ni Dictionary View Object ga return chestundi. For loop lo iterate chesthe okkokka key vastundi. Original dictionary modify avvadu.

dict.values() : Dictionary View Object ni return chestundi. Dictionary lo unna anni values ni Dictionary View Object ga return chestundi. For loop lo iterate chesthe okkokka value vastundi. Original dictionary modify avvadu.

dict.items() : Dictionary View Object ni return chestundi. Dictionary lo unna anni (key, value) pairs ni Dictionary View Object ga return chestundi. For loop lo iterate chesthe prathi iteration lo oka (key, value) tuple vastundi. Original dictionary modify avvadu.

dict.update(other_dict) : None ni return chestundi. Other dictionary lo unna key-value pairs ni current dictionary lo add chestundi. Same key already unte existing value update chestundi. Original dictionary ni inplace modify chestundi.

dict.update(key=value) : None ni return chestundi. Keyword arguments ni use chesi dictionary lo new key-value pair add chestundi leka existing key value ni update chestundi. Original dictionary ni inplace modify chestundi.

dict.pop(key) : Object (Removed Value) ni return chestundi. Specified key ni dictionary nundi remove chesi aa key yokka value ni return chestundi. Key dorakakapothe KeyError exception vastundi. Original dictionary ni modify chestundi.

dict.pop(key, default) : Object (Removed Value / Default Value) ni return chestundi. Specified key unte remove chesi value ni return chestundi. Key lekapothe default value ni return chestundi. KeyError exception ivvadu. Original dictionary modify avutundi (key unte matrame).

dict.popitem() : Tuple (key, value) ni return chestundi. Dictionary lo last insert ayina (key, value) pair ni remove chesi tuple ga return chestundi. Dictionary empty unte KeyError exception vastundi. Original dictionary ni modify chestundi.

dict.clear() : None ni return chestundi. Dictionary lo unna anni key-value pairs ni remove chesi empty dictionary ga marchestundi. Original dictionary ni modify chestundi.

dict.copy() : Dictionary (dict) ni return chestundi. Existing dictionary yokka shallow copy ni create chesi return chestundi. Original dictionary modify avvadu. Nested dictionaries unte deep copy kaadu.

dict.setdefault(key) : Object (Value / None) ni return chestundi. Specified key unte aa value ni return chestundi. Key lekapothe aa key ni None value tho add chesi None ni return chestundi. Original dictionary modify avutundi (key lekapothe).

dict.setdefault(key, default) : Object (Value / Default Value) ni return chestundi. Specified key unte existing value ni return chestundi. Key lekapothe key ni dictionary lo add chesi default value assign chesi aa value ni return chestundi. Original dictionary modify avutundi (key lekapothe).

dict.fromkeys(iterable) : Dictionary (dict) ni return chestundi. Iterable (List, Tuple, Set, String...) lo unna values ni keys ga use chesi kotha dictionary create chestundi. Prathi key ki default ga None value assign chestundi. Existing dictionary modify avvadu. Idi class method.

dict.fromkeys(iterable, value) : Dictionary (dict) ni return chestundi. Iterable lo unna values ni keys ga use chesi kotha dictionary create chestundi. Prathi key ki manam ichina same value assign chestundi. Existing dictionary modify avvadu. Idi class method.

📝 Interview Quick Notes
get() vs []
dict.get("key") → Key lekapothe None (leda default value) return chestundi.
dict["key"] → Key lekapothe KeyError exception vastundi.
keys() vs values() vs items()
keys() → Keys ni return chestundi.
values() → Values ni return chestundi.
items() → (key, value) pairs ni return chestundi.

Note: Ee moodu methods Dictionary View Object ni return chestayi, list ni kaadu.

pop() vs popitem()
pop(key) → Given key ni remove chesi value ni return chestundi.
popitem() → Last inserted (key, value) pair ni remove chesi tuple ga return chestundi.

update() vs setdefault()
update() → Existing value ni direct ga add/update chestundi.
setdefault() → Key lekapothe matrame add chestundi; key unte existing value ni marchadu.

copy()
Shallow Copy create chestundi.
Nested dictionaries unte inner objects share avutayi.

⭐ Important Note
Dictionary Mutable: Dictionary methods (update(), pop(), popitem(), clear(), setdefault()) original dictionary ni inplace modify chestayi. Anduke ekkuva methods None leka removed value ni return chestayi.

get(), keys(), values(), items(), copy(), fromkeys() original dictionary ni modify cheyyavu. Avi value, view object, leka kotha dictionary ni return chestayi.