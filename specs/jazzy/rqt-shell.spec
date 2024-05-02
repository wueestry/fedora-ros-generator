# Meta Package
Name:           ros-jazzy-rqt-shell
Version:        1.2.2
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/rqt_shell
Summary:        Meta package for ros2-jazzy-rqt_shell and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rqt_shell
Requires:       ros2-jazzy-rqt_shell-devel

Obsoletes: ros-jazzy-rqt-shell < 1.2.2-1

%description
rqt_shell is a Python GUI plugin providing an interactive shell.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.2.2-1
- Update to latest release
