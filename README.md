# multi-precision-IE-ACHE
Multi-precision Arithmetic Circuit Homomorphic Encryption for Integer Expressions

This project will be integrated to the <a href="https://github.com/kennethsoh/IE-ACHE">main project</a> when ready for deployment.

#### Dependencies
* BOOST Library
```bash
$ cd /
$ sudo apt-get install libboost-all-dev
```

* Fast Fully Homomorphic Encryption over the Torus (https://github.com/tfhe/tfhe)
```bash
$ cd /
$ git clone --recurse-submodules --branch=master https://github.com/tfhe/tfhe.git
$ cd tfhe
$ mkdir build; cd build
$ ccmake ../src

# Press 'c' to configure, then 'g' to generate

$ make
$ make install
```

#### Installation and usage
1. Clone this repository
``` bash
$ git clone https://github.com/kennethsoh/multi-precision-IE-ACHE.git
````

2. Edit operator.txt to set operation value
- 1: Addition
- 2: Subtraction
- 4: Multiplication

3. Compile the c programs 
```bash
$ g++ alice.c -o alice -ltfhe-spqlios-fma
$ g++ cloud.c -o cloud -ltfhe-spqlios-fma
$ g++ process.c -o process -ltfhe-spqlios-fma
$ g++ verif.c -o verif -ltfhe-spqlios-fma
```

4. Execute the compiled C files, starting with process, then alice, cloud, and verif.
