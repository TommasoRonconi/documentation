# TFM of MBH

This is a template module for documenting an hybrid code using a blend of
- Sphinx
- Breathe
- Doxygen
- Meson

Be(a)ware of The F***ing Manual!!

All the credit goes to [Sy Brand's tutorial](https://devblogs.microsoft.com/cppblog/clear-functional-c-documentation-with-sphinx-breathe-doxygen-cmake/) who
implemented basicaly the same thing but using `CMake`. I have just ported it to `meson`.

**_Note_** The name _MBH_ refers to a cool [Instagram profile](https://www.instagram.com/monstersholdingbitches/) that you will love, if you are a weirdo like myself...

## Dependencies

All of these are available in `conda`:
- meson
- ninja
- sphinx
- breathe

Thus you could just create the `doc` environment with the kindly provided yaml: [doc_environment.yml](useful/doc_environment.yml).

| If you do not have Anaconda or Miniconda, these packages are also available with `pip` |
| :------------------------------------------------------------------------------------: |
| ... but there must be something wrong with you.                                        |

Other dependency you do not want to forget:
- Doxygen

But you'll have to install this manualy (_"ehy! what year is this? 2005??"_).