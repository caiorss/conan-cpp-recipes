from conans import ConanFile, CMake
from conans.tools import replace_in_file
import os
import shutil

class ServedLibConan(ConanFile):
    name       = "served"
    version    = "1.6"
    url        ="https://github.com/Wi3ard/conan-cpp-netlib"
    generators = "cmake", "txt"
    settings   = "os", "compiler", "build_type", "arch"
    # requires = "boost/1.71.0@conan/stable"
    requires   = "boost/1.69.0@conan/stable"

    topics     = ("server", "http", "rest", "boost-asio")
    author     = "Caio Rodrigues - caiorss.rodrigues@gmail.com"
    license    = "Public Domain"

    description = """ A restful HTTP library built on top of Boost.Asio 
                      - https://github.com/meltwater/served  """

    options = { "shared"          : [True, False],
                "enable_https"    : [True, False],
                "enable_tests"    : [True, False],
                "enable_examples" : [True, False],                
               }
    default_options = "shared=False", \
        "enable_https=True", \
        "enable_tests=False", \
        "enable_examples=False", \
        "Boost:shared=False"

    def source(self):
        self.run("git clone https://github.com/meltwater/served")
        self.run("cd served && git checkout v1.6.0")

    def build(self):
        cmake = CMake(self)
        cmake.definitions["SERVED_BUILD_SHARED"] = "OFF"
        cmake.definitions["SERVED_BUILD_STATIC"] = "ON"
        cmake.configure(source_folder="served")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def package(self):
        self.copy("*.hpp", dst="include/served", src="served/src/served")
        self.copy("*.ipp", dst="include/served", src="served/src/served")
        # self.copy("*.hpp", dst="include", src="cpp-netlib/deps/asio/asio/include")
        # self.copy("*.ipp", dst="include", src="cpp-netlib/deps/asio/asio/include")
        self.copy("*.dll", dst="bin", src="install/install/bin")
        self.copy("*.lib", dst="lib", src="served/lib")
        self.copy("*.a", dst="lib", src="served/lib")
        self.copy("*.so*", dst="lib", src="served/lib")
        self.copy("*.dylib", dst="lib", src="served/lib")
        self.copy("*.*", dst="lib/CMake", src="install/install/CMake")

    def package_info(self):
        self.cpp_info.libs = ["served"]

        if self.settings.compiler == "gcc" or self.settings.compiler == "apple-clang":
            self.cpp_info.cppflags = ["-std=c++1z"]
