#include <served/served.hpp>

int main(int argc, char const* argv[]) {
	// Create a multiplexer for handling requests
	served::multiplexer mux;

	// GET /hello
	mux.handle("/hello")
		.get([](served::response & res, const served::request & req) {
			res << "Hello world!";
		});

	// Create the server and run with 10 handler threads.
	served::net::server server("127.0.0.1", "9080", mux);
	server.run(10);
	
	return (EXIT_SUCCESS);
}
