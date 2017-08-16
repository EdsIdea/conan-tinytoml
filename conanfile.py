from conans import ConanFile

class TinytomlConan(ConanFile):
    name = "TinyToml"
    version = "0.40"
    exports_sources = "include/*"

    def package(self):
        self.copy("*.h", dst="include", src="include")

