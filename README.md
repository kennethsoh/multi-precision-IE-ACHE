# multi-precision-IE-ACHE
Multi-precision Arithmetic Circuit Homomorphic Encryption for Integer Expressions

This project will be integrated to the <a href="https://github.com/kennethsoh/IE-ACHE">main project</a> when ready for deployment.

<b>Important!</b>
No licence has been added to this work.

Copyright © 2019-2020 <br>
All rights reserved. No part of this publication may be reproduced, distributed, or transmitted in any form or by any means, including photocopying, recording, or other electronic or mechanical methods, without the prior written permission of the publisher, except in the case of brief quotations embodied in critical reviews and certain other noncommercial uses permitted by copyright law. For permission requests, write to the publisher, addressed “Attention: Permissions Coordinator,” at the addresses below:<br>
kennethsoh@yahoo.com.sg; tewzhenghong@outlook.com; dominic1js@gmail.com; chengjing32@yahoo.com

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
$ python3 compile.py
```

4. Execute the compiled C files, starting with process, then alice, cloud, and verif.
```bash
# Value 1
$ ./process
$ ./alice

# Value 2
$ ./process
$ ./alice

# Compute
$ ./cloud

# Verify
$ ./verif
```

For >2 client setup:
```bash
# Value 1
$ ./process
$ ./alice

# Value 2
$ ./process
$ ./alice

# Compute
$ ./cloud

# Delete cloud.data
$ rm cloud.data

# Value 3
$ ./process
$ ./alice

# Add answer from first compute to cloud.data
$ cat answer.data >> cloud.data

# Compute again
$ ./cloud

# Verify
$ ./verif
```




