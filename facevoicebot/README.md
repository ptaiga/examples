# Face Detection and Voice Processing Bot

The bot has two features. One of them is to detect faces in a photos and save only photo with faces (using _OpenCV_ library). The second feature is getting voice messages, process the frame rate to 16 kHz (256 kbps) and saving it in `.wav`-file (all this achived using _PyDub_ library).

The bot can be run locally or rolled out to a remote hosting (for example, [_Heroku_](https://www.heroku.com/)). Data is stored using _PostgreSQL_ or locally (in-memory and files).


## Usage

You can send a photo or voice message to the bot.

If the bot detects at least one face in the photo, the photo is saved. The reply message marks the sectors in the photo where face(s) are found.

Voice message will be processed at sampling rate 16 kHz (256 kbps) and saved.

The following commands are available for the bot:

 - `/photo` - Return last saving photo. _"/photo {number}"_ return photo specified by number in saving order.
 - `/voice` - Return last saving voice message. _"/voice {number}"_ return voice message specified by number in saving order.
 - `/reset photos` - Deleted all saved photos.
 - `/reset voices` - Deleted all saved voice messages.


## Guide

### Dependencies

To run the project, the following dependencies must be installed in the virtual environment together with `python3`:

- `pytelegrambotapi` &ndash; module [_pyTelegramBotAPI_](https://github.com/eternnoir/pyTelegramBotAPI) simplifies working with the [_Telegram Bot API_](https://core.telegram.org/bots/api).

- `psycopg2` &ndash; module [_Psycopg_](https://www.psycopg.org/docs/usage.html) is necessary for working with the _PostgreSQL_.

- `opencv-python-headless` &ndash; _OpenCV_ (Open Source Computer Vision Library: http://opencv.org) is an open-source library that includes several hundreds of computer vision algorithms. `opencv-python(-headless)` is the python API for _OpenCV_. It needs for face detection feature.

- `numpy` &ndash; library for the _Python_, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. It uses to prepare data for _OpenCV_.

- `pydub` &ndash; library for audio processing.

- `ffmpeg` &ndash; _Python_ bindings for _FFmpeg_ needed to extract audio from _Telegram_ voice messages presented in `ogg` format.

### Variables, Deploy and Launch

A detailed description of the variables used, how to deploy to _Heroku_ and the launch of the bot can be read at the [link](https://github.com/ptaiga/examples/blob/master/geotelebot/README.md).

It is worth noting that will need to [install an additional buildpack](https://stackoverflow.com/questions/58146519/how-to-use-the-heroku-buildpack-ffmpeg-for-python) to be able to use `ffmpeg`.


## Files

This section gives a description of the project's files/modules.

- `main.py` &ndash; The main file where all the logic of the bot is implemented.

- `storage.py` &ndash; The module is responsible for storing user data. If there is a link to the _PostgreSQL_ instance, the data stored in it. Otherwise, data stored in memory and in files on disk.

- `process.py` &ndash; Module contais functions responsible for detecting faces in photos and for audio processing of voice messages.

- `opencv/haarcascade_frontalface_default.xml` &ndash; _OpenCV_ cascade classifier is necessary for face detection.

- `requirements.txt`, `runtime.txt`, `Procfile` &ndash; These files are required to create a proper environment when the project is deployed to _Heroku_. They are not necessary if the bot is launched locally.


## Useful links

A list of links that will help understand why specific solutions were used during development.

- _PyDub_ for voice processing &ndash; https://github.com/jiaaro/pydub

- How to use the _Heroku_ buildpack `ffmpeg` for _Python_? &ndash; https://stackoverflow.com/questions/58146519/how-to-use-the-heroku-buildpack-ffmpeg-for-python

- Tutorial "Face Detection with _Python_ using _OpenCV_"  &ndash; https://www.datacamp.com/community/tutorials/face-detection-python-opencv

- Use `opencv-python-headless` in production &ndash; https://github.com/opencv/opencv-python/issues/370
