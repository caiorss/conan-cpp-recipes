import os 
from conans import ConanFile, CMake, tools

# Note: release is the name of the git *tag*
# Download zip archive release from Github and extracts it renaming
# the directory to 'extracted'. 
def DownloadGithubRelease(user, project, release):
    url = "https://github.com/{0}/{1}/archive/v{2}.zip".format(user, project, release)
    extracted_dir = project + "-" + release 
    # Download archive and extract it 
    tools.get(url)
    # Rename directory to 'extracted'    
    os.rename(extracted_dir, "extracted")

class CpptomlConan(ConanFile):
    name = "cpptoml"
    version = "0.1"
    license = "PUBLIC DOMAIN - Modify It at will"
    author = "Caio Rodrigues"
    url = "https://github.com/caiorss/conan-cpp-recipes/recipes/cpptoml"

    description = """Header-only library for parsing TOML configuration files. 
                     Repository: https://github.com/skystrife/cpptoml
                  """
    
    topics = ("toml", "config", "configuration", "parser")
    generators = "cmake"

    def source(self):
        DownloadGithubRelease("skystrife", "cpptoml", "0.1.1")

    def package(self):
        # Copy all *.hpp and *.h files to include directory 
        self.copy("*",        dst = "include",  src = "extracted/include")
        self.copy("LICENSE*", dst = "licenses", src = "extracted")

    def package_info(self):
        self.info.header_only()
