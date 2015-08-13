

#include <stack>


class Q
{
    public: 
        Q();
        ~Q();
        int front() const;
        void insert(int value);
        void pop();
        bool empty();
    private:
        int peek;
        bool peekB;
        bool popMode;
        std::stack<int> one;
        std::stack<int> two;

};