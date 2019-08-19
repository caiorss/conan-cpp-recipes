

test-httplib:
	conan create ./cpp-httplib cpp-httplib/testing

install-httplib:
	conan export ./cpp-httplib local/testing 
