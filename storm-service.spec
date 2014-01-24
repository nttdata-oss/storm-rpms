%define storm_name storm
%define storm_branch 0.9
%define storm_ver 0.9.0.1
%define storm_version 0.9.0.1
%define release_version 1
%define storm_home /var/lib/storm/%{storm_name}-%{storm_version}
%define config_storm %{storm_home}/conf
%define storm_user storm
%define storm_group storm

Name: storm-service
Version: 0.9.0.1
Release: 1
Summary: Storm Complex Event Processing Daemon Package
Group: Applications/Internet
License: EPLv1
URL: http://storm-project.net
Source: https://github.com/acromusashi/storm-install/storm-service-%{version}.tgz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Requires: storm, sh-utils, textutils, /usr/sbin/useradd, /usr/sbin/usermod, /sbin/chkconfig, /sbin/service
%description
Storm is a distributed realtime computation system.
Similar to how Hadoop provides a set of general primitives for doing batch processing,
Storm provides a set of general primitives for doing realtime computation. Storm is simple,
can be used with any programming language, is used by many companies, and is a lot of fun to use!

The Rationale page on the wiki explains what Storm is and why it was built.
This presentation is also a good introduction to the project.

Storm has a website at storm-project.net.

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install
# Clean out any previous builds not on slash (lol)
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Copy the storm file to the right places
%{__mkdir_p} %{buildroot}/etc/sysconfig
%{__mkdir_p} %{buildroot}/etc/init.d
%{__mkdir_p} %{buildroot}/var/log/storm
%{__mkdir_p} %{buildroot}/var/run/storm

%{__mv} init.d/storm-nimbus init.d/storm-supervisor init.d/storm-ui init.d/storm-drpc %{buildroot}/etc/init.d
%{__mv} sysconfig/storm %{buildroot}/etc/sysconfig/storm


# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%pre
getent group %{storm_group} >/dev/null || groupadd -r %{storm_group}
getent passwd %{storm_user} >/dev/null || /usr/sbin/useradd --comment "Storm Daemon User" --shell /bin/bash -M -r -g %{storm_group} --home /var/lib/storm/default %{storm_user}

%files
%defattr(755,root,root)
/etc/init.d/storm-nimbus
/etc/init.d/storm-supervisor
/etc/init.d/storm-ui
/etc/init.d/storm-drpc
/etc/sysconfig/storm
%defattr(-,%{storm_user},%{storm_group})
/var/log/storm
/var/run/storm/
