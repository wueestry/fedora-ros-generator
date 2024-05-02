# Meta Package
Name:           ros-jazzy-ament-copyright
Version:        0.17.0
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_copyright and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_copyright
Requires:       ros2-jazzy-ament_copyright-devel

Obsoletes: ros-jazzy-ament-copyright < 0.17.0-1

%description
The ability to check source files for copyright and license
information.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.17.0-1
- Update to latest release
