

test-httplib:
	conan create ./recipes/httplib cpp-httplib/testing

install-httplib:
	conan export ./recipes/httplib local/testing 

#====================================================#

# Install all recipes to local cache 
install:
	conan export ./recipes/httplib local/testing 
