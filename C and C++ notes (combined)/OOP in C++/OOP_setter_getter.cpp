#include <iostream>
using namespace std;
class stove
{
private: //  Its(private) primary role is to hide the internal implementation details and data of a class from the outside world, preventing direct manipulation and ensuring data integrity
    // we can't access variables inside private outside the class and hiden attribute outside the world
    int temperature = 0;

public:
    stove(int temperature)
    {
        setTemperature(temperature);
    }

    void setTemperature(int temperature)
    { // setter is void function and it returns nothing
        if (temperature < 0)
        {
            this->temperature = 0;
        }
        else if (temperature >= 10)
        {
            this->temperature = 10;
        }
        else
        {
            this->temperature = temperature;
        }
        // adding a getter will make the attribute readable
        // a setter make a private attribute writable
    }

    int getTemperature()
    { // getter is a non void function which returns a value
        return temperature;
        // adding a getter will make the attribute readable
    }
};

int main()
{
    // Abstraction = hiding unnecessary data from a class
    // getter= that make a private attribute readable
    // setter= that make a private attribute writable
    stove s(-4);
    // s.setTemperature(-1);
    cout << "The temperature: " << s.getTemperature();
    return 0;
}