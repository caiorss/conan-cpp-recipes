# ======= Install all recipes to local cache =====#
install:
	conan export ./recipes/httplib local/testing
	conan export ./recipes/cpptoml local/testing 

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

#====================================================#

