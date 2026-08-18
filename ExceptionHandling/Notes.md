Exception: Exception anedi program execution time (Runtime) lo jarige unexpected situation. Ee situation valla normal program execution interrupt avuthundi. Python aa situation ni Exception Object ga create chesi, danini handle cheyyakapothe program execution ni stop chestundi.

Shortly : "Exception ante Runtime lo program normal execution ni interrupt chese unexpected event."

Error vs Exception: -
Error:
    Error ante program execute avvakunda chese problem.
    Examples: 
    Syntax Error, Indentation Error
    Python code execute cheyyadaniki mundhe detect chestundi, Program start avvadu.

Exception: 
    Exception ante program already execute avuthundi.
    Execution madhyalo unexpected situation vastundi.
    Examples: 
    File Not Found, Division by Zero, Invalid Dictionary Key, API Timeout
    Program start avuthundi, Execution madhyalo stop avuthundi.

Main Difference: 
    Error: Program execution start kakamundhe detect avuthundi.
    Exception: Program execution start ayyaka runtime lo detect avuthundi.

Exception enduku vastundi? Python program external resources tho work chestundi.
    Examples: Files, Database, API, Browser, Network, JSON, User Input
    Veetilo expected value rakapothe exception generate avuthundi.
    Kabatti Exception ante Python mistake kaadu, Most of the time Unexpected Runtime Situation.

Python Exception ni internally ela handle chestundi?
Suppose: number = 10 / 0
Python internally almost ila think chestundi.
    Program execute chestundi.
    Division operation execute chestundi.
    Denominator check chestundi.
    Zero detect chestundi.
    ZeroDivisionError Exception Object create chestundi.
    Exception handler kosam search chestundi.
    Handler dorikithe, Exception handle chestundi, Program terminate chestundi
    Important Point: Python direct ga program ni stop cheyyadu, First Exception Object create chestundi, Tarvata Handler unda ani check chestundi.

    Exception Handling ante enti?
    Runtime lo vachina Exception ni properly handle chesi, Program ni unexpected ga terminate kakunda continue cheyyadam.

    Shortly: Exception Handling ante Runtime Exception ni capture chesi, program crash kakunda handle cheyyadam.

    Automation Testing lo ekkada use chestaru?
        Almost every automation framework lo
            File Handling: JSON file lekapothe, CSV file lekapothe, Report file open kakapothe.
            API Automation: API Timeout, 401 Unauthorized, 500 Internal Server Error, Invalid Response.
            Playwright: Element kanapadakapothe, Page load kakapothe, Browser close aipothe, Locator invalid ayithe.
            JSON: Invalid JSON, Missing Key, Wrong Data Type.
    
    Real-Time Enterprise Purpose:
        Exception Handling main purpose:
            Program ni
            Crash kakunda
            Gracefully handle cheyyadam.
            Automation execution continue avvadam.
            Logs generate avvadam.
            Reports complete avvadam.
            Cleanup execute avvadam.

Interview Explanation: Exception is an unexpected runtime event that interrupts the normal flow of program execution. Python creates an Exception Object whenever such a situation occurs. Exception Handling is the process of catching and handling that exception so that the program can continue executing gracefully instead of terminating unexpectedly. (Exception ante Runtime lo unexpected situation. Python aa situation ni Exception Object ga represent chestundi. Program terminate cheyyadaniki mundu, aa Exception ni handle cheyyadaniki handler kosam search chestundi. Handler unte Exception handle avuthundi. Lekapothe program terminate avuthundi.)

try ante enti?
try anedi Python keyword. Idi exception ravachu ani anukune code block ni define cheyyadaniki use chestaru, try exception ni handle cheyyadu.
try yokka responsibility: e code execute cheyyi. Exception vaste Python ki telusu ikkada handle cheyyali ani, Kabatti try ante, Exception possible unna code ni monitor cheyyadaniki use chese block.

except ante enti?
except anedi Python keyword, Idi try block lo vachina exception ni catch chesi handle cheyyadaniki use chestaru.

Shortly: try -> Exception detect -> except -> Handle

Basic Syntax:
try:
    # Exception ravachu ani expect chese code
except:
    # Exception ni handle chese code

try(⭐ Mandatory): Exception ravachu ani anukune code.
except(⭐ Mandatory): Exception vaste execute avuthundi.

Scenario 1: try block execution start chestundi -> Statements one by one execute chestundi -> try complete -> except skip -> Remaining code execute.

