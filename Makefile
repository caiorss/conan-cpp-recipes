# ======= Install all recipes to local cache =====#
install:
        # Http client/server library 
	conan export ./recipes/httplib local/testing
        # Toml configuration parser 
	conan export ./recipes/cpptoml local/testing
        # Http server library built on top of Boost.Asio 
	conan export ./recipes/served  local/testing 

#======== Recipe: cpptoml  ======================#

test-cpptoml:
	conan create ./recipes/cpptoml cpp-httplib/testing

install-cpptoml:
	conan export ./recipes/cpptoml local/testing 


#======== Recipe: cpp-httplib  ======================#

test-httplib:
	conan create ./recipes/httplib cpp-httplib/testing

install-httplib:
	conan export ./recipes/httplib local/testing 

#======== Recipe: served REST http library (Boost Asio) ======#

test-served:
	conan create ./recipes/served  served/testing

install-served:
	conan export ./recipes/served served/testing 


