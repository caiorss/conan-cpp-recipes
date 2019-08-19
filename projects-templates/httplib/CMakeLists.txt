cmake_minimum_required(VERSION 3.14 FATAL_ERROR)
project(cmake-experiment)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_VERBOSE_MAKEFILE ON)

# ============= Conan Bootstrap =============================#

# Download automatically, you can also just copy the conan.cmake file
if(NOT EXISTS "${CMAKE_BINARY_DIR}/conan.cmake")
   message(STATUS "Downloading conan.cmake from https://github.com/conan-io/cmake-conan")
   file(DOWNLOAD "https://github.com/conan-io/cmake-conan/raw/v0.13/conan.cmake"
                 "${CMAKE_BINARY_DIR}/conan.cmake")
endif()

include(${CMAKE_BINARY_DIR}/conan.cmake)

conan_cmake_run( REQUIRES
                # Libraries to be installed locally
                cpp-httplib/0.1@local/testing

                BASIC_SETUP
                BUILD missing
                )

#  ========= Target Configuration ==================== #

add_executable(server server.cpp)
target_link_libraries(server pthread)

