#include <iostream>
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int count_lines(std::string);
//std::ifstream open_file(std::string);
std::string get_libraries(std::string, std::string);

int main(){
    std::string line;
    while(std::cin >> line)
    {
        if(line.substr(line.find_last_of(".")+1) == "py")
        {
            std::cout << line << std::endl;
            std::cout << count_lines(line) << std::endl;
            std::cout << get_libraries(line, "py") << std::endl;
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

    fin.close();
    return line_count;
}

std::string get_libraries(std::string file_name, std::string ext)
{
    std::ifstream fin;
    std::string line, word;
    std::string libraries = "";
    std::vector<std::string> line_buffer;

    fin.open(file_name);
    if(fin.fail())
    {
        std::cerr << file_name << " not found.\n";
        return "";
    }

    while(std::getline(fin, line)) 
    {
        line_buffer.clear();
        if(ext == "py")
        {
            std::stringstream sin(line);
            while(sin >> word)
                line_buffer.push_back(word);
            if(line_buffer.size() >= 2)
            {
                if(line_buffer[0] == "import")
                {
                    libraries += line_buffer[1] + " ";
                }
                else if(line_buffer[0] == "from")
                {
                    if(line_buffer.size() >= 4)
                    {
                        libraries += line_buffer[1] + "." + line_buffer[3] + " ";
                    }
                }
            }
        }
    }

    return libraries;
}


/*
   std::ifstream open_file(std::string file_name)
   {
   std::ifstream fin;
   fin.open(file_name);
   if(fin.fail())
   {
   std::cerr << file_name << " not found.\n";
   return -1;
   }

   return fin;
   }*/
