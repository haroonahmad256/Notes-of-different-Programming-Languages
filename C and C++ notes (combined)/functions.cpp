//Functions in c++ are similar to C language. The differences are explained: 
/*
Similarities:
Basic Syntax: A function's core structure (name, parameters, return type, body) is largely the same for simple, non-OOP functions.
C Standard Library: C++ can call most C library functions (like printf, malloc). 

Key Differences:
Function Overloading: C++ allows multiple functions with the same name but different parameters; C does not.
Member Functions: C++ functions can exist inside classes (as methods) to operate on object data; C structures cannot contain functions.
Default Arguments: C++ supports optional parameters (e.g., void func(int x=0)); C requires all arguments to be provided.
Namespaces: C++ uses namespaces to organize code and prevent name clashes (e.g., std::cout); C does not have this feature.
Function Prototypes: C++ strictly requires function prototypes (declarations) before use; C is more lenient (though C99/C11 enforce it more).
main() Function: In C++, main() must return an int; in C, void main() was sometimes allowed (though int main() is standard in C too).
printf/scanf vs. cin/cout: C uses stdio.h functions, while C++ typically uses iostream objects. 

Important:
If we want to write the function below the main function then we have to write function prototype of that function
before the main function
*/