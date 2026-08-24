OOPs (Object-Oriented Programming) anedi programming lo code ni objects and classes chuttu organize chese programming approach. Python lo automation frameworks build chestunnappudu code ni reusable, maintainable, structured ga organize cheyyadaniki OOPs chala important.

Automation Testing context lo especially Page Object Model (POM), Page Classes, Test Data Classes, Utility Classes, API Client Classes, Configuration Classes, Fixtures lantivi design cheyyadaniki OOP concepts use chestam.

1. Class:
Class ante blueprint / template; object ela undali, danilo ye data and behavior undali ane structure ni define chestundi.
Class lo attributes/data and methods/behavior ni define chestam.
Class create chesinappudu specific object kosam instance memory allocate avvadu.
Oka class nunchi multiple objects create cheyyachu; prati object ki separate instance state undachu.
Class vs Function: Function mainly oka task/logic ni perform chestundi; class related data + related methods + object state ni oka reusable structure lo organize chestundi.
Example: LoginPage class lo page, username lanti state tho paatu login(), logout(), verify_login() lanti related methods maintain cheyyachu.
Only functions use chesthe same data ni multiple functions ki repeatedly pass cheyyalsi ravachu; class/object approach lo aa state ni object lo maintain chesi multiple methods reuse cheyyachu.
Automation lo Page Objects, API clients, browser managers, configuration handlers lanti components ni classes ga design chestam.
2. Object:
Object ante class nunchi create chesina real instance/entity.
Class define chesina structure ni follow chestu object create avutundi.
Object ki own instance data/state untundi.
Same class nunchi create chesina two objects, same methods ni use chesina, own state/data base chesukoni different output/behavior ivvachu.
Example:
login_admin = LoginPage("admin")
login_readonly = LoginPage("readonly")
Ikkada LoginPage → class; LoginPage(...) → object creation; login_admin, login_readonly → aa objects ni refer chese reference variables.
Object vs Reference Variable: Object actual instance; reference variable aa object ni access/use cheyyadaniki use chese reference/name.
login_admin.login() call chesthe aa referenced object yokka login() method execute avutundi.
Automation lo different browser sessions/pages/users ni separate objects ga maintain cheyyachu.
3. Object Reference:
Object create chesina tarvata, aa object ni access cheyyadaniki variable/reference use chestam.
Example:
login_page = LoginPage(page)
LoginPage(page) → object create chestundi.
login_page → aa object ni refer chestundi.
login_page.login() → referenced object meeda method execute chestundi.
Oka reference ni inko variable ki assign chesthe rendu references same object ni refer cheyyachu.
Example:
a = LoginPage()
b = a
Ikkada a and b rendu same object ni refer chestayi; b ద్వారా change chesina object state a ద్వారా kuda observe cheyyachu.
Idi aliasing concept ki basic example.
4. Constructor __init__():
__init__() object create ayina taruvata automatically execute ayye initialization method.
Object ki required initial data/state/dependencies ni initialize cheyyadaniki use chestam.
Example:
class LoginPage:
    def __init__(self, page):
        self.page = page
Ikkada incoming page object ni current LoginPage object state lo store chestunnam.
Constructor lo validation, defaults, dependencies setup, configuration initialization lanti work kuda cheyyachu.
__init__() ni normal usage lo manual ga call cheyyalsina avasaram undadu.
Technical ga object creation process __new__() stage ni kuda involve chestundi; __init__() already-created instance ni initialize chestundi.
5. self:
self ante current object ni refer chese reference.
self.username → current object yokka username.
self.page → current object lo stored Playwright page.
self.login() → current object yokka method.
obj1.login() call ayithe aa execution lo self → obj1.
obj2.login() call ayithe self → obj2.
Anduke same instance method multiple objects tho different state meeda work cheyyagaladu.
self Python keyword kaadu; self ane name conventionally use chestam.
6. Instance Variable:
Instance variable ante particular object ki own data/state.
Usually self.variable form lo create chestam.
Same class objects ki same variable name unna different values undachu.
Example:
self.username
self.page
self.token
user1.username = "admin" and user2.username = "readonly" ayithe rendu separate object states.
Oka object instance variable value change chesina vere object value automatically change avvadu.
Automation lo page, driver, current user, token, environment-specific state lanti values instance variables ga maintain cheyyachu.
7. Instance Method:
Instance method ante current object state ni use chesi behavior perform chese method.
Usually first parameter self.
Method implementation class lo same ga define chestam.
Kani current object data different ayithe execution/output/behavior different ga undachu.
Example:
def login(self):
    if self.role == "admin":
        ...