Scenario 2: try execute -> Exception detect -> Exception Object create -> Matching except search -> except execute -> Remaining program continue.

Important Rule: "try" block lo Exception vachina line daggara execution stop avuthundi, Aa line tarvata try block lo unna remaining statements execute avvavu, Control direct ga "except" ki transfer avuthundi.

Interview Explanation: "try is a Python keyword used to wrap code that may raise an exception during runtime. If an exception occurs, Python creates an Exception Object and immediately transfers control to the matching except block, where the exception is handled. If no exception occurs, the except block is skipped."("try block lo runtime exception ravachu ani expect chese code untundi. Python aa block ni execute chestundi. Exception vaste, aa point daggara try execution stop ayi Exception Object create avuthundi. Tarvata matching except block ki control transfer avuthundi. Exception lekapothe except execute avvadu.")

Multiple except ante enti?
Python lo oka try block lo different types of Exceptions ravachu. Oka except block anni exceptions ni handle cheyyagaladu, kani real-time enterprise projects lo exception type batti different handling chestaru, Kabatti oka try block ki multiple except blocks rayachu.

Shortly: "Multiple except blocks allow us to handle different exception types in different ways."

Enduku Multiple except use chestham?
    Suppose oka code lo
        File open chestunnam, JSON read chestunnam, Dictionary value access chestunnam.
    Ikkada different exceptions ravachu.
        File Not Found, Invalid JSON, Key Not Found
Prati exception ki same message print cheyyadam professional approach kaadu, Kabatti exception type batti different handling chestham
Syntax: 
    try:
        # Risky Code
    except ExceptionType1:
        # Handle ExceptionType1
    except ExceptionType2:
        # Handle ExceptionType2
    except ExceptionType3:
        # Handle ExceptionType3

Syntax Breakdown:
    try(⭐Mandatory) Runtime exception ravachu ani expect chese code.
    except ExceptionType: Specific exception ni catch chestundi.
    Example: FileNotFoundError, KeyError, ValueError, TypeError, ZeroDivisionError

    Python exception type match ayithe matrame aa except execute avuthundi, Match kakapothe next except Match ayithe Aa except execute avuthundi Match kakapothe next except ki move avuthundi alaa Remaining program continue.

Python anni except blocks execute cheyyadu, Matching except okkate execute avuthundi.
Example:
        except FileNotFoundError
        except KeyError
        except ValueError
    Suppose: KeyError vachindi.
        Execution: Only except KeyError execute avvadu.
    Matching Process: Python Top nundi Bottom varaku "except" blocks check chestundi, First matching block execute chestundi, Remaining "except" blocks ignore chestundi, Kabatti Order important.

Enterprise Automation Usage: Automation Framework lo 
File Handling -> FileNotFoundError
JSON -> JSONDecodeError
Dictionary -> KeyError
API -> ConnectionError or TimeoutError
Playwright -> TimeoutError

"Can multiple except blocks execute for a single exception?"
    "No. Python executes only the first matching except block and skips the remaining ones."

else ante enti?
else anedi Python keyword, Exception Handling lo else block try block lo exception raanappudu matrame execute avuthundi.

Shortly: else block is executed only when the try block completes successfully without any exception.

Enduku else use chestham?
try block lo risky code untundi, Risky code success ayithe next execute cheyyalsina code untundi, Aa code ni try lo rayochu, Kani best practice enti ante Success code ni "else" block lo rayadam.

Reason: Risky code -> try (Success code) -> else (Exception Handling) -> except (Responsibilities clear ga separate avuthayi.)

Syntax: 
    try:
        # Risky Code
    except ExceptionType:
        # Exception Handling
    else:
        # Success Code

Syntax Breakdown:
try(⭐Mandatory): Exception ravachu ani expect chese code.
except(⭐Mandatory): Exception ni handle chestundi.
else(⭐Optional): Exception raanappudu matrame execute avuthundi.

Enterprise Automation Usage:
API Automation: API Call -> Success -> Validate Response (else)
File Handling: Open File -> Success -> Read Data (else)
Database: Connection -> Success -> Execute Query (else)
Playwright: Launch Browser -> Success -> Login (else)

Why else?
Without else:
try -> Risky Code -> Success Code
Problem: Success code lo exception vachina Adi kuda "try" exception laga treat avuthundi, Kabatti Risky code. Success code separate responsibilities maintain cheyyalem.

With else: 
try -> Risky Code -> Success -> else -> Success Code
Responsibilities clear, Code readability improve avuthundi.

try: Risky code execute cheyyadam
except: Exception handle cheyyadam
else: try success ayithe execute avvadam

