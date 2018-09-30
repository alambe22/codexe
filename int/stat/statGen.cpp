#include <iostream>
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

int count_lines(std::string);
int count_comments(std::string, std::string);
std::string get_libraries(std::string, std::string);

int main(){
    std::string line, libraries;
    int line_num;
    while(std::cin >> line)
    {
        line_num = count_lines(line);
        if(line.substr(line.find_last_of(".")+1) == "py")
        {
            std::cout << line << " " << line_num << " " << count_comments(line, "py")
                << " python " << get_libraries(line, "py")
                << std::endl;
        }
        else if(line.substr(line.find_last_of(".")+1) == "cpp")
        {
            std::cout << line << " " << line_num << " " << count_comments(line, "cpp")
                << " c++ " << get_libraries(line, "cpp")
                << std::endl;
        }
        else if(line.substr(line.find_last_of(".")+1) == "java")
        {
            std::cout << line << " " << line_num << " " << count_comments(line, "java")
                << " java " << get_libraries(line, "java")
                << std::endl;
        }
        else if(line.substr(line.find_last_of(".")+1) == "c")
        {
            std::cout << line << " " << line_num << " " << count_comments(line, "c")
                << " c " << get_libraries(line, "c")
                << std::endl;
        }
        else
        {
            std::cout << line << " " << line_num << " - - -" << std::endl;
        }
    }
}

//Return # of lines in file
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

//Return string of libraries / modules being used
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
        std::stringstream sin(line);
        line_buffer.clear();
        while(sin >> word)
            line_buffer.push_back(word);

        if(ext == "py" || ext == "java")
        {
            if(line_buffer.size() >= 2)
            {
                if(line_buffer[0] == "import")
                {
                    libraries += line_buffer[1] + " ";
                }
                else if(line_buffer[0] == "from")
                {
                    if(line_buffer.size() >= 4)
                        libraries += line_buffer[1] + "." + line_buffer[3] + " ";
                }
            }
        }
        else if (ext == "cpp" || ext == "c")
        {
            if(line_buffer.size() >= 2)
            {
                if(line_buffer[0] == "#include")
                    libraries += line_buffer[1] + " ";
            }
        }
    }

    return libraries;
}

//Return # of comments in file
int count_comments(std::string file_name, std::string ext)
{
    std::ifstream fin;
    std::string line;
    int num_comment = 0;

    fin.open(file_name);
    if(fin.fail())
    {
        std::cerr << file_name << " not found.\n";
        return -1;
    }

    while(std::getline(fin, line))
    {
        if(ext == "py")
        {
            if (line.find("#") != std::string::npos)
                num_comment++;

        }
        if(ext == "cpp" || ext == "c" || ext == "java")
        {
            if (line.find("//") != std::string::npos)
                num_comment++;
        }
    }

    return num_comment;
}