Same login() method different objects lo different self.role value ni use chesukoni different path execute cheyyachu.
Automation Page Object methods usually instance methods.
8. Encapsulation:
Encapsulation ante related data + related methods ni oka class lo bundle cheyyadam.
Data ni handle chese operations same class lo maintain chestam.
Automation lo locators + page actions + page-level validations ni same Page Class lo maintain cheyyadam practical example.
Test file lo login_page.login() ani use chestam; actual locator and interaction details Page Class lo remain avutayi.
Encapsulation valla changes localized ga untayi; locator change ayithe test cases anni modify cheyyalsina avasaram takkuva.
Python lo strict private access Java laga direct restriction kaadu; _name convention and __name name-mangling available.
9. Inheritance:
Inheritance ante parent class functionality ni child class reuse/extend cheyyadam.
Common functionality ni duplicate ga rayakunda parent class lo maintain chestam.
Example:
class LoginPage(BasePage):
    pass
LoginPage inherited methods ni use cheyyagaladu.
Child own methods add cheyyachu or parent methods override cheyyachu.
Automation lo BasePage common actions; LoginPage, DashboardPage, SearchPage specific behavior.
Inheritance "is-a" relationship ni model cheyyadaniki suitable.
Unnecessary deep inheritance framework complexity penchutundi; reusable composition kuda consider cheyyali.
10. Single Inheritance:
One parent → One child.
Example: LoginPage(BasePage).
Simple and commonly used pattern.
Common parent behavior child directly reuse chestundi.
11. Multilevel Inheritance:
GrandParent → Parent → Child.
Example: BasePage → WebPage → LoginPage.
Child inherited chain dwara higher-level behavior ni kuda access cheyyachu.
Too many levels unte code trace/debug cheyyadam difficult avvachu.
12. Multiple Inheritance:
Multiple parents → One child.
Example:
class TestPage(BasePage, ApiHelper):
    pass
Child two parent classes functionality ni inherit cheyyachu.
Same method multiple parents lo unte MRO decide chestundi.
Mixins/utilities lanti controlled use cases lo useful; unnecessary ga use cheyyadam avoid cheyyadam better.
13. Hierarchical Inheritance:
One parent → Multiple children.
Example:
BasePage
 ├── LoginPage
 ├── DashboardPage
 └── SearchPage
Parent common functionality multiple pages reuse chestayi.
POM framework lo natural pattern.
14. Method Overriding:
Child class parent class lo unna same method ni own implementation tho redefine chesthe overriding.
Child object meeda aa method call chesthe child version execute avutundi.
Parent logic kuda kavali ante super().method() use cheyyachu.
Runtime polymorphism ki idi practical base.
Automation lo environment/page-specific behavior customize cheyyadaniki use cheyyachu.
15. Polymorphism:
Polymorphism ante same method/interface different objects lo different behavior provide cheyyadam.
Caller same interface use chestadu; actual behavior current object implementation batti change avvachu.
Method overriding Python lo common example.
Example concept: browser.launch() same interface; different browser implementations different behavior.
Automation framework lo common interfaces or common method names maintain cheyyadaniki useful.
16. Method Overloading:
Traditional overloading ante same method name + different parameter signatures.
Python lo Java/C++ laga direct traditional overloading support cheyyadu.
Same name tho second definition rayithe previous definition replace avutundi.
Similar flexible behavior kosam default parameters, *args, **kwargs use cheyyachu.
Overloading vs Overriding: Overloading → parameter variations concept; overriding → child class parent method ni redefine cheyyadam.
17. Abstraction:
Abstraction ante unnecessary implementation details ni hide chesi required interface/functionality ni expose cheyyadam.
Automation test:
login_page.login()
Test ki locator, explicit wait, click sequence, error handling internal details avasaram ledu.
Ivanni Page Class implementation lo hide cheyyachu.
Python formal abstraction kosam ABC and @abstractmethod use cheyyachu.
Abstraction maintainability and separation of responsibilities improve chestundi.
18. Encapsulation vs Abstraction:
Encapsulation → Data + related methods ni bundle and organize cheyyadam.
Abstraction → Unnecessary implementation details ni hide chesi required interface ni expose cheyyadam.
POM lo same design lo rendu concepts kalisi kanipinchachu; kani renditi purpose same kaadu.
19. super():
super() child class nunchi parent class functionality ni access cheyyadaniki use chestam.
super().__init__() → parent constructor call.
super().login() → parent method call.
Child own logic + parent common logic combine cheyyachu.
Multiple inheritance lo super() MRO chain ni follow chestundi; direct parent class name call kanna cooperative inheritance designs lo better.
20. Class Variable:
Class variable ante class-level common data.
Class body lo define chestam.
class Employee:
    company = "ABC"
