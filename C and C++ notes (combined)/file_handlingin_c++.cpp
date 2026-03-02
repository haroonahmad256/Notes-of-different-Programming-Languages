#include <iostream>
#include <fstream>      //to perform operation related to file handling we add this header file
#include <sstream>      //used to manuplate date that we read in a variable
using namespace std;
int main(){
    //There are many ways to open a file in different modes like

    fstream filein("file.txt", ios::in);            //this file is opening in read mode ios::in is used for read file
    fstream fileout("file.txt", ios::out);          //this file is opening in write mode ios::out is used for read file
    fstream str("file.txt", ios::in | ios::out);    //this file is opening in both write and read mode 
    fstream fileout("file.txt", ios::app);          //this file is opening ios::app  Append (add at end)

    //instead of writing ios::in or out we can ismply use ofstream of writing file and ifstream for reading file

    ofstream fout("data.txt");       //This is most commont form of opening a file
    ofstream fout;  //These two lines are also a way to open a file
    fout.open("data.txt");
    // file_object.open(filename, mode); this is general form

    //To write in file
    ofstream fout("data.txt");   //ofstream is used to open the file in write mode stream namewechoose(file)
    fout << "Hello File";        //printing in file for writing we use <<
    fout.close(); //If we can open a file then we cal also close it

    //To read
    ifstream fin("data.txt");  //opening file in read mode
    string text;               //it is the variable text in which readed data will be stored
    fin >> text;               //for reading >> is used but it Stops at space but there is a solution using getline
    fin.close();               //closing

    //solution of don't reading when space comes between data in file
    ifstream fin("data.txt");
    string line;
    while(getline(fin, line))       //used while to read complete data and store it in variable line
    {
    cout << line << endl;
    }
    fin.close();

    //Checking if File Opened Successfully
    //Function: is_open()
    //after opening file use this to check
    if(fin.is_open())
    {
    cout << "File opened successfully";
    }
    else
    {
    cout << "File not found";
    }
    // Checking if getline() read successfully or not
    if (!getline(fin, line))
        cerr << "Error: Failed to read data" << endl;

    fin.close();

    //End of File 
    //Function: eof()
    while(!fin.eof())  //it is better to use getline instead of eof
    //closing functions of file
    fin.close();
    fout.close();

    //Using fstream (Read + Write)
    fstream file;
    file.open("data.txt", ios::in | ios::out);
    // Read using >> or getline()
    // Write using <<

    int pos = file.tellg(); //get read position
    int pos = file.tellp(); //get write position
    file.seekg(0, ios::beg); //Move read pointer
    file.seekp(0, ios::end); //Move write pointer

    // Binary File Handling
    // Writing Object to Binary File
    ofstream fout("data.bin", ios::binary);
    fout.write((char*)&obj, sizeof(obj));
    // Reading Object
    ifstream fin("data.bin", ios::binary);
    fin.read((char*)&obj, sizeof(obj));

}