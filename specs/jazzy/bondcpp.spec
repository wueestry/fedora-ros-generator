# Meta Package
Name:           ros-jazzy-bondcpp
Version:        4.1.0
Release:        1%{?dist}
License:        BSD
URL:            http://www.ros.org/wiki/bondcpp
Summary:        Meta package for ros2-jazzy-bondcpp and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-bondcpp
Requires:       ros2-jazzy-bondcpp-devel

Obsoletes: ros-jazzy-bondcpp < 4.1.0-1

%description
C++ implementation of bond, a mechanism for checking when another
process has terminated.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.1.0-1
- Update to latest release
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.4.0.0-1
- Update to latest release
