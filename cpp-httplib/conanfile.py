import os 
from conans import ConanFile, CMake, tools

class CpphttplibConan(ConanFile):
    name = "cpp-httplib"
    version = "0.1"
    license = "Public Domain Package Recipe"
    author = "Caio Rodrigues"
    url = "<Package recipe repository url here, for issues about the package>"
    description = """Package recipe for singl-header web server 
                     https://github.com/yhirose/cpp-httplib"""
    topics = ("http", "web", "server")
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/yhirose/cpp-httplib")

    def package(self):
        # Copy all *.h (header files) from (.) current directory to {PACKAGE}/include
        # Note: src = 'cpp-httplib' is the directory where all files are copied.
        self.copy("httplib.h", dst="include", src="cpp-httplib")
        # Copy license to package directory
        self.copy("LICENSE", dst=".", src="cpp-httplib")
        
    def package_info(self):
        # Indicate that the package is header-only
        self.info.header_only()


