import pyttsx3
engine = pyttsx3.init()
text = """Kotlin Interview Questions for Freshers.

1. What is Kotlin? 
Kotlin is a modern, statically typed programming language developed by JetBrains. It is fully interoperable with Java and is widely used for Android development.

2. What are the key features of Kotlin? 
Some key features of Kotlin are: Concise syntax, Null safety, Interoperability with Java, Extension functions, and Coroutines for asynchronous programming.

3. What is the difference between val and var in Kotlin? 
val is immutable, meaning its value cannot be reassigned, while var is mutable, meaning its value can be changed.

4. What is a data class in Kotlin? 
A data class is a class that automatically provides useful functions like toString, equals, and hashCode. Example: data class User(val name: String, val age: Int)

5. What is the difference between == and === in Kotlin? 
== checks structural equality (compares values), whereas === checks referential equality (compares memory references).

6. What is a nullable type in Kotlin? 
Kotlin prevents null pointer exceptions by using nullable types. Example: var name: String? = null.

7. What are extension functions in Kotlin? 
Extension functions allow adding new functionality to existing classes without modifying them. Example: fun String.capitalizeFirstLetter() = this[0].uppercase() + this.substring(1).

8. What is a companion object in Kotlin? 
A companion object is used to create static-like methods and properties inside a class.

9. What are coroutines in Kotlin? 
Coroutines help manage asynchronous programming efficiently by avoiding blocking operations.

10. What is the Elvis operator in Kotlin? 
The Elvis operator (?:) provides a default value when encountering null. Example: val name = user?.name ?: "Unknown".

11. What is the difference between listOf and mutableListOf in Kotlin? 
listOf creates an immutable list, while mutableListOf allows modifications.

12. What is the purpose of the sealed class in Kotlin? 
Sealed classes are used for defining restricted class hierarchies, ensuring better type safety.

13. How does Kotlin handle exceptions? 
Kotlin uses try, catch, and finally blocks for exception handling.

14. What is the use of the lateinit keyword in Kotlin? 
lateinit allows the initialization of non-nullable variables at a later point.

15. What is inline function in Kotlin? 
An inline function reduces function call overhead by inlining the function body.

16. What is higher-order function in Kotlin? 
A higher-order function takes another function as a parameter or returns a function.

17. What is lambda expression in Kotlin? 
A lambda expression is an anonymous function used as a concise way to define functions.

18. What is the difference between apply and also in Kotlin? 
apply modifies an object and returns it, while also performs an operation and returns the original object.

19. How does Kotlin handle default arguments? 
Kotlin allows function parameters to have default values, making function calls flexible.

20. What is the difference between suspend and launch in Kotlin? 
suspend is used to define a coroutine function, whereas launch is used to start a coroutine.

End of Kotlin Interview Questions.
"""
engine.say(text)
engine.runAndWait()
