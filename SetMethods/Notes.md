set.add(item) :

None ni return chestundi. Set lo specified okka item ni add chestundi. Item already unte malli add cheyyadu. Duplicate values allow cheyyadu. Original set ni inplace modify chestundi.

set.update(iterable) :

None ni return chestundi. Iterable (List, Tuple, Set, String...) lo unna values ni okkokatiga iterate chesi set lo add chestundi. Duplicate values automatic ga ignore avutayi. Original set ni inplace modify chestundi.

set.remove(item) :

None ni return chestundi. Specified item ni set nundi remove chestundi. Item dorakakapothe KeyError exception vastundi. Original set ni inplace modify chestundi.

set.discard(item) :

None ni return chestundi. Specified item ni set nundi remove chestundi. Item dorakakapothe emi cheyyadu, exception kuda ivvadu. Original set ni inplace modify chestundi.

set.pop() :

Object (Removed Item) ni return chestundi. Set nundi oka item ni remove chesi aa item ni return chestundi. Ye item remove avutundo guarantee undadu, endukante set unordered. Empty set unte KeyError exception vastundi. Original set ni inplace modify chestundi.

set.clear() :

None ni return chestundi. Set lo unna anni items ni remove chesi empty set ga marchestundi. Original set ni inplace modify chestundi.

set.copy() :

Set ni return chestundi. Existing set yokka shallow copy ni create chesi return chestundi. Original set modify avvadu.

set.union(other_set) :

Set ni return chestundi. Rendu leka ekkuva sets lo unna unique values anni kalipi kotha set ni return chestundi. Original sets modify avvavu.

set.intersection(other_set) :

Set ni return chestundi. Rendu sets lo common ga unna values matrame kotha set ga return chestundi. Original sets modify avvavu.

set.difference(other_set) :

Set ni return chestundi. First set lo undi, second set lo leni values ni kotha set ga return chestundi. Original sets modify avvavu.

set.symmetric_difference(other_set) :

Set ni return chestundi. Rendu sets lo common values ni remove chesi, common kaani unique values matrame kotha set ga return chestundi. Original sets modify avvavu.

set.intersection_update(other_set) :

None ni return chestundi. Set ni common values matrame unde laga update chestundi. Original set ni inplace modify chestundi.

set.difference_update(other_set) :

None ni return chestundi. Other set lo unna common values ni current set nundi remove chestundi. Original set ni inplace modify chestundi.

set.symmetric_difference_update(other_set) :

None ni return chestundi. Common values ni remove chesi unique values tho current set ni update chestundi. Original set ni inplace modify chestundi.

set.isdisjoint(other_set) :

Boolean (True / False) value ni return chestundi. Rendu sets lo okka common value kuda lekapothe True return chestundi. Oka common value aina unte False return chestundi. Original sets modify avvavu.

set.issubset(other_set) :

Boolean (True / False) value ni return chestundi. Current set lo unna anni values other set lo kuda unte True return chestundi. Leka pothe False return chestundi.

set.issuperset(other_set) :

Boolean (True / False) value ni return chestundi. Other set lo unna anni values current set lo unte True return chestundi. Leka pothe False return chestundi.

📝 Interview Quick Notes
remove() vs discard()
remove() → Item lekapothe KeyError exception vastundi.
discard() → Item lekapothe exception ivvadu.
union() vs update()
union() → Kotha set ni return chestundi. Original set modify avvadu.
update() → Original set ni inplace modify chestundi.
intersection() vs intersection_update()
intersection() → Kotha set ni return chestundi.
intersection_update() → Original set ni inplace modify chestundi.
difference() vs difference_update()
difference() → Kotha set ni return chestundi.
difference_update() → Original set ni inplace modify chestundi.
symmetric_difference() vs symmetric_difference_update()
symmetric_difference() → Kotha set ni return chestundi.
symmetric_difference_update() → Original set ni inplace modify chestundi.

⭐ Important Note

Set Mutable & Unordered:
Set duplicates allow cheyyadu.
Set indexing support cheyyadu.
Set unordered kabatti pop() ye item remove chestundo fixed ga cheppalem.
add(), update(), remove(), discard(), pop(), clear(), intersection_update(), difference_update(), symmetric_difference_update() methods original set ni inplace modify chestayi.
union(), intersection(), difference(), symmetric_difference(), copy() methods original set ni modify cheyyavu; avi kotha set ni return chestayi.