list.append(item) :

None ni return chestundi. List last lo okka item ni add chestundi. Original list ni modify chestundi. Kotha list create cheyyadu. Item edaina data type ayyi undochu (int, str, list, tuple...).

list.extend(iterable) :

None ni return chestundi. Iterable (List, Tuple, Set, String...) lo unna prathi value ni okkokatiga iterate chesi list last lo add chestundi. Original list ni modify chestundi. Kotha list create cheyyadu.

list.insert(index, item) :

None ni return chestundi. Given index position lo item ni insert chestundi. Aa index nundi existing values anni right side ki shift avutayi. Original list ni modify chestundi.

list.remove(value) :

None ni return chestundi. List lo specified value first occurrence ni search chesi remove chestundi. Value dorakakapothe ValueError exception vastundi. Original list ni modify chestundi.

list.pop() :

Object (Removed Item) ni return chestundi. Default ga list last item ni remove chesi aa item ni return chestundi. Original list ni modify chestundi.

list.pop(index) :

Object (Removed Item) ni return chestundi. Given index lo unna item ni remove chesi aa item ni return chestundi. Invalid index iste IndexError exception vastundi. Original list ni modify chestundi.

list.clear() :

None ni return chestundi. List lo unna anni items ni remove chesi empty list ga marchestundi. Original list ni modify chestundi.

list.copy() :

List ni return chestundi. Existing list yokka shallow copy ni create chesi return chestundi. Original list modify avvadu. Nested list unte deep copy kaadu.

list.index(value) :

Integer (int) ni return chestundi. List lo specified value first occurrence index ni return chestundi. Value dorakakapothe ValueError exception vastundi.

list.index(value, start) :

Integer (int) ni return chestundi. Given start index nundi search start chesi first matching value index ni return chestundi. Value dorakakapothe ValueError exception vastundi.

list.index(value, start, end) :

Integer (int) ni return chestundi. Given start nundi end varaku search chesi first matching value index ni return chestundi. Value dorakakapothe ValueError exception vastundi.

list.count(value) :

Integer (int) ni return chestundi. List lo specified value enni sarlu undo count chesi aa count ni return chestundi. Original list modify avvadu.

list.sort() :

None ni return chestundi. List lo unna items ni ascending order lo sort chestundi. Original list ni inplace modify chestundi. Kotha list create cheyyadu.

list.sort(reverse=True) :

None ni return chestundi. List lo unna items ni descending order lo sort chestundi. Original list ni inplace modify chestundi.

list.sort(key=function) :

None ni return chestundi. Given key function return chese value base meeda list ni sort chestundi. Original list ni inplace modify chestundi.

list.reverse() :

None ni return chestundi. List lo unna items order ni reverse chestundi. Idi sort cheyyadu. Existing order ni reverse matrame chestundi. Original list ni inplace modify chestundi.

📝 Interview Quick Notes
append() vs extend()
append() → Oka item ni add chestundi.
extend() → Iterable lo unna anni items ni separate ga add chestundi.

remove() vs pop()
remove() → Value ni remove chestundi.
pop() → Index base meeda remove chesi removed item ni return chestundi.

sort() vs sorted()
list.sort() → Original list ni modify chestundi. None return chestundi.
sorted(list) → Kotha sorted list ni return chestundi. Original list modify avvadu.

reverse() vs sort(reverse=True)
reverse() → Existing order ni reverse chestundi.
sort(reverse=True) → Descending order lo sort chestundi.


⭐ Important Note
List Mutable: 
List methods (append(), extend(), insert(), remove(), pop(), clear(), sort(), reverse()) ekkuvaga original list ni modify (in-place) chestayi. Anduke chala methods None return chestayi.

copy(), count(), index() matrame original list ni modify cheyyavu; avi value leka kotha object ni return chestayi.