Interview Explanation: "else in Exception Handling is executed only when the try block completes successfully without raising any exception. It is generally used to place code that should run only after the risky operation succeeds."("else block exception handle cheyyadu. try block successful ga complete ayina tarvata matrame execute avuthundi. try lo exception vaste Python direct ga except block ki transfer avuthundi kabatti else block completely skip avuthundi.")

finally ante enti?
finally anedi Python keyword.
finally block exception vachina, rakapoyina compulsory execute avuthundi.

Simply: "finally block is always executed regardless of whether an exception occurs or not."

Enduku finally use chestham?
Program execution lo konni resources untayi.
Examples: Browser, File, Database Connection, API Session, Network Connection.

Veetini work complete ayyaka close/release cheyyali.

Exception vachina kuda -> Close cheyyali.
Exception rakapoyina kuda -> Close cheyyali.
Kabatti "finally" use chestham.

Syntax: 
    try:
        # Risky Code
    except ExceptionType:
        # Exception Handling
    finally:
        # Cleanup Code

try(⭐Mandatory): Runtime exception ravachu ani expect chese code.
except(⭐Optional (Usually use chestham)): Exception ni handle chestundi.
finally(⭐Optional): Cleanup code rayadaniki.

Important Rule: "finally" execute avvadam ki Exception avasaram ledu, Success avasaram ledu.

Python "finally" ni almost guaranteed cleanup block laga treat chestundi.

Enterprise Automation Usage:
Playwright: Browser Launch -> Login -> Exception vachindi -> Browser Close (finally)
File Handling: Open File -> Read Data -> Exception -> File Close (finally)
Database: Connection Open -> Execute Query -> Exception -> Connection Close (finally)
API Automation: Create Session -> Send Request -> Exception -> Close Session (finally)

Why finally?
Without finally: Browser open gane untundi, Memory leak Resources release avvavu.

With finally: Browser always close avuthundi.

try:	    Risky code execute cheyyadam
except:	    Exception handle cheyyadam
else:	    Success ayithe execute avvadam
finally:	Cleanup code always execute cheyyadam

Execution Order: 
Exception lekapothe: try -> else -> finally -> Remaining Program
Exception vachithe: try -> except -> finally -> Remaining Program

Interview Explanation: "finally is a block that always executes regardless of whether an exception occurs or not. It is mainly used for cleanup activities such as closing files, database connections, browser instances, network sessions, and releasing other resources."("finally exception ni handle cheyyadu. Success ni kuda check cheyyadu. Program try block complete ayina tarvata, exception unna lekapoyina compulsory execute avuthundi. Anduke cleanup operations kosam finally best place.")

Real-Time Enterprise Examples:
Playwright:
    browser.close()
    context.close()
    page.close()

File Handling
    file.close()

Database
    connection.close()
    cursor.close()

API
    session.close()

Ivi chala projects lo finally lo untayi.

Foundation Summary: 
    finally optional block.
    Exception unna execute avuthundi.
    Exception lekapoyina execute avuthundi.
    finally main purpose cleanup.
    Browser, File, Database, API Session lanti resources release cheyyadaniki use chestaru.
    Enterprise frameworks lo finally chala frequently use chestaru.

Important Interview Question:
    Question: finally block execute kakapoye situation unda?
        Normal Answer: Almost always execute avuthundi.
        But technically, konni rare situations lo execute avvakapovachu:
            Program ni forcefully terminate cheyyadam (os._exit()).
            Python interpreter crash avvadam.
            Operating System process ni kill cheyyadam (kill -9 Linux).
        Ivi normal automation interviews lo expect cheyyaru. Interview lo simple ga:
        "finally block always executes and is mainly used for cleanup operations.", ani cheppadam saripothundi.

raise ante enti?
raise anedi Python keyword, Python automatic ga Exception create cheyyagaladu.
Kani konni situations lo maname intentionally Exception create cheyyali, Aa purpose kosame "raise" use chestham.

Simply: "raise is used to manually create and throw an exception."

Enduku "raise" use chestham?
Python ki konni business rules teliyavu.
Example: API Status 200 Python ki Correct, Kani mana application rule 201 compulsory but Python ki idi teliyadu, Kabatti maname Exception create cheyyali, Appude "raise" use chestham.

Syntax: raise ExceptionType("Message")

Syntax Breakdown: 
raise(⭐Mandatory) Python keyword, Exception ni manually trigger chestundi.

