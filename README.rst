##################################
README
##################################

.. sectnum::

==========================
Feature
==========================

* Deploy binaries of Storm to /usr/lib/storm.
* Separately make rpms of Storm and Strom init scripts.
* Make "storm" user and "storm" group to start processes.
* Use the "storm" command provided in Storm project to start and stop services.
* Storm 0.9.2-incubating is used in the following procedure.

==========================
Requriement
==========================
* Internet access
* Linux distribution: CentOS6
* JDK6 or JDK7

  + We used Oracle JDK7

* The following packages should be installed.

  + rpm-build
  + zip, unzip

==========================
How to make Storm rpm
==========================

------------------
Clone spec files
------------------
Download spec files from the repository.

command example::

 $ cd <your working directory>
 $ git clone https://github.com/nttdata-oss/storm-rpms
 $ cd storm-rpms
 $ git checkout -b v0.9.2-incubating refs/tags/0.9.2-incubating

------------------------
Download storm binaries
------------------------
Download storm binaries from the official download link.

command example::

 $ wget http://ftp.meisei-u.ac.jp/mirror/apache/dist/incubator/storm/apache-storm-0.9.2-incubating/apache-storm-0.9.2-incubating.zip

Rename zip file.

command example::

 $ unzip -o apache-storm-0.9.2-incubating.zip
 $ mv apache-storm-0.9.2-incubating storm-0.9.2
 $ tar cvzf storm-0.9.2.tgz storm-0.9.2

If you don't have ~/rpmbuild directory,
you need to make directories.

command sample::

 $ mkdir -p ~/rpmbuild/BUILD ~/rpmbuild/BUILDROOT ~/rpmbuild/RPMS ~/rpmbuild/SOURCES ~/rpmbuild/SPECS ~/rpmbuild/SRPMS

Copy tgz file to the rpmbuild directory.

command example::

 $ cp storm-0.9.2.tgz ~/rpmbuild/SOURCES

------------------
Copy spec file
------------------

Copy spec file of storm to the rpmbuild directory.

command example::

 $ cp storm-rpm/storm.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba ~/rpmbuild/SPECS/storm.spec

As a result of this command,
you get ~/rpmbuild/RPMS/x86_64/storm-0.9.2.x86_64.rpm.

================================
How to make Storm service rpm
================================

-------------------------------
Copy scripts and make tar file
-------------------------------
Copy scripts and config files to rpmbuild directory.

command example::

 $ mkdir ~/rpmbuild/SOURCES/storm-service-0.9.2
 $ cp -r storm-rpm/init.d ~/rpmbuild/SOURCES/storm-service-0.9.2
 $ cp -r storm-rpm/sysconfig ~/rpmbuild/SOURCES/storm-service-0.9.2

Make tar file.

command example::

 $ cd ~/rpmbuild/SOURCES
 $ tar cvzf storm-service-0.9.0.tgz storm-service-0.9.0

------------------
Copy spec file
------------------
Copy spec file of storm to the rpmbuild directory.

command example::

 $ cd <your working directory>
 $ cp storm-rpm/storm-service.spec  ~/rpmbuild/SPECS

-----------
Build rpm
-----------
Build rpm.

command example::

 $ rpmbuild -ba ~/rpmbuild/SPECS/storm-service.spec

As a result of this command,
you get ~/rpmbuild/RPMS/x86_64/storm-service-0.9.0.1.x86_64.rpm.

=========================
ToDo
=========================
The following is the main of ToDo.

* Bring init scripts into compliance with LSB.

  + http://refspecs.linuxbase.org/LSB_3.1.1/LSB-Core-generic/LSB-Core-generic/iniscrptact.html

* Gather configration files into /etc/storm directory.
* Use alternatives.
* (Systemd for future)

.. vim: ft=rst tw=0
