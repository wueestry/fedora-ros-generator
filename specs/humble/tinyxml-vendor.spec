# Meta Package
Name:           ros-humble-tinyxml-vendor
Version:        0.8.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-tinyxml_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-tinyxml_vendor
Requires:       ros2-humble-tinyxml_vendor-devel

Obsoletes: ros-humble-tinyxml-vendor < 0.8.3-1

%description
CMake shim over the tinxml library.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat May 25 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.0.8.3-1
- Update to latest release