ExceptionType(⭐Mandatory) Ye type Exception create cheyyalo.
Examples: Exception, ValueError, TypeError, RuntimeError, KeyError

Message(⭐Optional but Best Practice): Developer ki clear information ivvadaniki.

Important Rule: "raise" Exception ni Handle cheyyadu.
                "raise" Exception ni Create chestundi, Handling "except" responsibility

Python Exception vs raise:
    Python Automatically:
        10 / 0 -> ZeroDivisionError (Python create chestundi.)
    Manually:
        API Status != 200 -> raise -> Exception (Developer create chestadu.)

Enterprise Automation Usage:
   API Automation: Expected Status Code 200 but Actual 500 -> raise -> Test Fail.
   JSON Validation: Key compulsory. 
   Key ledu -> raise -> Validation Fail.
   Playwright: Element compulsory visible.
   Visible ledu -> raise -> Execution Stop.
   Database: Record compulsory undali.
   Record ledu -> raise -> Validation Fail.

Why raise?
Without raise: API -> 500 -> Program Continue 
Wrong Automation Pass aipovachu.

With raise: API -> 500 -> raise -> Exception -> Test Fail (Correct behavior)

try:	Risky code monitor chestundi.
except:	Exception ni catch chesi handle chestundi.
raise:	Exception ni manually create chesi throw chestundi.

Interview Explanation: "raise is a Python keyword used to manually create and throw an exception. It interrupts the normal execution flow by creating an Exception Object and transferring control to the nearest matching except block. It is mainly used to enforce business validations and custom application rules." (raise Python automatic ga generate chese exception kaadu. Developer intentionally Exception Object create cheyyadaniki use chestadu. raise execute ayina ventane normal execution stop ayi, Python matching except block kosam search chestundi. raise exception ni create chestundi; except aa exception ni handle chestundi)

Custom Exception ante enti?
Python already chala built-in Exceptions provide chestundi.
Examples: ValueError, TypeError, KeyError, FileNotFoundError, ZeroDivisionError

Kani mana application ki own business rules untayi, Aa business rules fail ayithe, Python daggara aa Exception undadu, Kabatti maname own Exception create chestham, Danne Custom Exception antaru

Simply: Custom Exception ante developer application requirement kosam create chese own Exception Class.

Enduku Custom Exception use chestham?
Mana own Exception name.
Naming Mostly: InvalidUserException, APIValidationException, DatabaseConnectionException, LoginFailedException, ConfigurationException

Syntax: class CustomException(Exception):
class(⭐Mandatory): Python class create chestundi.
CustomException: Mana own Exception name.
Exception(⭐Mandatory): Python built-in base Exception class, Mana custom class "Exception" ni inherit chestundi, Kabatti mana class Exception laga behave chestundi.

Why Inheritance?
Enduku "Exception" inherit chestham?
Reason: Python except block Exception hierarchy ni search chestundi. Mana class Exception inherit cheyyakapothe Python Exception ga treat cheyyadu.

Why Custom Exception?
Without Custom Exception: Exception vostheye Log Very Generic, Problem exact ga teliyadu.

With Custom Exception: Developer ki Immediate ga Problem ardham avuthundi.

Built-in Exception:	                    Custom Exception:
    Python create chesindi.	                Developer create chestadu.
    Common runtime problems kosam.	        Business/Application rules kosam.
    Already available.	                    Mana requirement batti create chestham.
    Generic usage.	                        Domain specific usage.

raise:	                                Custom Exception:
Exception ni manually throw chestundi.	    Own Exception type create chestundi.
Existing Exception use chestundi.	        New Exception Class create chestundi.
Keyword.	                                Class.

Interview Explanation:
"A Custom Exception is a user-defined exception class created by inheriting from Python's built-in Exception class. It is used to represent application-specific or business-specific validation failures that are not covered by Python's built-in exceptions."("Python built-in Exceptions common runtime problems ni handle chestayi. Kani application-specific validations kosam developer own Exception Class create chestadu. Aa class Exception ni inherit chestundi, kabatti Python danini normal Exception laga handle chestundi. raise use chesi aa Custom Exception ni trigger cheyyachu.")

Real-Time Automation Examples:
API Framework
    InvalidStatusCodeException
    ResponseValidationException
    AuthenticationException
Playwright Framework
    ElementNotVisibleException
    PageLoadException
    LoginFailedException
Database Framework
    RecordNotFoundException
    DuplicateRecordException
Configuration Framework
    InvalidConfigurationException
    EnvironmentVariableException

