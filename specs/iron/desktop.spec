# Meta Package
Name:           ros-iron-desktop
Version:        0.10.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-desktop and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-desktop
Requires:       ros2-iron-desktop-devel

Obsoletes: ros-iron-desktop < 0.10.0-1

%description
A package which extends 'ros_base' and includes high level packages
like vizualization tools and demos.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.10.0-1
- Update to latest release
