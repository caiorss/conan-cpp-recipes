#include <iostream>
#include <string>
#include <sstream>

#include <cpptoml.h>

extern const char* tomlData;

template <typename T>
using sh = std::shared_ptr<T>;

int main()
{
    auto is = std::stringstream(tomlData);
    cpptoml::parser p{is};
    sh<cpptoml::table> config = p.parse();

    std::cout << "\n --- TOML Configuration data read from input stream ------\n";

    int loglevel  = config->get_qualified_as<int>("INFO.loglevel").value_or(0);
    auto userName = config->get_qualified_as<std::string>("INFO.user").value_or("unnamed");
    auto file     = config->get_qualified_as<std::string>("INFO.file").value_or("");
    auto port     = config->get_qualified_as<int>("SERVER.port").value_or(8080);
    std::cout << " => loglevel = " << loglevel << "\n"
              << " => userName = " << userName << "\n"
              << " => file     = " << file << "\n"
              << " => port     = " << port << "\n";

    return 0;
}

const char* tomlData = R"(
[INFO]
 loglevel = 10
 user     = "Somebody else"
 file     = "C:\\Users\\somebody\\storage\\data.log"

[SERVER]
  host = "127.0.0.1"
  port = 9090
  directories = [
      "C:\\Users\\somebody\\Document"
     ,"C:\\Users\\somebody\\Upload"
     ,"C:\\Users\\somebody\\Pictures"
  ]

)";

