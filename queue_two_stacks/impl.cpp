#include "impl.h"

Q::Q(): peekB(false), popMode(false)
{

}
Q::~Q()
{

}
int Q::front() const
{
    return peek;
}
void Q::insert(int value)
{
    if(popMode)
    {
        while(!two.empty())
        {
            one.push(two.top());
            two.pop();
        }
        popMode = false;
    }
    
    if(!peekB)
    {
        peek = value;
        peekB = true;
    }

    one.push(value);
}
void Q::pop()
{
    if(!popMode)
    {
        while(!one.empty())
        {
            two.push(one.top());
            one.pop();
        }
        popMode = true;
    }

    two.pop();

    if(two.empty())
    {
        peekB = false;
    }
    else
    {
        peek = two.top();
    }

}
bool Q::empty()
{
    return (two.empty() && one.empty());
}


