Title: Pelican Getting Started 
date: 07/11/2015
tags: 
category: Pelican 
slug: pelicanGettingStarted

# Quick Start #

Now we have the installation completed,  [Pelican Installation ]({filename}pelicanInstallation.md). We are ready to getting started by making a sample blog, Pelican has an inbuilt utility to make it, we can execute it by issuing the command.

````
pelican-quickstart
````

If every thing is fine, you will get a set of question which we will discuss later, but if something is wrong, like in my case, I was on Mac OS X, and it gave me this error.

````
Traceback (most recent call last):
  File "/Users/user/anaconda/bin/pelican-quickstart", line 7, in <module>
    from pelican.tools.pelican_quickstart import main
  File "/Users/user/anaconda/lib/python2.7/site-packages/pelican/__init__.py", line 20, in <module>
    from pelican.generators import (ArticlesGenerator, PagesGenerator,
  File "/Users/user/anaconda/lib/python2.7/site-packages/pelican/generators.py", line 22, in <module>
    from pelican.readers import Readers
  File "/Users/user/anaconda/lib/python2.7/site-packages/pelican/readers.py", line 9, in <module>
    import docutils.core
  File "/Users/user/anaconda/lib/python2.7/site-packages/docutils/core.py", line 20, in <module>
    from docutils import frontend, io, utils, readers, writers
  File "/Users/user/anaconda/lib/python2.7/site-packages/docutils/frontend.py", line 41, in <module>
    import docutils.utils
  File "/Users/user/anaconda/lib/python2.7/site-packages/docutils/utils/__init__.py", line 20, in <module>
    import docutils.io
  File "/Users/user/anaconda/lib/python2.7/site-packages/docutils/io.py", line 18, in <module>
    from docutils.utils.error_reporting import locale_encoding, ErrorString, ErrorOutput
  File "/Users/user/anaconda/lib/python2.7/site-packages/docutils/utils/error_reporting.py", line 47, in <module>
    locale_encoding = locale.getlocale()[1] or locale.getdefaultlocale()[1]
  File "/Users/user/anaconda/lib/python2.7/locale.py", line 543, in getdefaultlocale
    return _parse_localename(localename)
  File "/Users/user/anaconda/lib/python2.7/locale.py", line 475, in _parse_localename
    raise ValueError, 'unknown locale: %s' % localename
ValueError: unknown locale: UTF-8
````

## ValueError: unknown locale: UTF-8 ##

We get a `ValueError`, Now the solution of this is proposed in one Stackoverflow Question [here](http://stackoverflow.com/questions/19961239/pelican-3-3-pelican-quickstart-error-valueerror-unknown-locale-utf-8), 

We have to add these two line in our bashrc file.

````
export LC_ALL=en_US.UTF-8
export LANG=en_US.UTF-8
````

Once we add this line, we can again issue the `pelican-quickstart` command to get to the 10 question.