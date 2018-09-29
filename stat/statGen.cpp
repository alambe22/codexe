#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string>

int count_lines(std::string);

int main(){
    std::string line;
    while(std::cin >> line)
    {
        if(line.substr(line.find_last_of(".")+1) == "py")
        {
            std::cout << line << ": " << count_lines(line) << std::endl;
        }
    }
}

int count_lines(std::string file_name)
{
    std::ifstream fin;
    std::string line;
    int line_count = 0;

    fin.open(file_name);
    if(fin.fail())
    {
        std::cerr << file_name << " not found.\n";
        return -1;
    }

   while(std::getline(fin, line)) 
       line_count++;

   return line_count;
}
