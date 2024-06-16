# Meta Package
Name:           ros-jazzy-rcl-lifecycle
Version:        9.2.3
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-jazzy-rcl_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-rcl_lifecycle
Requires:       ros2-jazzy-rcl_lifecycle-devel

Obsoletes: ros-jazzy-rcl-lifecycle < 9.2.3-1

%description
Package containing a C-based lifecycle implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.3-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.9.2.2-1
- Update to latest release
