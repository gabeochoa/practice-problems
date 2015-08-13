#include "impl.h"
#include <iostream>


int main(int argc, char** args)
{

    Q queue;

    queue.insert(1);
    queue.insert(2);
    queue.insert(3);
    
    if(queue.front() != 1)
    {
        std::cout << "Front incorrect 1" << "\n";
        return -1;
    }

    queue.pop();
    if(queue.front() != 2)
    {
        std::cout << "Front incorrect 2" << "\n";
        std::cout << queue.front();
        return -1;
    }

    queue.pop();
    if(queue.front() != 3)
    {
        std::cout << "Front incorrect 3" << "\n";
        return -1;
    }

    queue.pop();

    if(!queue.empty())
    {
        std::cout << "Empty incorrect" << "\n";
        return -1;
    }

    return 0;
}