# Meta Package
Name:           ros-iron-ament-package
Version:        0.15.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-ament_package and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-ament_package
Requires:       ros2-iron-ament_package-devel

Obsoletes: ros-iron-ament-package < 0.15.3-1

%description
The parser for the manifest files in the ament buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.15.3-1
- Update to latest release
