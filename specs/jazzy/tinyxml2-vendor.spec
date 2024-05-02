# Meta Package
Name:           ros-jazzy-tinyxml2-vendor
Version:        0.9.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-tinyxml2_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-tinyxml2_vendor
Requires:       ros2-jazzy-tinyxml2_vendor-devel

Obsoletes: ros-jazzy-tinyxml2-vendor < 0.9.1-1

%description
Wrapper around tinyxml2, providing nothing but a dependency on
tinyxml2, on some systems. On others, it provides a fixed CMake module
or even an ExternalProject build of tinyxml2.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.9.1-1
- Update to latest release