Multiple objects same class variable ni access cheyyagalavu.
Shared state kosam use cheyyachu.
Mutable class variables like list/dict unintended shared-state bugs create cheyyachu; careful ga use cheyyali.
21. Instance Variable vs Class Variable:
Instance variable → each object ki own state.
Class variable → class-level shared state.
self.username → object-specific.
company → common.
Object attribute same name tho set chesthe instance value class attribute ni shadow cheyyachu.
Requirement object-specific aa, common aa ani decide chesi correct variable type choose cheyyali.
22. Class Method @classmethod:
Class method first parameter cls.
cls current class ni refer chestundi.
Class-level data/config operations kosam useful.
Alternative constructors implement cheyyadaniki common.
@classmethod
def from_config(cls, data):
    return cls(data["name"])
Instance method lo self; class method lo cls — main difference.
23. Static Method @staticmethod:
Static method ki self/cls automatic ga pass avvavu.
Object/class state direct ga avasaram leni but class domain ki logically related utility logic kosam use chestam.
Example: email/date validation, formatting, conversion.
Object-specific state kavali ante instance method better; class-level state kavali ante class method better.
24. MRO:
MRO = Method Resolution Order.
Multiple inheritance lo Python method/attribute ni ye class nunchi ye order lo search cheyyalo decide chestundi.
ClassName.mro() or ClassName.__mro__ tho inspect cheyyachu.
Python C3 Linearization algorithm use chestundi.
Same method multiple parents lo unte MRO first matching implementation ni determine chestundi.
super() kuda MRO chain ni follow chestundi.
25. Composition vs Inheritance:
Inheritance → is-a relationship.
Composition → has-a relationship.
Example: LoginPage(BasePage) → inheritance.
LoginPage lo BrowserManager object store cheyyadam → composition.
Automation frameworks lo composition often useful because components ni loosely combine cheyyachu without creating deep inheritance trees.
Design choose chesetappudu reuse kosam inheritance automatic ga choose cheyyakunda relationship correct ga unda ani think cheyyali.
26. POM lo OOP Practical Mapping:
Class → LoginPage
Object → LoginPage(page) nunchi create ayina instance
Reference Variable → login_page
Constructor → __init__(self, page)
Instance Variable → self.page
Instance Method → login()
Encapsulation → locators + page actions same Page Class lo
Abstraction → test file ki internal locator/wait implementation hide
Inheritance → LoginPage(BasePage)
Overriding → child page custom implementation
super() → parent constructor/common method reuse
Polymorphism → common method/interface, different implementations
Composition → page/object lo another helper/client object use cheyyadam
27. Real Automation Design Thinking:
Oka class create cheyyali ante first “Ee class responsibility enti?” ani decide cheyyali.
Oka class lo unrelated functionality anni dump cheyyakudadhu; single responsibility maintain cheyyadam better.
Object ki state avasaram unte instance variables use cheyyali.
Same data all objects ki common ayithe class variable consider cheyyali.
Common child behavior unte inheritance consider cheyyali; independent reusable components unte composition consider cheyyali.
Test case should focus on business flow + assertions; page implementation, locators, waits, low-level interactions helper/Page classes lo maintain cheyyadam better.
OOPs goal syntax memorize cheyyadam kaadu; reusable, maintainable, scalable automation framework design cheyyadam.

![alt text](image.png)