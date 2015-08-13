TARGET := q2s
EXECUTABLE := test

SRC_FILES := \
	q2s.cpp \
	impl.h \
	impl.cpp 

OBJ_FILES := \
	q2s.o \
	impl.o 

CXX := clang++
CXXFLAGS := -std=c++11 -Wall -Wextra -Wpedantic

$(EXECUTABLE): $(OBJ_FILES)
	$(CXX) $(OBJ_FILES) -o $(EXECUTABLE)

clean:
	rm -rf *.o *~ $(EXECUTABLE)

depend:
	$(CXX) $(CXXFLAGS) -MM *.cpp

q2.o: q2s.cpp impl.h
impl.o: impl.cpp impl.h

run:
	./test
