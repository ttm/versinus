# versinus
Versinus: a visualization method for time-evolving networks

## documentation
Current best documentation is the article in the doc/ directory and available in arXiv: https://arxiv.org/abs/1412.7311

## implementations
Versinus was conceived while probing stability of social networks
and was found to be very useful.
It has since then received three implementations:
* a Python+FFmpeg that renders animations though stop-motion.
* a Javascript implementation in [ccNetViz](https://github.com/HelikarLab/ccNetViz) for static networks.
* a Javascript implementation using BabylonJS for interactive data analysis (Visual Analytics).

## found scripts
* gmaneLegacy makes audio and png files
* sistemaMinimo_5000.py may have the most advanced implementation of all...

## further info
To render the stop-motion animations, you may use ffmpeg. E.g.:
$ ffmpeg -r 25 -i "%05d.png" totoro.mp4

And use ffmpeg again to add the sound track:
$ ffmpeg -i video.avi -i audio.mp3 -codec copy -shortest output.avi
Issues:
* how to control the number of images/second used. -r seems to be only the final framerate.
* how to input the sound file rendered?

### repositories
* https://github.com/ttm/gmaneLegacy
* https://github.com/ttm/gmaneToolkit
* https://github.com/ttm/musicLegacy
* https://github.com/ttm/gmaneMessages
* https://github.com/ttm/gmane


## about
Please refer to the VICG/ICMC group for more information or contact me at:
renato [DOT] fabbri {at} gmail (dot) com

