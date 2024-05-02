# Meta Package
Name:           ros-jazzy-foonathan-memory-vendor
Version:        1.3.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-foonathan_memory_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-foonathan_memory_vendor
Requires:       ros2-jazzy-foonathan_memory_vendor-devel

Obsoletes: ros-jazzy-foonathan-memory-vendor < 1.3.1-1

%description
Foonathan/memory vendor package for Fast-RTPS.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.3.1-1
- Update to latest release
