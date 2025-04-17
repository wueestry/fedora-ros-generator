# Meta Package
Name:           ros-jazzy-ament-package
Version:        0.16.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-ament_package and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-ament_package
Requires:       ros2-jazzy-ament_package-devel

Obsoletes: ros-jazzy-ament-package < 0.16.4-1

%description
The parser for the manifest files in the ament buildsystem.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.16.4-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.16.3-1
- Update to latest release
