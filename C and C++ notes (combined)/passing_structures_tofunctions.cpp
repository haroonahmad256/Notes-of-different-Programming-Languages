#include <iostream>
using namespace std;
struct Fuck
{
    string book;
    int pages;
    string author;
    char present;
};

void book_information(Fuck &book);
void book_information(Fuck book, string how);

int main(){
    Fuck mybook;
    mybook.book= "48 Laws of Power";
    mybook.author= "Williams";
    mybook.pages= 48;
    mybook.present= 'N';
    
    Fuck mybook2;
    mybook2.book= "Rich Dad Poor Dad";
    mybook2.author= "Chinie";
    mybook2.pages= 280;
    mybook2.present= 'Y';
    book_information(mybook);
    book_information(mybook, "very Good");
    
}
void book_information(Fuck &book){   //Here we are passign by reference by removing & it will be called call by valueAQ
    cout<<"Book Name: "<<book.book<<endl;
    cout<<"Book author: "<<book.author<<endl;
    cout<<"Number of pages: "<<book.pages<<endl;
    cout<<"Is present in lirary: "<<book.present<<endl;
    
}

void book_information(Fuck book, string how){
    cout<<book.book<<" "<<how;
}