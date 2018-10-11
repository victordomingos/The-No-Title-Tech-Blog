Title: Count Files v1.4 – new features and finally available on PyPI!
Date: 2018-09-09 16:25
Lang: en
Tags: python, cli, files, file management, file count, file extension, argparse, pypi
Category: Programming
Slug: count_files_v1_4_available_on_pypi
Author: Victor Domingos
Cover: images/2018/count-files_1_4_haiku.png
Summary: The latest release of this file counting command-line utility has just been released. It is a platform independent (pure Python) package that makes it easy to count files by extension. This version has some useful new features. It was tested in a wide range on environments and, for the first time, it is now available on PyPI, which means you can just `pip install` it as any other Python package.


Our team member [Nataliia Bondarenko](https://github.com/NataliaBondarenko){target=:_blank} has done an amazing work in several areas of the project, especially the implementation of the unit test system, as well as adding new features and improving documentation. Thank you very much, Nataliia!

Here are some highlights:

 * Reworked some of the internals so that the application is a lot faster and more responsive.
 * Added visual feedback while the computer is processing.
 * Added an option to count the total number of files.
 * Added full support for handling hidden files and folders.
 * Updated preview for text files and added list of supported types.
 * Added support for (optional) case sensitiveness.
 * Added support for search/count files without extension (.) or all files(..).
 * Optional display of file sizes.
 * More detailed help system.
 * Tests for different operating systems.
 * Added extensive documentation in English, Portuguese, Russian and Ukrainian.
 * Refactored module into a full package and created the setup.py file.
 * It's now available on PyPI.org: just `pip install` it! 😉


To install it, if you have Python 3.6+, just type `pip3 install count-files` on the command-line. More detailed info, including some iOS specific procedures, is available on the documentation.

So, go ahead and see the updated documentation, which also includes lots of usage examples, to get you started right away:

- [English](https://countfiles.readthedocs.io/en/latest/){target=:_blank}
- [Portugu&ecirc;s](https://github.com/victordomingos/Count-files/blob/master/docs/Documentation_PT.md){target=:_blank}
- [&#x420;&#x443;&#x441;&#x441;&#x43A;&#x438;&#x439;](https://github.com/victordomingos/Count-files/tree/master/docs/documentation_ru/README.md){target=:_blank}
- [&#x423;&#x43A;&#x440;&#x430;&#x457;&#x43D;&#x441;&#x44C;&#x43A;&#x430;](https://github.com/victordomingos/Count-files/blob/master/docs/README_UA.md){target=:_blank}


