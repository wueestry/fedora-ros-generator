# Meta Package
Name:           ros-jazzy-desktop
Version:        0.11.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-desktop and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-desktop
Requires:       ros2-jazzy-desktop-devel

Obsoletes: ros-jazzy-desktop < 0.11.0-1

%description
A package which extends 'ros_base' and includes high level packages
like vizualization tools and demos.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.11.0-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.10.0-1
- Update to latest release
