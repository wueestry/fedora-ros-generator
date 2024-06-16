# Meta Package
Name:           ros-iron-tinyxml-vendor
Version:        0.9.2
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-tinyxml_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-tinyxml_vendor
Requires:       ros2-iron-tinyxml_vendor-devel

Obsoletes: ros-iron-tinyxml-vendor < 0.9.2-1

%description
CMake shim over the tinxml library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat May 25 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.9.2-1
- Update to latest release
