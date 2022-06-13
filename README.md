# Examples of code

This repository contains code examples of projects written using **_Python_** and other related technologies: *Django*, *HTML*, *CSS*, *SQLite*, *PostgreSQL*, *Redis*, *Celery*, *Git*, *etc*. Here is just a brief description of each project. For more information, go to the appropriate folder.

Sections: [Apps](#apps), [Bots](#bots), [Utils](#utils), [Tests](#tests).


## Apps

- [`/socialblog`](https://github.com/ptaiga/examples/tree/master/socialblog) &mdash; Test task for creating a blog platform with social media capabilities. The version is implemented using _Python_ and _Django_.

- [`/smarthome`](https://github.com/ptaiga/examples/tree/master/smarthome) &mdash; An example of the interaction between _Smart Home_ systems that supports real-time state configuration. The application is written in _Python_. The following tools are used: _Django_, _SQLite_, _Celery_, _Redis_.

- [`/somemart`](https://github.com/ptaiga/examples/tree/master/somemart) &mdash; Realization of a simple API for an online store: add a product, add a review to the product, get a product description and all reviews for it. All actions are performed via _GET_ or _POST_ requests using _JSON_. Unauthorized users can get a product description or add a review to the product. Admin's rights allow to add new products. User authentication is performed via [_HTTP Basic Auth_](https://en.wikipedia.org/wiki/Basic_access_authentication). Data validation is performed using `django.forms`, `jsonschema` and `marshmallow`. The project is made using _Django_. For testing used `pytest`.

- [`/herokuapp`](https://github.com/ptaiga/examples/tree/master/herokuapp) &mdash; Step-by-step guide to creating a simple web application that shows the number of page views in _Python_ and _Django_ using _Redis_. It also shows how to roll out the application to _Heroku_ hosting using _Git_.

- [`/gameoflife`](https://github.com/ptaiga/examples/tree/master/gameoflife) &mdash; Console utility for demonstrating the famous _"Conway's Game of Life"_. The implementation is made using the _Python_ language and _OOP_ principles.

- [`/asyncsocket`](https://github.com/ptaiga/examples/tree/master/asyncsocket) &mdash; A system for collecting and storing metrics based on a client-server architecture. Examples of such systems are _Graphite_ and _InfluxDB_. The clients and server communicate with each other over a simple text protocol via _TCP-sockets_. To implement an asynchronous server, the following popular _Python_-library is used: _asyncio_. To implement clients, the other popular library is used: _socket_.


## Bots

Bots are written in _Python_, can be run locally and prepared for rolling out to _Heroku_-hosting. Data is stored using _PostgreSQL_ or locally (in-memory and files).

- [`/geotelebot`](https://github.com/ptaiga/examples/tree/master/geotelebot) &mdash; Prototype of a working _Telegram Bot_. Helps the user to save and view interesting places (name, address, geo-position and photo). When sending a location, it shows which of these places are within a 500-meter radius.

- [`/facevoicebot`](https://github.com/ptaiga/examples/tree/master/facevoicebot) &mdash; The bot has two features. One of them is to detect faces in a photos and save only photo with faces (using _OpenCV_). The second feature is getting voice messages, process the frame rate to 16 kHz (256 kbps) and saving it in this form for later use (using _PyDub_).


## Utils

This section contains single-file utilities that perform simple actions. They can be modified and they will be useful in development.

- [`/cipher`](https://github.com/ptaiga/examples/tree/master/cipher) &mdash; Implementation of the _Caesar_ cipher and its two variations _Rot13_ and _Vigenere_. The performance of each of the ciphers is checked by using unit testing.

- [`/kvstore`](https://github.com/ptaiga/examples/tree/master/kvstore) &mdash; Simple key-value storage. Saves data in JSON-format to a file with the following command `$ python keyvaluestorage.py --key KEY --val VAL`. When writing, the new value is added to the previous one. For reading value, you only need to specify the key as a parameter `python keyvaluestorage.py --key KEY`.


## Tests

This section is dedicated to code testing, approaches to testing, etc.

- [`/utestapproaches`](https://github.com/ptaiga/examples/tree/master/utestapproaches) &mdash; using the implementation of sorting algorithm are considered different unit testing approaches: _doctest_, _contracts_, _self-writing tests_, _unittest_, _pytest_.

- [`/primefactor`](https://github.com/ptaiga/examples/tree/master/primefactor) &mdash; TDD on the example of implementation prime factor algorithm.


##

**Note**. If the project contains a `projectname-git.zip`-archive (the full contents of the project and `.git`-folder), you can download and unzip it. As a result you will get the files and commit history of this project.
