#include <iostream> 
#include <httplib.h>

int main(void)
{
    using namespace httplib;

    std::puts("\n\n ===================================");
    std::puts(" [INFO] Starting Web server. OK");
    
    Server svr;

    svr.Get("/hi", [](const Request& req, Response& res) {
	std::puts(" [INFO] Server route /hi");
        res.set_content("Hello World!", "text/plain");
    });

    svr.Get(R"(/numbers/(\d+))", [&](const Request& req, Response& res) {
	std::puts(" [INFO] Server route /numbers");			  
        auto numbers = req.matches[1];
        res.set_content(numbers, "text/plain");
    });

    svr.Get("/stop", [&](const Request& req, Response& res) {
        std::puts(" [INFO] Server route /stop");			  
        svr.stop();
    });

    std::puts(" [INFO] Running server - listening port 1234");			  
    svr.listen("localhost", 1234);
}
