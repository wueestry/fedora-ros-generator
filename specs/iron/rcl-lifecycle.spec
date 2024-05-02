# Meta Package
Name:           ros-iron-rcl-lifecycle
Version:        6.0.5
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-rcl_lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-rcl_lifecycle
Requires:       ros2-iron-rcl_lifecycle-devel

Obsoletes: ros-iron-rcl-lifecycle < 6.0.5-1

%description
Package containing a C-based lifecycle implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.6.0.5-1
- Update to latest release
