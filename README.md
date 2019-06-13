# versinus
Versinus: a visualization method for time-evolving networks

## documentation
Current best documentation is the article in the doc/ directory,
and the resources in this repository.

There is also a dummy and less recent article available in arXiv: https://arxiv.org/abs/1412.7311

## implementations
Versinus was conceived while probing stability of social networks
and was found to be very useful.
It has since then received four implementations:
* a Python script that renders animations though stop-motion, available in legacy/sistemaMinimo_5000Py3.py
* Python functionalities made available though packages. These packages enable the rendering of animations with soundtracks, both obtained by mapping of the evolving network. The packages needed are [gmaneLegacy](https://github.com/ttm/gmaneLegacy) and [musicLegacy](https://github.com/ttm/musicLegacy). After installing them, run the script tests/testEvolutionMusicPy3.py in the gmaneLegacy tree.
* a lightweight Javascript implementation in [ccNetViz](https://github.com/HelikarLab/ccNetViz) for static networks.
* a Javascript implementation for interactive data visualization: https://github.com/ttm/netText.

## public interactive interfaces 
* http://rfabbri.vicg.icmc.usp.br:3000/evolution
* http://rfabbri.vicg.icmc.usp.br:3000/evolution/dev

### available videos
Some animations obtained using the Versinus method (and the scripts mentioned above) 
are available in the following playlists:
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jWYQiJZYhVlJVngb7vsf6na
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jVFS_AJZm_HuO9pywnSWaNF
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jUZpAX3cKPC5J0t3q836CLy
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jVb7CTt59t3ZnrmXuG0N3cO
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jU-1j4jiIUiyMqyVSzIYeh6
* https://www.youtube.com/playlist?list=PLf_EtaMqu3jVodaqDjN7yaSgsQx2Xna3d

## further info
To render the stop-motion animations, you may use ffmpeg. E.g.:
$ ffmpeg -r 25 -i "%05d.png" versinus.mp4

And use ffmpeg again to add the sound track:
$ ffmpeg -i video.avi -i audio.mp3 -codec copy -shortest versinus.avi

### repositories
* https://github.com/ttm/gmaneLegacy
* https://github.com/ttm/gmaneToolkit
* https://github.com/ttm/musicLegacy
* https://github.com/ttm/gmaneMessages
* https://github.com/ttm/gmane

## about
Please refer to the VICG/ICMC group for more information or contact me at:
renato [DOT] fabbri {at} gmail (dot) com

:::
