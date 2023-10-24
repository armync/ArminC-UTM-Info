# PA setup

## Compilers

### C++
Use a recent `g++` version: at least `g++-7`, recommended `g++-10`.
```bash
$ sudo add-apt-repository ppa:ubuntu-toolchain-r/test
$ sudo apt update
$ sudo apt install g++-10
# optional: install gcc-10
```

### Java
Use Java 10 or later.
```bash
# java 11
$ sudo add-apt-repository ppa:openjdk-r/ppa
$ sudo apt update
$ sudo apt install openjdk-11-jdk
```

```bash
# java 10
$ wget https://download.java.net/java/GA/jdk10/10/binaries/openjdk-10_linux-x64_bin.tar.gz

$ ls
openjdk-10_linux-x64_bin.tar.gz

$ tar -vxf openjdk-10_linux-x64_bin.tar.gz

$ ls
jdk-10  openjdk-10_linux-x64_bin.tar.gz

$ sudo mv jdk-10/ /usr/lib/jvm/java-10-openjdk-amd64


$ sudo update-alternatives  --install /usr/bin/java java /usr/lib/jvm/java-10-openjdk-amd64/bin/java  20

$ sudo update-alternatives  --install /usr/bin/javac javac /usr/lib/jvm/java-10-openjdk-amd64/bin/javac  20

$ sudo update-alternatives  --config java
# se va selecta numarul corespunzator lui java 10, se introduce numarul, se apasa enter

$ sudo update-alternatives  --config javac
# se va selecta numarul corespunzator lui javac 10, se introduce numarul, se apasa enter

$ javac -version
javac 10

$ java -version
openjdk version "10" 2018-03-20
OpenJDK Runtime Environment 18.3 (build 10+46)
OpenJDK 64-Bit Server VM 18.3 (build 10+46, mixed mode)
```
## check deps

Required for running the local checker.

```bash
# Python 3.0 or later
$ sudo apt install python3 python

# ensure that the "python" command exists
# example: sudo apt install python-is-python3
$ python --version
Python 3.8.2

```

## IDE

* [Visual Studio Code](https://code.visualstudio.com/Download) for `C++` or `Java`
* [IntelliJ IDEA](https://www.jetbrains.com/idea/) for  `Java`

#### VSCode
##### VSCode: install
```bash
# download https://code.visualstudio.com/docs/?dv=linux64_deb

$ sudo dpkg -i ~/Downloads/code_<version>.deb
```

##### VSCode: C++ extension
* open VSCode
* open command shell `CTRL + SHIFT + P`
* type "install" and select `Extensions: Install Extensions`
* search for `C++`
* select `C/C++ Intellisense` from Microsoft (~18M users)
* install
* restart the IDE

##### VSCode: Java extension
* open VSCode
* open command shell `CTRL + SHIFT + P`
* type "install" and select `Extensions: Install Extensions`
* search for `Java`
* select `Language Support for Java` from Red Hat (~9M users)
* install
* restart the IDE

##### VSCode: Markdown extension (local rendering)
* open VSCode
* open command shell `CTRL + SHIFT + P`
* type "install" and select `Extensions: Install Extensions`
* search for `Markdown`
* select `Markdown Preview Enhanced` from Yiyi Wang (~2M users)
* install
* restart the IDE
* `code .` in the root of this repo
* open `setup.md`
* preview the docs

#### IntelliJ IDEA
#### install
```bash
$ sudo add-apt-repository ppa:mmk2410/intellij-idea
$ sudo apt update
$ sudo apt install intellij-idea-community
```