🎯 Complete Exception Handling Mind Map:
Exception Handling
↓
try
(Risky Code)
↓
Exception vachinda?
↓
No -
    ↓
    else
    ↓
    finally
Yes
    ↓
Python Exception
OR
raise Exception
    ↓
Exception Object
    ↓
Matching except
    ↓
Handle
    ↓
finally

################

doubts: 
1. is Exception Object create by python?
Runtime lo exception situation vachinappudu, Python aa exception ni represent cheyyadaniki Exception Object create chestundi.

Python create chese Exception Object lo multiple different exceptions undavu, Oka particular runtime exception vachinappudu, aa particular exception ki sambandhinchina one Exception Object create avuthundi.

Example: 10 / 0 ZeroDivisionError situation
Python one ZeroDivisionError Exception Object create chestundi.
Aa object lo aa exception ki sambandhinchina information untundi, like exception type/message.

2. So, ippudu manam exception handling implement cheyaledu(try-except), normal code laa "10/0" ani rasam ippud manaki "10/0" ki "ZeroDivisionError" vochindi appud em avuthundi? 
10 / 0 → ZeroDivisionError Exception Object create → exception raise → matching handler lekapothe unhandled exception ga ZeroDivisionError error message tho program terminate avuthundi.

adeye "try-except" implemnation undi "try" block lo "10/0" vundi "except" block lo "ZeroDivisionError" vundi like except ZeroDivisionError: ikkada em message aitheye rasamo adi print avuthundi.
    try:
    result = 10 / 0    #ZeroDivisionError occurs

    except ZeroDivisionError:
    print("Cannot divide by zero")   # Matching except block execute → this message print avuthundi 
    
    anteye ikkada 10/0 ki ZeroDivisionError aneye object python automatic gaa create chesthundi, ikkada manam em idi "ZeroDivisionError" ani python ki chepataledu. python konni exception ki adeye identify chesthundi

3. okka ippudu "try" block vundi and lo code vundi like 10/0 but except lo ZeroDivisionError ledu "valueerror' vundi appudu kudaa python ZeroDivisionError exception throw chesi execution terminate chesthundi right?
    try:
    result = 10 / 0

    except ValueError:
        print("Value error handled")

Ikkada: 
    10 / 0
    → Python ZeroDivisionError identify chestundi
    → ZeroDivisionError Exception Object create & raise chestundi
    → except ValueError check chestundi ❌ Match kaadu
    → ValueError handler execute avvadu
    → ZeroDivisionError unhandled exception ga propagate avuthundi
    → suitable handler ekkada dorakakapothe program execution terminate avuthundi.

    Core point: except lo wrong exception type unte, aa exception handle avvadu. Python original ga vachina ZeroDivisionError ni terminate varaku carry chestundi.

4. Exception handling python in-built haa ledaa manual handling rayalaa ledaa koni in-built vuntayaa koni manual gaa rayalaa?

    Python lo "Exception" mariyu "Exception Handling" rendu different concepts.

    Exception: ante program runtime lo vachina unexpected situation ni represent chese event. Python already konni built-in Exceptions provide chestundi, examples "ZeroDivisionError, ValueError, TypeError, KeyError" etc. Runtime lo corresponding situation vachinappudu Python aa exception type ki sambandhinchina Exception Object ni create chesi raise chestundi.
    Daaniki matching Exception Handling lekunte, exception unhandled ga propagate ayi, suitable handler dorakakapothe program execution terminate avuthundi.

    Exception Handling: ante program lo vachina exception valla program direct ga terminate kakunda, aa exception ni manaki kavalsina way lo properly handle cheyyadam. 
    Daanikosam Python provide chese try, except, else, finally ane keywords/blocks ni use chestam. 
    Built-in Exception aina, manam raise chesi intentionally generate chesina Exception aina, aa exception vachinappudu em action perform cheyyali, ye code execute avvali ane handling logic ni maname define chestam. 
    try block lo exception ravachu ani expect chese risky code ni place chestam. Exception vaste, corresponding except block lo aa exception ki kavalsina handling code execute avuthundi. 
    else block try successful ga complete ayinappudu execute avuthundi, finally block exception vachina, rakapoyina cleanup kosam execute avuthundi.

    Custom Exception different concept. Python already provide cheyyani application-specific or business-specific exception kavali ante, manam Exception class ni inherit chesi own Exception class create chestam. Tarvata requirement batti raise use chesi aa Custom Exception ni intentionally raise cheyyachu, mariyu except use chesi danini handle cheyyachu.

 