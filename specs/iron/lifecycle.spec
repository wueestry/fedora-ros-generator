# Meta Package
Name:           ros-iron-lifecycle
Version:        0.27.1
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-lifecycle and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-lifecycle
Requires:       ros2-iron-lifecycle-devel

Obsoletes: ros-iron-lifecycle < 0.27.1-1

%description
Package containing demos for lifecycle implementation

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.0.27.1-1
- Update to latest release
