# Meta Package
Name:           ros-iron-rqt-shell
Version:        1.1.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_shell
Summary:        Meta package for ros2-iron-rqt_shell and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rqt_shell
Requires:       ros2-iron-rqt_shell-devel

Obsoletes: ros-iron-rqt-shell < 1.1.1-1

%description
rqt_shell is a Python GUI plugin providing an interactive shell.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.1.1-1
- Update to latest release
